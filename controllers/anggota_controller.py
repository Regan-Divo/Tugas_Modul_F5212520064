import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()

        self.view.btn_simpan.configure(command=self.simpan_anggota)
        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)
        data_anggota = self.model.get_all_anggota()
        for anggota in data_anggota:
            self.view.tabel.insert("", "end", values=(anggota['id_anggota'], anggota['nama'], anggota['alamat']))

    def simpan_anggota(self):
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()
        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom anggota harus diisi!")
            return
        if self.model.create_anggota(nama, alamat):
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.muat_data_tabel()

    def run(self):
        self.view.mainloop()