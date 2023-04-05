CREATE TABLE Kategori (
    id SERIAL PRIMARY KEY,
    nama_kat VARCHAR(128) NOT NULL
);

CREATE TABLE Bahan (
    id SERIAL PRIMARY KEY,
    nama_bahan VARCHAR(128) NOT NULL,
    satuan VARCHAR(64) NOT NULL
);

CREATE TABLE Resep (
    id SERIAL PRIMARY KEY,
    nama_resep VARCHAR(256) NOT NULL,
    kategori_id INT NOT NULL REFERENCES Kategori(id) ON DELETE RESTRICT
);

CREATE TABLE Bahan_Resep (
    resep_id INT NOT NULL REFERENCES Resep(id) ON DELETE CASCADE,
    bahan_id INT NOT NULL REFERENCES Bahan(id) ON DELETE RESTRICT,
    jumlah DECIMAL(10,4) NOT NULL,
    PRIMARY KEY (resep_id, bahan_id)
);