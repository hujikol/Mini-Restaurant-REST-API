from sqlalchemy.orm import Session
from db import schemas
from models import models


def create_resep(db: Session, resep: schemas.ResepCreate):
    if not resep.nama_resep or not resep.kategori_id:
        return {"message": "Nama resep and kategori ID are required"}, 400

    db_resep = db.query(models.Resep).filter(
        models.Resep.nama_resep == resep.nama_resep).first()
    if db_resep:
        return {"message": f"Resep with name {resep.nama_resep} already exists"}, 409

    db_resep = models.Resep(nama_resep=resep.nama_resep,
                            kategori_id=resep.kategori_id)
    db.add(db_resep)
    db.commit()
    db.refresh(db_resep)

    return {"message": "New resep created", "data": db_resep}, 201


def get_resep(db: Session, resep_id: int):
    db_resep = db.query(models.Resep).get(resep_id)
    if not db_resep:
        return {"message": f"Resep with ID {resep_id} is not found"}, 404

    return {"message": "Resep found", "data": db_resep}, 200


def get_resep_by_name(db: Session, nama_resep: str):
    db_resep = db.query(models.Resep).filter(
        models.Resep.nama_resep == nama_resep).first()
    if not db_resep:
        return {"message": f"Resep with name {nama_resep} is not found"}, 404

    return {"message": f"Resep with name {nama_resep} is found", "data": db_resep}, 200


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

    db_resep = db_resep.offset(offset).limit(page_size).all()

    if len(db_resep) == 0:
        return {"message": "No resep found"}, 404

    return {"message": "All resep retrieved", "data": db_resep, "total_data": total_data}, 200


def update_resep(db: Session, resep_id: int, resep: schemas.ResepUpdate):
    db_resep = db.query(models.Resep).get(resep_id)
    if not db_resep:
        return {"message": f"Resep with ID {resep_id} is not found"}, 404

    if not any([resep.nama_resep, resep.kategori_id]):
        return {"message": "At least one field is required to update resep"}, 400

    update_data = {k: v for k, v in resep.dict(exclude_unset=True).items()}
    for key, value in update_data.items():
        setattr(db_resep, key, value)

    db.commit()
    db.refresh(db_resep)

    return {"message": f"Resep with id {resep_id} is updated", "data": db_resep}, 200


def delete_resep(db: Session, resep_id: int):
    db_resep = db.query(models.Resep).filter_by(id=resep_id).first()
    if not db_resep:
        return {"message": f"Resep with ID {resep_id} is not found"}, 404

    db.delete(db_resep)
    db.commit()

    return {"message": "Resep deleted successfully"}, 204
