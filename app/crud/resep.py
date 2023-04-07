from sqlalchemy.orm import Session
from models import models, schemas


def create_resep(db: Session, resep: schemas.ResepCreate):
    # Check if required fields are present in the request body
    if not resep.nama_resep or not resep.kategori_id:
        return {"message": "Nama resep and kategori ID are required"}, 400

    # Check if a resep with the same name already exists
    db_resep = db.query(models.Resep).filter(
        models.Resep.nama_resep == resep.nama_resep).first()

    if db_resep:
        # If the resep is not found in the database, return a 404 error message
        return {"message": f"Resep with name {resep.nama_resep} already exists"}, 409

    # Create a new resep object and add it to the database
    db_resep = models.Resep(nama_resep=resep.nama_resep,
                            kategori_id=resep.kategori_id)
    db.add(db_resep)
    db.commit()
    db.refresh(db_resep)

    # Return success response with the newly created resep object
    return {"message": "New resep created", "data": db_resep}, 201


def get_resep(db: Session, resep_id: int):
    # Query the database for the resep with the given ID
    db_resep = db.query(models.Resep).get(resep_id)

    if not db_resep:
        # If the resep is not found in the database, return a 404 error message
        return {"message": f"Resep with ID {resep_id} is not found"}, 404

    # Return success response with the resep object
    return {"message": "Resep found", "data": db_resep}, 200


def get_resep_by_name(db: Session, nama_resep: str):
    # Query the database for the resep with the given name
    db_resep = db.query(models.Resep).filter(
        models.Resep.nama_resep == nama_resep).first()

    if not db_resep:
        # If the resep is not found in the database, return a 404 error message
        return {"message": f"Resep with name {nama_resep} is not found"}, 404

    # Return success response with the resep object
    return {"message": f"Resep with name {nama_resep} is found", "data": db_resep}, 200


def get_all_resep(db: Session, offset: int = 0, page_size: int = 100, nama_resep: str = None, kategori_id: int = None, sort_by: str = "id", sort_order: str = "asc"):
    # Start building the query with the Resep model
    query = db.query(models.Resep)
    total_data = query.count()

    # Apply filters based on optional parameters
    if nama_resep:
        query = query.filter(models.Resep.nama_resep.ilike(f"%{nama_resep}%"))
    if kategori_id:
        query = query.filter(models.Resep.kategori_id == kategori_id)

    # Apply sorting based on optional parameters
    if sort_by:
        column = getattr(models.Resep, sort_by, None)
        if column is not None:
            if sort_order.lower() == "desc":
                column = column.desc()
            query = query.order_by(column)

    # Execute the query with pagination
    db_resep = db_resep.offset(offset).limit(page_size).all()

    # Check if any reseps were found
    if len(db_resep) == 0:
        return {"message": "No resep found"}, 404

    # Return success response with the list of reseps and total count
    return {"message": "All resep retrieved", "total_data": total_data, "data": db_resep}, 200


def update_resep(db: Session, resep_id: int, resep: schemas.ResepUpdate):
    # Query the database for the resep with the given ID
    db_resep = db.query(models.Resep).get(resep_id)

    if not db_resep:
        # If the resep is not found in the database, return a 404 error message
        return {"message": f"Resep with ID {resep_id} is not found"}, 404

    # Check if any fields are being updated
    if not any([resep.nama_resep, resep.kategori_id]):
        return {"message": "At least one field is required to update resep"}, 400

    # Update the resep object with the new data
    update_data = {k: v for k, v in resep.dict(exclude_unset=True).items()}
    for key, value in update_data.items():
        setattr(db_resep, key, value)

    # Commit the changes to the database
    db.commit()
    db.refresh(db_resep)

    # Return success response with the updated resep object
    return {"message": f"Resep with id {resep_id} is updated", "data": db_resep}, 200


def delete_resep(db: Session, resep_id: int):
    # Query the database for the resep with the given ID
    db_resep = db.query(models.Resep).filter_by(id=resep_id).first()

    if not db_resep:
        # If the resep is not found in the database, return a 404 error message
        return {"message": f"Resep with ID {resep_id} is not found"}, 404

    # Delete the resep object from the database
    db.delete(db_resep)
    db.commit()

    # Return success response with no content
    return {"message": f"Resep with id {resep_id} is deleted successfully"}, 204
