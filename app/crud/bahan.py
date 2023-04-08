from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models import models, schemas


def create_bahan(db: Session, bahan: schemas.BahanCreate):
    # Check if input data is valid
    if not bahan.nama_bahan or not bahan.satuan:
        return {"message": "Invalid input data"}, 400

    try:
        # Create a new Bahan object and add it to the database
        db_bahan = models.Bahan(
            nama_bahan=bahan.nama_bahan, satuan=bahan.satuan)
        db.add(db_bahan)
        db.commit()
        db.refresh(db_bahan)

        # Return success response with the new Bahan object
        return {"message": "New bahan created", "data": db_bahan}, 201

    except IntegrityError:
        # If the Bahan already exists in the database, return a 409 error message
        db.rollback()
        return {"message": f"Bahan with name {bahan.nama_bahan} already exists"}, 409


def get_bahan(db: Session, bahan_id: int):
    # Query the database for the Bahan with the given ID
    db_bahan = db.query(models.Bahan).filter(
        models.Bahan.id == bahan_id).first()

    # Check if the Bahan was found in the database
    if not db_bahan:
        return {"message": f"Bahan with id {bahan_id} is not found"}, 404

    # Return success response with the Bahan object
    return {"message": "Bahan found", "data": db_bahan}, 200


def get_bahan_by_name(db: Session, nama_bahan: str):
    # Query the database for the Bahan with the given name
    db_bahan = db.query(models.Bahan).filter(
        models.Bahan.nama_bahan == nama_bahan).first()

    # Check if the Bahan was found in the database
    if not db_bahan:
        return {"message": f"Bahan with name {nama_bahan} is not found"}, 404

    # Return success response with the Bahan object
    return {"message": "Bahan found", "data": db_bahan}, 200


def get_all_bahan(db: Session, offset: int = 0, page_size: int = 100, nama_bahan: str = None, sort_by: str = 'id', sort_order: str = "asc"):
    # Start building the query with the Bahan model
    query = db.query(models.Bahan)
    total_data = query.count()

    # Apply filters based on optional parameters
    if nama_bahan:
        query = query.filter(models.Bahan.nama_bahan.ilike(f"%{nama_bahan}%"))

    # Apply sorting based on optional parameters
    if sort_by:
        column = getattr(models.Bahan, sort_by, None)
        if column is not None:
            if sort_order.lower() == "desc":
                column = column.desc()
            query = query.order_by(column)

    # Execute the query with pagination
    db_bahan = db_bahan.offset(offset).limit(page_size).all()

    # Check if any bahan were found
    if len(db_bahan) == 0:
        return {"message": "No bahan found"}, 404

    # Return success response with the list of bahan and total count
    return {"message": "All bahan retrieved", "total_data": total_data, "data": db_bahan}, 200


def update_bahan(db: Session, bahan_id: int, bahan: schemas.BahanUpdate):
    # Query the database for the Bahan with the given ID
    db_bahan = db.query(models.Bahan).get(bahan_id)

    if not db_bahan:
        # If the Bahan is not found in the database, return a 404 error message
        return {"message": f"Bahan with ID {bahan_id} is not found"}, 404

    # Check if any fields are being updated
    if not any([bahan.nama_bahan, bahan.satuan]):
        return {"message": "At least one field is required to update bahan"}, 400

    # Update the Bahan object with the new data
    update_data = {k: v for k, v in bahan.dict(exclude_unset=True).items()}
    for key, value in update_data.items():
        setattr(db_bahan, key, value)

    # Commit the changes to the database
    db.commit()
    db.refresh(db_bahan)

    # Return success response with the updated Bahan object
    return {"message": f"Bahan with id {bahan_id} is updated", "data": db_bahan}, 200


def delete_bahan(db: Session, bahan_id: int):
    # Query the database for the Bahan with the given ID
    db_bahan = db.query(models.Bahan).filter_by(id=bahan_id).first()

    if not db_bahan:
        # If the Bahan is not found in the database, return a 404 error message
        return {"message": f"Bahan with ID {bahan_id} is not found"}, 404

    # Delete the Bahan object from the database
    db.delete(db_bahan)
    db.commit()

    # Return success response with no content
    return {"message": f"Bahan with id {bahan_id} is deleted successfully"}, 204
