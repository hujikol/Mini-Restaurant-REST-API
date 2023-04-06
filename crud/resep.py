from sqlalchemy.orm import Session

from app.db import schemas
from app.models import models


def create_resep(db: Session, resep: schemas.ResepCreate):
    db_resep = db.query(models.Resep).filter(models.Resep.nama_resep == resep.nama_resep).first()
    if db_resep:
        return {"error": {"message": "Resep already exists"}}, 409
    db_resep = models.Resep(nama_resep=resep.nama_resep, kategori_id=resep.kategori_id)
    db.add(db_resep)
    db.commit()
    db.refresh(db_resep)
    return {"success": {"message": "New resep created"}, "data": db_resep}, 201

def get_resep(db: Session, resep_id: int):
    return db.query(models.Resep).filter(models.Resep.id == resep_id).first()

def get_all_resep(db: Session, skip: int = 0, limit: int = 100, nama_resep: str = None, kategori_id: int = None):
    query = db.query(models.Resep)
    total_data = query.count()
    
    if nama_resep:
        query = query.filter(models.Resep.nama_resep.ilike(f"%{nama_resep}%"))
    if kategori_id:
        query = query.filter(models.Resep.kategori_id == kategori_id)
    
    resep = query.offset(skip).limit(limit).all()
    return resep, total_data

def update_resep(db: Session, resep_id: int, resep: schemas.ResepUpdate):
    db_resep = get_resep(db, resep_id)
    if not db_resep:
        return None
    for var, value in resep.__dict__.items():
        if value is not None:
            setattr(db_resep, var, value)
    db.commit()
    db.refresh(db_resep)
    return db_resep


def delete_resep(db: Session, resep_id: int):
    db_resep = get_resep(db, resep_id)
    if db_resep is not None:
        db.delete(db_resep)
        db.commit()
    
    return db_resep
