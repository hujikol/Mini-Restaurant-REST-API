from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.models import schemas
from app.crud.bahanResep import create_bahan_resep, delete_bahan_resep, get_all_bahan_resep, get_bahan_by_resep_id, get_bahan_resep, get_resep_by_bahan_ids, update_bahan_resep

router = APIRouter()


@router.post("/bahan_resep/", response_model=schemas.Bahan_Resep)
def create_bahan_resep(bahan_resep: schemas.Bahan_ResepCreate, db: Session = Depends(get_db)):
    return create_bahan_resep(db=db, bahan_resep=bahan_resep)


@router.get("/bahan_resep/{resep_id}/{bahan_id}", response_model=schemas.Bahan_Resep)
def read_bahan_resep(resep_id: int, bahan_id: int, db: Session = Depends(get_db)):
    db_bahan_resep = get_bahan_resep(
        db=db, resep_id=resep_id, bahan_id=bahan_id)
    if db_bahan_resep is None:
        raise HTTPException(status_code=404, detail="Bahan not found")
    return db_bahan_resep


@router.get("/bahan_resep/resep/{resep_id}", response_model=List[schemas.Bahan_Resep])
def read_bahan_by_resep_id(resep_id: int, offset: int = 0, page_size: int = 100, db: Session = Depends(get_db)):
    db_bahan_resep = get_bahan_by_resep_id(
        db=db, resep_id=resep_id, offset=offset, page_size=page_size)
    if not db_bahan_resep:
        raise HTTPException(status_code=404, detail="Bahan not found")
    return db_bahan_resep


@router.get("/bahan_resep/bahan/", response_model=List[int])
def read_resep_by_bahan_ids(bahan_ids: List[int], offset: int = 0, page_size: int = 100, db: Session = Depends(get_db)):
    resep_ids = get_resep_by_bahan_ids(
        db=db, bahan_ids=bahan_ids, offset=offset, page_size=page_size)
    if not resep_ids:
        raise HTTPException(status_code=404, detail="Resep not found")
    return resep_ids


@router.get("/bahan_resep/", response_model=List[schemas.Bahan_Resep])
def read_all_bahan_resep(offset: int = 0, page_size: int = 100, db: Session = Depends(get_db)):
    db_bahan_resep = get_all_bahan_resep(
        db=db, offset=offset, page_size=page_size)
    return db_bahan_resep


@router.put("/bahan_resep/{resep_id}/{bahan_id}", response_model=schemas.Bahan_Resep)
def update_existing_bahan_resep(resep_id: int, bahan_id: int, bahan: schemas.Bahan_ResepUpdate, db: Session = Depends(get_db)):
    db_bahan_resep = update_bahan_resep(
        db=db, resep_id=resep_id, bahan_id=bahan_id, bahan=bahan)
    if db_bahan_resep is None:
        raise HTTPException(status_code=404, detail="Bahan not found")
    return db_bahan_resep


@router.delete("/bahan_resep/{resep_id}/{bahan_id}")
def delete_existing_bahan_resep(resep_id: int, bahan_id: int, db: Session = Depends(get_db)):
    db_bahan_resep = delete_bahan_resep(
        db=db, resep_id=resep_id, bahan_id=bahan_id)
    if db_bahan_resep is None:
        raise HTTPException(status_code=404, detail="Bahan not found")
    return {"message": f"Bahan with id {bahan_id} for resep id {resep_id} is deleted"}
