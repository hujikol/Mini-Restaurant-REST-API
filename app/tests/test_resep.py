from fastapi.testclient import TestClient
from app.db.database import SessionLocal, get_db
from app.main import app

client = TestClient(app)


def override_get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


def test_create_resep():
    resep_data = {"nama_resep": "Nasi Goreng", "kategori_id": 1}
    response = client.post("/resep/", json=resep_data)
    assert response.status_code == 201
    assert response.json()["data"]["nama_resep"] == "Nasi Goreng"
    assert response.json()["data"]["kategori_id"] == 1


def test_create_resep_missing_fields():
    resep_data = {"nama_resep": "Nasi Goreng"}
    response = client.post("/resep/", json=resep_data)
    assert response.status_code == 400
    assert response.json()[
        "message"] == "Nama resep and kategori ID are required"


def test_create_resep_duplicate_name():
    resep_data = {"nama_resep": "Nasi Goreng", "kategori_id": 1}
    response = client.post("/resep/", json=resep_data)
    assert response.status_code == 409
    assert response.json()[
        "message"] == "Resep with name Nasi Goreng already exists"


def test_get_resep():
    response = client.get("/resep/1")
    assert response.status_code == 200
    assert response.json()["data"]["nama_resep"] == "Nasi Goreng"
    assert response.json()["data"]["kategori_id"] == 1


def test_get_resep_not_found():
    response = client.get("/resep/999")
    assert response.status_code == 404
    assert response.json()["message"] == "Resep with ID 999 is not found"


def test_get_resep_by_name():
    response = client.get("/resep/?nama_resep=Nasi Goreng")
    assert response.status_code == 200
    assert response.json()["data"]["nama_resep"] == "Nasi Goreng"
    assert response.json()["data"]["kategori_id"] == 1


def test_get_resep_by_name_not_found():
    response = client.get("/resep/?nama_resep=Unknown Resep")
    assert response.status_code == 404
    assert response.json()[
        "message"] == "Resep with name Unknown Resep is not found"


def test_get_all_resep():
    response = client.get("/resep/")
    assert response.status_code == 200
    assert len(response.json()["data"]) == 1


def test_get_all_resep_with_pagination():
    response = client.get("/resep/?offset=0&page_size=1")
    assert response.status_code == 200
    assert len(response.json()["data"]) == 1


def test_get_all_resep_with_filters():
    response = client.get("/resep/?nama_resep=Nasi Goreng&kategori_id=1")
    assert response.status_code == 200
    assert len(response.json()["data"]) == 1


def test_get_all_resep_with_sorting():
    response = client.get("/resep/?sort_by=nama_resep&sort_order=asc")
    assert response.status_code == 200
    assert response.json()["data"][0]["nama_resep"] == "Nasi Goreng"


def test_get_all_resep_not_found():
    response = client.get("/resep/?nama_resep=Unknown Resep")
    assert response.status_code == 404
    assert response.json()["message"] == "No resep found"


def test_update_resep():
    response = client.put(
        "/resep/1", json={"nama_resep": "Nasi Goreng Spesial"})
    assert response.status_code == 200
    assert response.json()["data"]["nama_resep"] == "Nasi Goreng Spesial"


def test_update_resep_not_found():
    response = client.put(
        "/resep/1000", json={"nama_resep": "Nasi Goreng Spesial"})
    assert response.status_code == 404
    assert response.json()["message"] == "Resep with ID 1000 is not found"


def test_update_resep_with_no_fields():
    response = client.put("/resep/1", json={})
    assert response.status_code == 400
    assert response.json()[
        "message"] == "At least one field is required to update resep"


def test_update_resep_with_invalid_field():
    response = client.put("/resep/1", json={"invalid_field": "Invalid Value"})
    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "invalid_field"]


def test_delete_resep():
    response = client.delete("/resep/1")
    assert response.status_code == 204


def test_delete_resep_not_found():
    response = client.delete("/resep/1000")
    assert response.status_code == 404
    assert response.json()["message"] == "Resep with ID 1000 is not found"
