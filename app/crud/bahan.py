from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from db import schemas
from models import models



def create_bahan(db: Session, bahan: schemas.BahanCreate):
    if not bahan.nama_bahan or not bahan.satuan:
        return {"error": {"message": "Invalid input data"}}, 400
    try:
        db_bahan = models.Bahan(nama_bahan=bahan.nama_bahan, satuan=bahan.satuan)
        db.add(db_bahan)
        db.commit()
        db.refresh(db_bahan)
        return {"success": {"message": "New bahan created"}, "data": db_bahan}, 201
    except IntegrityError:
        db.rollback()
        return {"error": {"message": f"Bahan with name {bahan.nama_bahan} already exists"}}, 409


def get_bahan(db: Session, bahan_id: int):
    db_bahan = db.query(models.Bahan).filter(models.Bahan.id == bahan_id).first()
    if not db_bahan:
        return {"error": {"message": f"Bahan with id {bahan_id} is not found"}}, 404
    return {"success": {"message": "Bahan found"}, "data": db_bahan}, 200

def get_bahan_by_name(db: Session, nama_bahan: str):
    db_bahan = db.query(models.Bahan).filter(models.Bahan.nama_bahan == nama_bahan).first()
    if not db_bahan:
        return {"error": {"message": f"Bahan with name {nama_bahan} is not found"}}, 404
    return {"success": {"message": "Bahan found"}, "data": db_bahan}, 200

def get_all_bahan(db: Session, skip: int = 0, limit: int = 100):
    db_bahan = db.query(models.Bahan).offset(skip).limit(limit).all()
    return {"success": {"message": "All bahan returned"}, "data": db_bahan}, 200

def update_bahan(db: Session, bahan_id: int, bahan: schemas.BahanUpdate):
    if not bahan.__dict__:
        return {"error": {"message": "Invalid input data"}}, 400
    db_bahan = get_bahan(db, bahan_id)["data"]
    if not db_bahan:
        return {"error": {"message": f"Bahan with id {bahan_id} is not found"}}, 404
    for var, value in bahan.__dict__.items():
        if value is not None:
            setattr(db_bahan, var, value)
    db.commit()
    db.refresh(db_bahan)
    return {"success": {"message": f"Bahan with id {bahan_id} updated"}, "data": db_bahan}, 200

def delete_bahan(db: Session, bahan_id: int):
    db_bahan = get_bahan(db, bahan_id)["data"]
    if not db_bahan:
        return {"error": {"message": f"Bahan with id {bahan_id} is not found"}}, 404
    db.delete(db_bahan)
    db.commit()
    return {"success": {"message": f"Bahan with id {bahan_id} is deleted"}, "data": db_bahan}, 200
