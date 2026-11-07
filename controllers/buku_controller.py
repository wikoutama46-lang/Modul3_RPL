import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = BukuModel()
        self.view = BukuView()

        # Binding (mengikat) tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_perbarui.configure(command=self.perbarui_data)
        self.view.btn_hapus.configure(command=self.hapus_data)

        # Menyimpan id_buku dari baris tabel yang diklik pengguna
        self.id_terpilih = None
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_data)

        # Memuat data ke tabel saat aplikasi pertama kali dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan isi tabel di View terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari Model (database)
        data_buku = self.model.get_all_buku()

        # Memasukkan data baru ke dalam tabel View
        for buku in data_buku:
            self.view.tabel.insert(
                "", "end",
                values=(
                    buku['id_buku'],
                    buku['judul'],
                    buku['penulis'],
                    buku['tahun_terbit']
                )
            )
    def simpan_data(self):
        # Mengambil teks dari kotak input di View
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        # Validasi Form Kosong
        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return
        # Mengirim data ke Model untuk disimpan
        berhasil = self.model.create_buku(judul, penulis, tahun)
        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil disimpan!"
            )
            # Bersihkan form input
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            # Muat ulang tabel agar data terbaru muncul
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Terjadi kesalahan saat menyimpan data."
            )
    def bersihkan_form(self):
        # Kosongkan form input dan lepas pilihan baris
        self.view.entry_judul.delete(0, 'end')
        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_tahun.delete(0, 'end')
        self.id_terpilih = None

    def pilih_data(self, event=None):
        # Dipanggil saat pengguna mengklik baris tabel
        pilihan = self.view.tabel.selection()
        if not pilihan:
            return
        nilai = self.view.tabel.item(pilihan[0], "values")

        # Ambil id_buku dari baris yang diklik, lalu isi form dengan datanya
        self.bersihkan_form()
        self.id_terpilih = nilai[0]
        self.view.entry_judul.insert(0, nilai[1])
        self.view.entry_penulis.insert(0, nilai[2])
        self.view.entry_tahun.insert(0, nilai[3])

    def perbarui_data(self):
        # Pastikan ada baris yang dipilih di tabel
        if self.id_terpilih is None:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku pada tabel terlebih dahulu!"
            )
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        # Validasi Form Kosong
        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        # Teruskan id_buku beserta data baru ke fungsi update di Model
        berhasil = self.model.update_buku(self.id_terpilih, judul, penulis, tahun)
        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil diperbarui!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Terjadi kesalahan saat memperbarui data."
            )

    def hapus_data(self):
        # Pastikan ada baris yang dipilih di tabel
        if self.id_terpilih is None:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku pada tabel terlebih dahulu!"
            )
            return

        # Minta konfirmasi sebelum data dihapus
        yakin = messagebox.askyesno(
            "Konfirmasi",
            "Yakin ingin menghapus data buku ini?"
        )
        if not yakin:
            return

        # Teruskan id_buku ke fungsi hapus di Model
        berhasil = self.model.delete_buku(self.id_terpilih)
        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil dihapus!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Terjadi kesalahan saat menghapus data."
            )

    # Fungsi untuk menjalankan aplikasi
    def run(self):
        self.view.mainloop()