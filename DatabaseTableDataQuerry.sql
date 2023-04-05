INSERT INTO Kategori (nama_kat) VALUES
('Main Course'),
('Dessert');

INSERT INTO Bahan (nama_bahan, satuan) VALUES
('Nasi', 'Piring'),
('Telur', 'Buah'),
('Minyak', 'ml'),
('Bawang Merah', 'Siung'),
('Bawang Putih', 'Siung'),
('Ayam', 'gr'),
('Sayur Caisim', 'Helai'),
('Kecap', 'sdm'),
('Garam', 'sdm'),
('Susu', 'ml'),
('Mentega', 'gr'),
('Tepung Terigu', 'gr'),
('Coklat Bubuk', 'sdm'),
('Gula', 'sdm');

INSERT INTO Resep (nama_resep, kategori_id) VALUES
('Nasi Goreng', 1),
('Ayam Geprek', 1),
('Puding Coklat', 2),
('Es Teh', 2),
('Nasi Ayam', 1);

-- Bahan Resep Nasi Goreng
INSERT INTO Bahan_Resep (resep_id, bahan_id, jumlah) VALUES
(1, 1, 1), -- Nasi (1 piring)
(1, 2, 2), -- Telur (2 buah)
(1, 3, 25), -- Minyak (25 ml)
(1, 4, 2), -- Bawang Merah (2 siung)
(1, 5, 3), -- Bawang Putih (3 siung)
(1, 6, 300), -- Ayam (300 gr)
(1, 7, 2), -- Sayur Caisim (2 helai)
(1, 8, 2), -- Kecap (2 sdm)
(1, 9, 2); -- Garam (2 sdm)

-- Bahan Resep Ayam Geprek
INSERT INTO Bahan_Resep (resep_id, bahan_id, jumlah) VALUES
(2, 6, 200), -- Ayam (200 gr)
(2, 4, 1), -- Bawang Merah (1 siung)
(2, 5, 2), -- Bawang Putih (2 siung)
(2, 9, 1), -- Garam (1 sdm)
(2, 10, 50), -- Susu (50 ml)
(2, 11, 20), -- Mentega (20 gr)
(2, 12, 150); -- Tepung Terigu (150 gr)

-- Bahan Resep Puding Coklat
INSERT INTO Bahan_Resep (resep_id, bahan_id, jumlah) VALUES
(3, 10, 200), -- Susu (200 ml)
(3, 11, 30), -- Mentega (30 gr)
(3, 13, 3), -- Coklat Bubuk (3 sdm)
(3, 14, 5), -- Gula (5 sdm)
(3, 12, 50); -- Tepung Terigu (50 gr)

-- Bahan Resep Es Teh
INSERT INTO Bahan_Resep (resep_id, bahan_id, jumlah) VALUES
(4, 14, 3); -- Gula (3 sdm)

-- Bahan Resep Nasi Ayam
INSERT INTO Bahan_Resep (resep_id, bahan_id, jumlah) VALUES
(5, 1, 1), -- Nasi (1 piring)
(5, 6, 300), -- Ayam (300 gr)
(5, 4, 2), -- Bawang Merah (2 siung)
(5, 5, 3), -- Bawang Putih (3 siung)
(5, 9, 1); -- Garam (1 sdm)