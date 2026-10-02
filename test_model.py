from models.buku_model import BukuModel

model = BukuModel()

# 1. Menguji fungsi Create (menambah buku baru)
print("\n=== Menambahkan data buku ===")
model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)
print("Data berhasil disimpan ke Laragon MySQL!")

# 2. Menguji fungsi Read (menampilkan data)
print("\n=== Daftar Buku ===")
data_buku = model.get_all_buku()

for buku in data_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} | {buku['penulis']} | {buku['tahun_terbit']}")