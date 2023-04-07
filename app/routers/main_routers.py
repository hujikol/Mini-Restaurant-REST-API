from fastapi import APIRouter
from . import kategori_routers, resep_routers,  bahan_routers, bahan_resep_routers

router = APIRouter()


router.include_router(kategori_routers, prefix="/kategori")
router.include_router(resep_routers, prefix="/resep")
router.include_router(bahan_routers, prefix="/bahan")
router.include_router(bahan_resep_routers, prefix="/bahan_resep")
