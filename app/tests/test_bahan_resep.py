# Import necessary modules and functions
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from main import app
from db.database import get_db
from crud.bahanResep import create_bahan_resep, get_bahan_resep, get_bahan_by_resep_id, get_resep_by_bahan_ids, get_all_bahan_resep, update_bahan_resep, delete_bahan_resep
from models.schemas import Bahan_ResepCreate, Bahan_ResepUpdate

# Create a test client to make requests to the API
client = TestClient(app)

# Define test data
test_bahan_resep = {
    "resep_id": 1,
    "bahan_id": 1,
    "jumlah": 2
}
test_update_data = {
    "jumlah": 3
}

# Define test functions for each CRUD function


def test_create_bahan_resep(db: Session):
    response = client.post("/bahan_resep/", json=test_bahan_resep)
    assert response.status_code == 201
    assert response.json()["data"]["resep_id"] == test_bahan_resep["resep_id"]
    assert response.json()["data"]["bahan_id"] == test_bahan_resep["bahan_id"]
    assert response.json()["data"]["jumlah"] == test_bahan_resep["jumlah"]


def test_get_bahan_resep(db: Session):
    create_bahan_resep(db, Bahan_ResepCreate(**test_bahan_resep))
    response = client.get(
        f"/bahan_resep/{test_bahan_resep['resep_id']}/{test_bahan_resep['bahan_id']}")
    assert response.status_code == 200
    assert response.json()["data"]["resep_id"] == test_bahan_resep["resep_id"]
    assert response.json()["data"]["bahan_id"] == test_bahan_resep["bahan_id"]
    assert response.json()["data"]["jumlah"] == test_bahan_resep["jumlah"]


def test_get_bahan_by_resep_id(db: Session):
    create_bahan_resep(db, Bahan_ResepCreate(**test_bahan_resep))
    response = client.get(f"/bahan_resep/resep/{test_bahan_resep['resep_id']}")
    assert response.status_code == 200
    assert len(response.json()["data"]) == 1
    assert response.json()[
        "data"][0]["resep_id"] == test_bahan_resep["resep_id"]
    assert response.json()[
        "data"][0]["bahan_id"] == test_bahan_resep["bahan_id"]
    assert response.json()["data"][0]["jumlah"] == test_bahan_resep["jumlah"]


def test_get_resep_by_bahan_ids(db: Session):
    create_bahan_resep(db, Bahan_ResepCreate(**test_bahan_resep))
    response = client.get(
        f"/bahan_resep/bahan/?bahan_ids={test_bahan_resep['bahan_id']}")
    assert response.status_code == 200
    assert len(response.json()["data"]) == 1
    assert response.json()["data"][0] == test_bahan_resep["resep_id"]


def test_get_all_bahan_resep(db: Session):
    create_bahan_resep(db, Bahan_ResepCreate(**test_bahan_resep))
    response = client.get("/bahan_resep/")
    assert response.status_code == 200
    assert len(response.json()["data"]) == 1
    assert response.json()[
        "data"][0]["resep_id"] == test_bahan_resep["resep_id"]
    assert response.json()[
        "data"][0]["bahan_id"] == test_bahan_resep["bahan_id"]
    assert response.json()["data"][0]["jumlah"] == test_bahan_resep["jumlah"]


def test_update_bahan_resep(db: Session):
    create_bahan_resep(db, Bahan_ResepCreate(**test_bahan_resep))
    response = client.put(
        f"/bahan_resep/{test_bahan_resep['resep_id']}/{test_bahan_resep['bahan_id']}", json=test_update_data)
    assert response.status_code == 200
    assert response.json()["data"]["resep_id"] == test_bahan_resep["resep_id"]
    assert response.json()["data"]["bahan_id"] == test_bahan_resep["bahan_id"]
    assert response.json()["data"]["jumlah"] == test_update_data["jumlah"]


def test_delete_bahan_resep(db: Session):
    create_bahan_resep(db, Bahan_ResepCreate(**test_bahan_resep))
    response = client.delete(
        f"/bahan_resep/{test_bahan_resep['resep_id']}/{test_bahan_resep['bahan_id']}")
    assert response.status_code == 204
    assert get_bahan_resep(
        db, test_bahan_resep["resep_id"], test_bahan_resep["bahan_id"])[1] == 404

# Define a function to run all the tests


def test_all():
    with TestClient(app) as client:
        with get_db() as db:
            # Run each test function with the database session
            test_create_bahan_resep(db)
            test_get_bahan_resep(db)
            test_get_bahan_by_resep_id(db)
            test_get_resep_by_bahan_ids(db)
            test_get_all_bahan_resep(db)
            test_update_bahan_resep(db)
            test_delete_bahan_resep(db)
