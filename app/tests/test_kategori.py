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


def test_create_kategori():
    kategori_data = {"nama_kat": "Main Course"}
    response = client.post("/kategori/", json=kategori_data)
    assert response.status_code == 201
    assert response.json()["data"]["nama_kat"] == "Main Course"


def test_create_kategori_missing_fields():
    kategori_data = {"nama_kat": "Main Course"}
    response = client.post("/kategori/", json=kategori_data)
    assert response.status_code == 400
    assert response.json()[
        "message"] == "Nama kategori are required"


def test_create_kategori_duplicate_name():
    kategori_data = {"nama_kat": "Main Course"}
    response = client.post("/kategori/", json=kategori_data)
    assert response.status_code == 409
    assert response.json()[
        "message"] == "kategori with name Main Course already exists"


def test_get_kategori():
    response = client.get("/kategori/1")
    assert response.status_code == 200
    assert response.json()["data"]["nama_kat"] == "Main Course"


def test_get_kategori_not_found():
    response = client.get("/kategori/999")
    assert response.status_code == 404
    assert response.json()["message"] == "kategori with ID 999 is not found"


def test_get_kategori_by_name():
    response = client.get("/kategori/?nama_kat=Main Course")
    assert response.status_code == 200
    assert response.json()["data"]["nama_kat"] == "Main Course"


def test_get_kategori_by_name_not_found():
    response = client.get("/kategori/?nama_kat=Unknown kategori")
    assert response.status_code == 404
    assert response.json()[
        "message"] == "kategori with name Unknown kategori is not found"


def test_get_all_kategori():
    response = client.get("/kategori/")
    assert response.status_code == 200
    assert len(response.json()["data"]) == 1


def test_get_all_kategori_with_pagination():
    response = client.get("/kategori/?offset=0&page_size=1")
    assert response.status_code == 200
    assert len(response.json()["data"]) == 1


def test_get_all_kategori_with_filters():
    response = client.get("/kategori/?nama_kat=Main Course")
    assert response.status_code == 200
    assert len(response.json()["data"]) == 1


def test_get_all_kategori_with_sorting():
    response = client.get("/kategori/?sort_by=nama_kat&sort_order=asc")
    assert response.status_code == 200
    assert response.json()["data"][0]["nama_kat"] == "Main Course"


def test_get_all_kategori_not_found():
    response = client.get("/kategori/?nama_kat=Unknown kategori")
    assert response.status_code == 404
    assert response.json()["message"] == "No kategori found"


def test_update_kategori():
    response = client.put(
        "/kategori/1", json={"nama_kat": "Main Course Spesial"})
    assert response.status_code == 200
    assert response.json()["data"]["nama_kat"] == "Main Course Spesial"


def test_update_kategori_not_found():
    response = client.put(
        "/kategori/1000", json={"nama_kat": "Main Course Spesial"})
    assert response.status_code == 404
    assert response.json()["message"] == "kategori with ID 1000 is not found"


def test_update_kategori_with_no_fields():
    response = client.put("/kategori/1", json={})
    assert response.status_code == 400
    assert response.json()[
        "message"] == "At least one field is required to update kategori"


def test_update_kategori_with_invalid_field():
    response = client.put(
        "/kategori/1", json={"invalid_field": "Invalid Value"})
    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "invalid_field"]


def test_delete_kategori():
    response = client.delete("/kategori/1")
    assert response.status_code == 204


def test_delete_kategori_not_found():
    response = client.delete("/kategori/1000")
    assert response.status_code == 404
    assert response.json()["message"] == "kategori with ID 1000 is not found"
