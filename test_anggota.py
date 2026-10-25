from models.anggota_model import AnggotaModel

model = AnggotaModel()

# 1. Menguji fungsi Create
print("\n=== Menambahkan data anggota ===")
model.create_anggota("Kiki Rahman", "Palu")
print("Data berhasil disimpan ke Laragon MySQL!")

# 2. Menguji fungsi Read
print("\n=== Daftar Anggota ===")
for anggota in model.get_all_anggota():
    print(f"[{anggota['id_anggota']}] {anggota['nama']} | {anggota['alamat']}")