from fastapi.testclient import TestClient

from db.database import SessionLocal, get_db
from main import app

client = TestClient(app)


def override_get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


def test_create_bahan():
    bahan_data = {"nama_bahan": "Garam", "satuan": "sdm"}
    response = client.post("/bahan/", json=bahan_data)
    assert response.status_code == 201
    assert response.json()["data"]["nama_bahan"] == "Garam"
    assert response.json()["data"]["satuan"] == "sdm"


def test_create_bahan_missing_fields():
    bahan_data = {"nama_bahan": "Garam"}
    response = client.post("/bahan/", json=bahan_data)
    assert response.status_code == 400
    assert response.json()[
        "message"] == "Invalid input data"


def test_create_bahan_duplicate_name():
    bahan_data = {"nama_bahan": "Garam", "satuan": "sdm"}
    response = client.post("/bahan/", json=bahan_data)
    assert response.status_code == 409
    assert response.json()[
        "message"] == "Bahan with name Garam already exists"


def test_get_bahan():
    response = client.get("/bahan/1")
    assert response.status_code == 200
    assert response.json()["data"]["nama_bahan"] == "Garam"
    assert response.json()["data"]["satuan"] == "sdm"


def test_get_bahan_not_found():
    response = client.get("/bahan/999")
    assert response.status_code == 404
    assert response.json()["message"] == "Bahan with ID 999 is not found"


def test_get_bahan_by_name():
    response = client.get("/bahan/?nama_bahan=Garam")
    assert response.status_code == 200
    assert response.json()["data"]["nama_bahan"] == "Garam"
    assert response.json()["data"]["satuan"] == "sdm"


def test_get_bahan_by_name_not_found():
    response = client.get("/bahan/?nama_bahan=Unknown bahan")
    assert response.status_code == 404
    assert response.json()[
        "message"] == "Bahan with name Unknown bahan is not found"


def test_get_all_bahan():
    response = client.get("/bahan/")
    assert response.status_code == 200
    assert len(response.json()["data"]) == 1


def test_get_all_bahan_with_pagination():
    response = client.get("/bahan/?offset=0&page_size=1")
    assert response.status_code == 200
    assert len(response.json()["data"]) == 1


def test_get_all_bahan_with_filters():
    response = client.get("/bahan/?nama_bahan=Garam&satuan=sdm")
    assert response.status_code == 200
    assert len(response.json()["data"]) == 1


def test_get_all_bahan_with_sorting():
    response = client.get("/bahan/?sort_by=nama_bahan&sort_order=asc")
    assert response.status_code == 200
    assert response.json()["data"][0]["nama_bahan"] == "Garam"


def test_get_all_bahan_not_found():
    response = client.get("/bahan/?nama_bahan=Unknown bahan")
    assert response.status_code == 404
    assert response.json()["message"] == "No bahan found"


def test_update_bahan():
    response = client.put(
        "/bahan/1", json={"nama_bahan": "Garam Spesial"})
    assert response.status_code == 200
    assert response.json()["data"]["nama_bahan"] == "Garam Spesial"


def test_update_bahan_not_found():
    response = client.put(
        "/bahan/1000", json={"nama_bahan": "Garam Spesial"})
    assert response.status_code == 404
    assert response.json()["message"] == "Bahan with ID 1000 is not found"


def test_update_bahan_with_no_fields():
    response = client.put("/bahan/1", json={})
    assert response.status_code == 400
    assert response.json()[
        "message"] == "At least one field is required to update bahan"


def test_update_bahan_with_invalid_field():
    response = client.put("/bahan/1", json={"invalid_field": "Invalid Value"})
    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "invalid_field"]


def test_delete_bahan():
    response = client.delete("/bahan/1")
    assert response.status_code == 204


def test_delete_bahan_not_found():
    response = client.delete("/bahan/1000")
    assert response.status_code == 404
    assert response.json()["message"] == "Bahan with ID 1000 is not found"
