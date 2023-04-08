from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.schemas import ResepCreate, ResepUpdate
from app.crud.resep import create_resep, get_resep, get_all_resep, update_resep, delete_resep

router = APIRouter()


@router.post("/resep", status_code=201)
def create_new_resep(resep: ResepCreate, db: Session = Depends(get_db)):
    """
    Create a new resep object in the database.
    """
    return create_resep(db=db, resep=resep)


@router.get("/resep/{resep_id}", status_code=200)
def get_single_resep(resep_id: int, db: Session = Depends(get_db)):
    """
    Get a single resep object from the database by its ID.
    """
    return get_resep(db=db, resep_id=resep_id)


@router.get("/resep", status_code=200)
def get_all_reseps(offset: int = 0, page_size: int = 100, nama_resep: str = None, kategori_id: int = None, sort_by: str = "id", sort_order: str = "asc", db: Session = Depends(get_db)):
    """
    Get a list of all resep objects from the database, with optional filtering and sorting.
    """
    return get_all_resep(db=db, offset=offset, page_size=page_size, nama_resep=nama_resep, kategori_id=kategori_id, sort_by=sort_by, sort_order=sort_order)


@router.put("/resep/{resep_id}", status_code=200)
def update_existing_resep(resep_id: int, resep: ResepUpdate, db: Session = Depends(get_db)):
    """
    Update an existing resep object in the database by its ID.
    """
    return update_resep(db=db, resep_id=resep_id, resep=resep)


@router.delete("/resep/{resep_id}", status_code=204)
def delete_existing_resep(resep_id: int, db: Session = Depends(get_db)):
    """
    Delete an existing resep object from the database by its ID.
    """
    return delete_resep(db=db, resep_id=resep_id)
