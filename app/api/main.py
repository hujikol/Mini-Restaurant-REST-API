from fastapi import APIRouter
from app.api import bahan, bahan_resep, kategori, resep

router = APIRouter()


router.include_router(kategori, prefix="/kategori")
router.include_router(resep, prefix="/resep")
router.include_router(bahan, prefix="/bahan")
router.include_router(bahan_resep, prefix="/bahan_resep")
