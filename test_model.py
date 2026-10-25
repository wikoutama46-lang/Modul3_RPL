from models.buku_model import BukuModel

model = BukuModel()

# 1. Menguji fungsi Create (dikomentari agar data tidak dobel)
# print("\n=== Menambahkan data buku ===")
# model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)
# print("Data berhasil disimpan ke Laragon MySQL!")

# 2. Menguji fungsi Read (sebelum update & delete)
print("\n=== Daftar Buku (Sebelum) ===")
for buku in model.get_all_buku():
    print(f"[{buku['id_buku']}] {buku['judul']} | {buku['penulis']} | {buku['tahun_terbit']}")

# 3. Menguji fungsi Update
print("\n=== Mengubah data buku id 14 ===")
model.update_buku(14, "Pemrograman Python MVC (Revisi)", "Guido van Rossum", 2024)
print("Data berhasil diupdate!")

# 4. Menguji fungsi Delete
print("\n=== Menghapus data buku id 15 ===")
model.delete_buku(15)
print("Data berhasil dihapus!")

# 5. Menguji fungsi Read (sesudah update & delete)
print("\n=== Daftar Buku (Sesudah) ===")
for buku in model.get_all_buku():
    print(f"[{buku['id_buku']}] {buku['judul']} | {buku['penulis']} | {buku['tahun_terbit']}")