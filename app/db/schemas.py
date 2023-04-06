from typing import List
from pydantic import BaseModel

# Model untuk Kategori
class KategoriBase(BaseModel):
    nama_kat: str

class KategoriCreate(KategoriBase):
    pass

class KategoriUpdate(KategoriBase):
    pass

class Kategori(KategoriBase):
    id: int

    class Config:
        orm_mode = True

class BahanBase(BaseModel):
    nama_bahan: str
    satuan: str

class BahanCreate(BahanBase):
    pass

class BahanUpdate(BahanBase):
    pass

class Bahan(BahanBase):
    id: int

    class Config:
        orm_mode = True

class ResepBase(BaseModel):
    nama_resep: str
    kategori_id: int

class ResepCreate(ResepBase):
    pass

class ResepUpdate(ResepBase):
    pass

class Resep(ResepBase):
    id: int
    kategori: Kategori
    bahan: List[Bahan] = []

    class Config:
        orm_mode = True

class Bahan_ResepBase(BaseModel):
    resep_id: int
    bahan_id: int
    jumlah: float

class Bahan_ResepCreate(Bahan_ResepBase):
    pass

class Bahan_ResepUpdate(Bahan_ResepBase):
    pass

class Bahan_Resep(Bahan_ResepBase):
    bahan: Bahan
    resep: Resep

    class Config:
        orm_mode = True
