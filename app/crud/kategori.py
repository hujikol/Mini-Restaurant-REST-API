from sqlalchemy.orm import Session

from db import schemas
from models import models


def create_kategori(db: Session, kategori: schemas.KategoriCreate):
    db_kategori = db.query(models.Kategori).filter(
        models.Kategori.nama_kat == kategori.nama_kat).first()

    if db_kategori:
        return {"message": f"Kategori with name {kategori.nama_kat} already exists"}, 409

    db_kategori = models.Kategori(nama_kat=kategori.nama_kat)
    db.add(db_kategori)
    db.commit()
    db.refresh(db_kategori)

    return {"message": "New kategori created", "kategori": db_kategori}, 201


def get_kategori(db: Session, kategori_id: int):
    db_kategori = db.query(models.Kategori).filter(
        models.Kategori.id == kategori_id).first()

    if not db_kategori:
        return {"message": f"Kategori with id {kategori_id} is not found"}, 404

    return {"message": "Kategori found", "data": db_kategori}, 200


def get_kategori_by_name(db: Session, nama_kat: str):
    db_kategori = db.query(models.Kategori).filter(
        models.Kategori.nama_kat == nama_kat).first()

    if not db_kategori:
        return {"message": f"Kategori with name {nama_kat} is not found"}, 404

    return {"message": "Kategori found", "data": db_kategori}, 200


def get_all_kategori(db: Session, offset: int = 0, page_size: int = 100):
    db_kategori = db.query(models.Kategori).offset(
        offset).limit(page_size).all()

    total_data = db.query(models.Kategori).count()

    return {"message": "All kategori returned", "total_data": total_data, "data": db_kategori}, 200


def update_kategori(db: Session, kategori_id: int, kategori: schemas.KategoriUpdate):
    db_kategori = db.query(models.Kategori).filter_by(id=kategori_id).first()

    if not db_kategori:
        return {"message": f"Kategori with id {kategori_id} is not found"}, 404

    if not any([kategori.nama_kat]):
        return {"message": "At least one field is required to update kategori"}, 400

    update_data = {k: v for k, v in kategori.dict(exclude_unset=True).items()}
    for key, value in update_data.items():
        setattr(db_kategori, key, value)

    db.commit()
    db.refresh(db_kategori)

    return {"message": f"Kategori with id {kategori_id} is updated", "data": db_kategori}, 200


def delete_kategori(db: Session, kategori_id: int):
    db_kategori = get_kategori(db, kategori_id)["data"]

    if not db_kategori:
        return {"message": f"Kategori with id {kategori_id} is not found"}, 404

    db.delete(db_kategori)
    db.commit()

    return {"message": f"Kategori with id {kategori_id} is deleted"}, 200
