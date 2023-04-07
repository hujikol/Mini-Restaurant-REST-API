from sqlalchemy.orm import Session

from db import schemas
from models import models


def create_bahan_resep(db: Session, bahan_resep: schemas.Bahan_ResepCreate):
    if not bahan_resep.resep_id or not bahan_resep.bahan_id or not bahan_resep.jumlah:
        return {"error": {"message": "Invalid input data"}, "data": None}, 400
    
    db_bahan_resep = get_bahan_resep(db, bahan_resep.resep_id , bahan_resep.bahan_id)
    
    if db_bahan_resep:
        return {"error": {"message": f"Bahan with id {bahan_resep.bahan_id} is already connected into resep id {bahan_resep.resep_id}"}, "data" : None}, 409
    
    db_bahan_resep = models.Bahan_Resep(resep_id=bahan_resep.resep_id, bahan_id=bahan_resep.bahan_id, jumlah=bahan_resep.jumlah)
    
    db.add(db_bahan_resep)
    db.commit()
    db.refresh(db_bahan_resep)
    
    return {"success": {"message": f"bahan with id {bahan_resep.bahan_id} sucessfully connected to resep id {bahan_resep.resep_id}"}, "data": db_bahan_resep}, 201

def get_bahan_resep(db: Session, resep_id: int, bahan_id: int):
    db_bahan_resep = db.query(models.Bahan_Resep).filter(models.Bahan_Resep.resep_id == resep_id, models.Bahan_Resep.bahan_id == bahan_id).first()
    
    if not db_bahan_resep:
        return {"error": {"message": f"Bahan with id {bahan_id} is not connected into any resep"}}, 404
    
    return {"success": {"message": "Bahan for resep found"}, "data": db_bahan_resep}, 200

def get_bahan_resep_by_resep_id(db: Session, resep_id: int, skip: int = 0, limit: int = 100):
    db_bahan_resep = db.query(models.Bahan_Resep).filter(models.Bahan_Resep.resep_id == resep_id).offset(skip).limit(limit).all()
    
    if not db_bahan_resep:
        return {"error": {"message": f"Bahan for resep id {resep_id} are not found"}}, 404
    
    return {"success": {"message": "All Bahan for resep id {resep_id} are found"}, "data": db_bahan_resep}, 200

def get_all_bahan_resep(db: Session, skip: int = 0, limit: int = 100):
    db_bahan_resep = db.query(models.Bahan_Resep).offset(skip).limit(limit).all()
    return {"success": {"message": "All bahan returned"}, "data": db_bahan_resep}, 200

def update_bahan_resep(db: Session, resep_id: int, bahan_id: int, bahan: schemas.Bahan_ResepUpdate):
    db_bahan_resep = get_bahan_resep(db, resep_id, bahan_id)["data"]
    
    if not db_bahan_resep:
        return {"error": {"message": f"Bahan with id {bahan_id} not found"}}, 404
    
    for var, value in bahan.__dict__.items():
        if value is not None:
            setattr(db_bahan_resep, var, value)
    db.commit()
    db.refresh(db_bahan_resep)
    
    return {"success": {"message": f"Bahan with id {bahan_id} for resep id {resep_id} updated"}, "data": db_bahan_resep}, 200


def delete_bahan_resep(db: Session, resep_id: int, bahan_id: int):
    db_bahan_resep = get_bahan_resep(db, resep_id, bahan_id)
    
    if not db_bahan_resep:
        return {"error": {"message": f"Bahan with id {bahan_id} is not match to any resep"}}, 404
    
    db.delete(db_bahan_resep)
    db.commit()
    
    return {"success": {"message": f"Bahan with id {bahan_id} for resep id {resep_id} is deleted"}, "data": db_bahan_resep}, 200


