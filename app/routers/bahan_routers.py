from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from models import schemas
from crud.bahan import create_bahan, get_bahan, get_bahan_by_name, get_all_bahan, update_bahan, delete_bahan


router = APIRouter()


@router.post("/bahan", status_code=201)
def add_bahan(bahan: schemas.BahanCreate, db: Session = Depends(get_db)):
    return create_bahan(db=db, bahan=bahan)


@router.get("/bahan/{bahan_id}", response_model=schemas.Bahan)
def read_bahan_by_id(bahan_id: int, db: Session = Depends(get_db)):
    return get_bahan(db=db, bahan_id=bahan_id)


@router.get("/bahan", response_model=List[schemas.Bahan])
def read_all_bahan(offset: int = 0, page_size: int = 100, nama_bahan: str = None, sort_by: str = 'id', sort_order: str = "asc", db: Session = Depends(get_db)):
    return get_all_bahan(db=db, offset=offset, page_size=page_size, nama_bahan=nama_bahan, sort_by=sort_by, sort_order=sort_order)


@router.get("/bahan/nama/{nama_bahan}", response_model=schemas.Bahan)
def read_bahan_by_name(nama_bahan: str, db: Session = Depends(get_db)):
    return get_bahan_by_name(db=db, nama_bahan=nama_bahan)


@router.put("/bahan/{bahan_id}", response_model=schemas.Bahan)
def update_existing_bahan(bahan_id: int, bahan: schemas.BahanUpdate, db: Session = Depends(get_db)):
    updated_bahan = update_bahan(db=db, bahan_id=bahan_id, bahan=bahan)
    if not updated_bahan:
        raise HTTPException(
            status_code=404, detail=f"Bahan with ID {bahan_id} not found")
    return updated_bahan


@router.delete("/bahan/{bahan_id}")
def delete_existing_bahan(bahan_id: int, db: Session = Depends(get_db)):
    deleted_bahan = delete_bahan(db=db, bahan_id=bahan_id)
    if not deleted_bahan:
        raise HTTPException(
            status_code=404, detail=f"Bahan with ID {bahan_id} not found")
    return deleted_bahan
