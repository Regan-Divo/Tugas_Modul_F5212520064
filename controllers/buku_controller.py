import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self):
        self.model = BukuModel()
        self.view = BukuView()

        # Binding tombol-tombol aksi
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.perbarui_data)
        self.view.btn_hapus.configure(command=self.hapus_data)

        # Event klik baris tabel untuk memilih data
        self.view.tabel.bind("<ButtonRelease-1>", self.pilih_tabel)

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)
        data_buku = self.model.get_all_buku()
        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))

    def pilih_tabel(self, event):
        # Mengisi form otomatis saat baris tabel diklik
        selected_item = self.view.tabel.focus()
        if selected_item:
            values = self.view.tabel.item(selected_item, 'values')
            self.selected_id = values[0]
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_judul.insert(0, values[1])
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_penulis.insert(0, values[2])
            self.view.entry_tahun.delete(0, 'end')
            self.view.entry_tahun.insert(0, values[3])

    def simpan_data(self):
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()
        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return
        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.muat_data_tabel()

    def perbarui_data(self):
        if hasattr(self, 'selected_id'):
            judul = self.view.entry_judul.get()
            penulis = self.view.entry_penulis.get()
            tahun = self.view.entry_tahun.get()
            success = self.model.update_buku(self.selected_id, judul, penulis, tahun)
            if success:
                messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
                self.muat_data_tabel()
        else:
            messagebox.showwarning("Peringatan", "Pilih data pada tabel yang ingin diubah!")

    def hapus_data(self):
        if hasattr(self, 'selected_id'):
            confirm = messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus data ini?")
            if confirm:
                success = self.model.delete_buku(self.selected_id)
                if success:
                    messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                    self.muat_data_tabel()
        else:
            messagebox.showwarning("Peringatan", "Pilih data pada tabel yang ingin dihapus!")

    def run(self):
        self.view.mainloop()