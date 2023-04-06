from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.database import Base

class Kategori(Base):
    __tablename__ = "kategori"

    id = Column(Integer, primary_key=True, index=True)
    nama_kat = Column(String(128), index=True)

    resep = relationship("Resep", back_populates="kategori")

class Bahan(Base):
    __tablename__ = "bahan"

    id = Column(Integer, primary_key=True, index=True)
    nama_bahan = Column(String(128), index=True)
    satuan = Column(String(64))

class Resep(Base):
    __tablename__ = "resep"

    id = Column(Integer, primary_key=True, index=True)
    nama_resep = Column(String(256), index=True)
    kategori_id = Column(Integer, ForeignKey("kategori.id"))

    kategori = relationship("Kategori", back_populates="resep")
    bahan = relationship("Bahan", secondary="bahan_resep")

class Bahan_Resep(Base):
    __tablename__ = "bahan_resep"

    resep_id = Column(Integer, ForeignKey("resep.id"), primary_key=True)
    bahan_id = Column(Integer, ForeignKey("bahan.id"), primary_key=True)
    jumlah = Column(Float)

    bahan = relationship("Bahan", backref="resep_detail")
    resep = relationship("Resep", backref="bahan_detail")
