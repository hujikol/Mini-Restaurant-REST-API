from typing import List
from sqlalchemy.orm import Session

from app.models import models, schemas


def create_bahan_resep(db: Session, bahan_resep: schemas.Bahan_ResepCreate):

    # Create a new Bahan_Resep object and add it to the database.
    # Validate input data
    if not all([bahan_resep.resep_id, bahan_resep.bahan_id, bahan_resep.jumlah]):
        return {"message": "Invalid input data"}, 400

    # Check if bahan is already connected to resep
    db_bahan_resep = get_bahan_resep(
        db, bahan_resep.resep_id, bahan_resep.bahan_id)
    if db_bahan_resep:
        return {"message": f"Bahan with id {bahan_resep.bahan_id} is already connected to resep with id {bahan_resep.resep_id}"}, 409

    # Create new bahan_resep object and add to database
    db_bahan_resep = models.Bahan_Resep(
        resep_id=bahan_resep.resep_id, bahan_id=bahan_resep.bahan_id, jumlah=bahan_resep.jumlah)
    db.add(db_bahan_resep)
    db.commit()
    db.refresh(db_bahan_resep)

    # Return success response
    return {"message": f"Bahan with id {bahan_resep.bahan_id} successfully connected to resep with id {bahan_resep.resep_id}", "data": db_bahan_resep}, 201


def get_bahan_resep(db: Session, resep_id: int, bahan_id: int):

    # Get a Bahan_Resep object from the database by its resep_id and bahan_id.

    db_bahan_resep = db.query(models.Bahan_Resep).filter(
        models.Bahan_Resep.resep_id == resep_id, models.Bahan_Resep.bahan_id == bahan_id).first()

    if not db_bahan_resep:
        return {"message": f"Bahan with id {bahan_id} is not connected into any resep"}, 404

    return {"message": "Bahan for resep found", "data": db_bahan_resep}, 200


def get_bahan_by_resep_id(db: Session, resep_id: int, offset: int = 0, page_size: int = 100):

    # Get all Bahan_Resep objects from the database by their resep_id.

    db_bahan_resep = db.query(models.Bahan_Resep).filter(
        models.Bahan_Resep.resep_id == resep_id).offset(offset).limit(page_size).all()

    if not db_bahan_resep:
        return {"message": f"Bahan for resep id {resep_id} are not found"}, 404

    return {"message": f"All Bahan for resep id {resep_id} are found", "data": db_bahan_resep}, 200


def get_resep_by_bahan_ids(db: Session, bahan_ids: List[int], offset: int = 0, page_size: int = 100):

    # Get all Resep objects from the database that contain the given list of bahan_ids.

    db_bahan_resep = db.query(models.Bahan_Resep).filter(
        models.Bahan_Resep.bahan_id.in_(bahan_ids)).offset(offset).limit(page_size).all()

    if not db_bahan_resep:
        return {"message": f"No resep found for given bahan ids"}, 404

    resep_ids = set([bahan_resep.resep_id for bahan_resep in db_bahan_resep])
    for bahan_id in bahan_ids[1:]:
        db_bahan_resep = db.query(models.Bahan_Resep).filter(
            models.Bahan_Resep.bahan_id == bahan_id).offset(offset).limit(page_size).all()
        resep_ids.intersection_update(
            set([bahan_resep.resep_id for bahan_resep in db_bahan_resep]))

    if not resep_ids:
        return {"message": f"No resep found for given bahan ids"}, 404

    return {"message": f"All Resep for given bahan ids are found", "data": list(resep_ids)}, 200


def get_all_bahan_resep(db: Session, offset: int = 0, page_size: int = 100):

    # Get all Bahan_Resep objects from the database.

    db_bahan_resep = db.query(models.Bahan_Resep).offset(
        offset).limit(page_size).all()
    return {"message": "All bahan returned", "data": db_bahan_resep}, 200


def update_bahan_resep(db: Session, resep_id: int, bahan_id: int, bahan: schemas.Bahan_ResepUpdate):

    # Update a Bahan_Resep object in the database by its resep_id and bahan_id.
    db_bahan_resep = get_bahan_resep(db, resep_id, bahan_id)["data"]

    if not db_bahan_resep:
        return {"message": f"Bahan with id {bahan_id} not found"}, 404

    update_data = {k: v for k, v in bahan.dict(exclude_unset=True).items()}
    for var, value in update_data.items():
        if value is not None:
            setattr(db_bahan_resep, var, value)
    db.commit()
    db.refresh(db_bahan_resep)

    return {"message": f"Bahan with id {bahan_id} for resep id {resep_id} updated", "data": db_bahan_resep}, 200


def delete_bahan_resep(db: Session, resep_id: int, bahan_id: int):

    # Delete a Bahan_Resep object from the database by its resep_id and bahan_id.

    db_bahan_resep = get_bahan_resep(db, resep_id, bahan_id)

    if not db_bahan_resep:
        return {"message": f"Bahan with id {bahan_id} is not match to any resep"}, 404

    db.delete(db_bahan_resep)
    db.commit()

    return {"message": f"Bahan with id {bahan_id} for resep id {resep_id} is deleted", "data": db_bahan_resep}, 204
