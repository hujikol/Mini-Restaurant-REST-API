from sqlalchemy.orm import Session

from app.db import schemas
from app.models import models


def create_kategori(db: Session, kategori: schemas.KategoriCreate):
    db_kategori = db.query(models.Kategori).filter(models.Kategori.nama_kat == kategori.nama_kat).first()
    if db_kategori:
        return {"error": {"message": f"Kategori with name {kategori.nama_kat} already exists"}}, 409
    db_kategori = models.Kategori(nama_kat=kategori.nama_kat)
    db.add(db_kategori)
    db.commit()
    db.refresh(db_kategori)
    return {"success": {"message": "New kategori created"}, "data": db_kategori}, 201

def get_kategori(db: Session, kategori_id: int):
    db_kategori = db.query(models.Kategori).filter(models.Kategori.id == kategori_id).first()
    if not db_kategori:
        return {"error": {"message": f"Kategori with id {kategori_id} is not found"}}, 404
    return {"success": {"message": "Kategori found"}, "data": db_kategori}, 200

def get_kategori_by_name(db: Session, nama_kat: str):
    db_kategori = db.query(models.Kategori).filter(models.Kategori.nama_kat == nama_kat).first()
    if not db_kategori:
        return {"error": {"message": f"Kategori with name {nama_kat} is not found"}}, 200
    return {"success": {"message": "Kategori found"}, "data": db_kategori}, 200

def get_all_kategori(db: Session, skip: int = 0, limit: int = 100):
    db_kategori = db.query(models.Kategori).offset(skip).limit(limit).all()
    return {"success": {"message": "All kategori returned"}, "data": db_kategori}, 200

def update_kategori(db: Session, kategori_id: int, kategori: schemas.KategoriUpdate):
    db_kategori = get_kategori(db, kategori_id)["data"]
    if not db_kategori:
        return {"error": {"message": f"Kategori with id {kategori_id} is not found"}}, 200
    for var, value in kategori.__dict__.items():
        if value is not None:
            setattr(db_kategori, var, value)
    db.commit()
    db.refresh(db_kategori)
    return {"success": {"message": f"Kategori with id {kategori_id} is updated"}, "data": db_kategori}, 200

def delete_kategori(db: Session, kategori_id: int):
    db_kategori = get_kategori(db, kategori_id)["data"]
    if not db_kategori:
        return {"error": {"message": f"Kategori with id {kategori_id} is not found"}}, 200
    db.delete(db_kategori)
    db.commit()
    return {"success": {"message": f"Kategori with id {kategori_id} is deleted"}, "data": db_kategori}, 200
