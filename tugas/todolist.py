def konversi_ke_huruf(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 65:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"

def main():
    print("=== Program Hitung Rata-rata Nilai Mahasiswa ===")
    
    nama = input("Masukkan nama mahasiswa: ")
    
    try:
        jumlah_matkul = int(input("Berapa jumlah mata kuliah yang ingin dimasukkan? "))
    except ValueError:
        print("Input harus berupa angka!")
        return
    
    if jumlah_matkul <= 0:
        print("Jumlah mata kuliah harus lebih dari 0.")
        return
    
    data_nilai = []
    
    for i in range(1, jumlah_matkul + 1):
        while True:
            nama_matkul = input(f"\nNama mata kuliah ke-{i}: ")
            try:
                nilai = float(input(f"Nilai untuk {nama_matkul} (0-100): "))
                if 0 <= nilai <= 100:
                    data_nilai.append({"matkul": nama_matkul, "nilai": nilai})
                    break
                else:
                    print("Nilai harus antara 0 dan 100. Coba lagi.")
            except ValueError:
                print("Nilai harus berupa angka. Coba lagi.")
    
    total_nilai = sum(item["nilai"] for item in data_nilai)
    rata_rata = total_nilai / jumlah_matkul
    huruf = konversi_ke_huruf(rata_rata)
    
    print("\n" + "=" * 40)
    print(f"Hasil Rekap Nilai untuk {nama}")
    print("=" * 40)
    for item in data_nilai:
        print(f"{item['matkul']:<20}: {item['nilai']:.1f}  ({konversi_ke_huruf(item['nilai'])})")
    print("-" * 40)
    print(f"Rata-rata Nilai   : {rata_rata:.2f}")
    print(f"Grade Akhir       : {huruf}")
    print("=" * 40)

if __name__ == "__main__":
    main()