from sqlalchemy.orm import Session

from app.models import models, schemas


def create_kategori(db: Session, kategori: schemas.KategoriCreate):
    # Check if required fields are present in the request body
    if not kategori.nama_kategori or not kategori.kategori_id:
        return {"message": "Nama kategori and kategori ID are required"}, 400

    # Check if the category already exists in the database
    db_kategori = db.query(models.Kategori).filter(
        models.Kategori.nama_kat == kategori.nama_kat).first()

    if db_kategori:
        # If the category already exists, return an error message with a 409 status code
        return {"message": f"Kategori with name {kategori.nama_kat} already exists"}, 409

    # Create a new category object and add it to the database
    db_kategori = models.Kategori(nama_kat=kategori.nama_kat)
    db.add(db_kategori)
    db.commit()
    db.refresh(db_kategori)

    # Return a success message with the newly created category and a 201 status code
    return {"message": "New kategori created", "kategori": db_kategori}, 201


def get_kategori(db: Session, kategori_id: int):
    # Get a category from the database based on its ID
    db_kategori = db.query(models.Kategori).filter(
        models.Kategori.id == kategori_id).first()

    if not db_kategori:
        # If the category is not found, return an error message with a 404 status code
        return {"message": f"Kategori with id {kategori_id} is not found"}, 404

    # Return a success message with the found category and a 200 status code
    return {"message": "Kategori found", "data": db_kategori}, 200


def get_kategori_by_name(db: Session, nama_kat: str):
    # Get a category from the database based on its name
    db_kategori = db.query(models.Kategori).filter(
        models.Kategori.nama_kat == nama_kat).first()

    if not db_kategori:
        # If the category is not found, return an error message with a 404 status code
        return {"message": f"Kategori with name {nama_kat} is not found"}, 404

    # Return a success message with the found category and a 200 status code
    return {"message": "Kategori found", "data": db_kategori}, 200


def get_all_kategori(db: Session, offset: int = 0, page_size: int = 100):
    # Get all categories from the database with pagination
    db_kategori = db.query(models.Kategori).offset(
        offset).limit(page_size).all()

    # Get the total number of categories in the database
    total_data = db.query(models.Kategori).count()

    # Check if any reseps were found
    if total_data == 0:
        return {"message": "No kategori found"}, 404

    # Return a success message with all categories and a 200 status code
    return {"message": "All kategori returned", "total_data": total_data, "data": db_kategori}, 200


def update_kategori(db: Session, kategori_id: int, kategori: schemas.KategoriUpdate):
    # Get a category from the database based on its ID
    db_kategori = db.query(models.Kategori).filter_by(id=kategori_id).first()

    if not db_kategori:
        # If the category is not found, return an error message with a 404 status code
        return {"message": f"Kategori with id {kategori_id} is not found"}, 404

    if not any([kategori.nama_kat]):
        # If no fields are provided to update, return an error message with a 400 status code
        return {"message": "At least one field is required to update kategori"}, 400

    # Update the category object with the provided data
    update_data = {k: v for k, v in kategori.dict(exclude_unset=True).items()}
    for key, value in update_data.items():
        setattr(db_kategori, key, value)

    db.commit()
    db.refresh(db_kategori)

    # Return a success message with the updated category and a 200 status code
    return {"message": f"Kategori with id {kategori_id} is updated", "data": db_kategori}, 200


def delete_kategori(db: Session, kategori_id: int):
    # Get a category from the database based on its ID
    db_kategori = get_kategori(db, kategori_id)["data"]

    if not db_kategori:
        # If the category is not found, return an error message with a 404 status code
        return {"message": f"Kategori with id {kategori_id} is not found"}, 404

    # Delete the category object from the database
    db.delete(db_kategori)
    db.commit()

    # Return a success message with the deleted category and a 200 status code
    return {"message": f"Kategori with id {kategori_id} is deleted"}, 204
