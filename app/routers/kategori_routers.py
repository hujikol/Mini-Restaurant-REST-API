from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.kategori import get_all_kategori, update_kategori

from crud.kategori import create_kategori, get_kategori, get_kategori_by_name, delete_kategori
from models import schemas
from db.database import get_db

router = APIRouter()


@router.post("/kategori", status_code=201)
def create_kategori(kategori: schemas.KategoriCreate, db: Session = Depends(get_db)):
    """
    Create a new category.
    """
    db_kategori = create_kategori(db, kategori)
    return db_kategori


@router.get("/kategori/{kategori_id}", response_model=schemas.Kategori)
def read_kategori(kategori_id: int, db: Session = Depends(get_db)):
    """
    Get a category by ID.
    """
    db_kategori = get_kategori(db, kategori_id=kategori_id)
    if db_kategori is None:
        raise HTTPException(status_code=404, detail="Kategori not found")
    return db_kategori


@router.get("/kategori/by_name/{nama_kat}", response_model=schemas.Kategori)
def read_kategori_by_name(nama_kat: str, db: Session = Depends(get_db)):
    """
    Get a category by name.
    """
    db_kategori = get_kategori_by_name(db, nama_kat=nama_kat)
    if db_kategori is None:
        raise HTTPException(status_code=404, detail="Kategori not found")
    return db_kategori


@router.get("/kategori", response_model=schemas.KategoriList)
def read_all_kategori(offset: int = 0, page_size: int = 100, db: Session = Depends(get_db)):
    """
    Get all categories with pagination.
    """
    db_kategori = get_all_kategori(db, offset=offset, page_size=page_size)
    return db_kategori


@router.put("/kategori/{kategori_id}", response_model=schemas.Kategori)
def update_existing_kategori(kategori_id: int, kategori: schemas.KategoriUpdate, db: Session = Depends(get_db)):
    """
    Update a category by ID.
    """
    db_kategori = update_kategori(
        db, kategori_id=kategori_id, kategori=kategori)
    if db_kategori is None:
        raise HTTPException(status_code=404, detail="Kategori not found")
    return db_kategori


@router.delete("/kategori/{kategori_id}", status_code=204)
def delete_existing_kategori(kategori_id: int, db: Session = Depends(get_db)):
    """
    Delete a category by ID.
    """
    db_kategori = delete_kategori(db, kategori_id=kategori_id)
    if db_kategori is None:
        raise HTTPException(status_code=404, detail="Kategori not found")
    return None
