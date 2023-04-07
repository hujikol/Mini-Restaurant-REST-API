from sqlalchemy.orm import Session
from db import schemas
from models import models

def create_resep(db: Session, resep: schemas.ResepCreate):
    if not resep.nama_resep or not resep.kategori_id:
        return {"error": {"message": "Nama resep and kategori ID are required"}}, 400
    
    db_resep = db.query(models.Resep).filter(models.Resep.nama_resep == resep.nama_resep).first()
    if db_resep:
        return {"error": {"message": f"Resep with name {resep.nama_resep} already exists"}}, 409

    db_resep = models.Resep(nama_resep=resep.nama_resep, kategori_id=resep.kategori_id)
    db.add(db_resep)
    db.commit()
    db.refresh(db_resep)
    
    return {"data": db_resep, "message": "New resep created"}, 201

def get_resep(db: Session, resep_id: int):
    db_resep = db.query(models.Resep).get(resep_id)
    if not db_resep:
        return {"error": {"message": f"Resep with ID {resep_id} is not found"}}, 404
    
    return {"data": db_resep, "message": "Resep found"}, 200

def get_resep_by_name(db: Session, nama_resep: str):
    db_resep = db.query(models.Resep).filter(models.Resep.nama_resep == nama_resep).first()
    if not db_resep:
        return {"error": {"message": f"Resep with name {nama_resep} is not found"}}, 404
    
    return {"data": db_resep, "message": "Resep found"}, 200

def get_all_resep(db: Session, offset: int = 0, page_size: int = 100, nama_resep: str = None, kategori_id: int = None, sort_by: str = None, sort_order: str = "asc"):
    query = db.query(models.Resep)
    total_data = query.count()
    
    if nama_resep:
        query = query.filter(models.Resep.nama_resep.ilike(f"%{nama_resep}%"))
    if kategori_id:
        query = query.filter(models.Resep.kategori_id == kategori_id)
    
    if sort_by:
        column = getattr(models.Resep, sort_by, None)
        if column is not None:
            if sort_order.lower() == "desc":
                column = column.desc()
            query = query.order_by(column)

    resep = query.offset(offset).limit(page_size).all()
    
    return {"data": resep, "total_data": total_data, "message": "All resep retrieved"}, 200

def update_resep(db: Session, resep_id: int, resep: schemas.ResepUpdate):
    if not any([resep.nama_resep, resep.kategori_id]):
        return {"error": {"message": "At least one field is required to update resep"}}, 400
    
    db_resep = db.query(models.Resep).get(resep_id)
    if not db_resep:
        return {"error": {"message": f"Resep with ID {resep_id} is not found"}}, 404

    resep_dict = dict(resep)
    for var, value in resep_dict.items():
        if value is not None:
            setattr(db_resep, var, value)
    
    db.commit()
    db.refresh(db_resep)
    
    return {"data": db_resep, "message": "Resep updated"}, 200


def delete_resep(db: Session, resep_id: int):
    db_resep = db.query(models.Resep).filter_by(id=resep_id).first()
    if not db_resep:
        return {"message": f"Resep with ID {resep_id} is not found"}, 404
    
    db.delete(db_resep)
    db.commit()
    
    return {"message": "Resep deleted successfully"}, 204

