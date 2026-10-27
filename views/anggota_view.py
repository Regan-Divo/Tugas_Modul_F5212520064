import customtkinter as ctk
from tkinter import ttk

class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Sistem Manajemen Perpustakaan - Anggota")
        self.geometry("850x500")
        self.resizable(False, False)
        
        # Frame Form Kiri
        self.frame_form = ctk.CTkFrame(self, width=320)
        self.frame_form.pack(side="left", fill="y", padx=10, pady=10)
        
        self.label_title = ctk.CTkLabel(self.frame_form, text="Form Data Anggota", font=("Arial", 16, "bold"))
        self.label_title.pack(pady=20)
        
        self.entry_nama = ctk.CTkEntry(self.frame_form, placeholder_text="Masukkan Nama Anggota", width=260)
        self.entry_nama.pack(pady=10)
        
        self.entry_alamat = ctk.CTkEntry(self.frame_form, placeholder_text="Masukkan Alamat Anggota", width=260)
        self.entry_alamat.pack(pady=10)
        
        self.btn_simpan = ctk.CTkButton(self.frame_form, text="Simpan Data", fg_color="green")
        self.btn_simpan.pack(pady=20)
        
        # Frame Tabel Kanan
        self.frame_tabel = ctk.CTkFrame(self)
        self.frame_tabel.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        
        self.label_tabel = ctk.CTkLabel(self.frame_tabel, text="Daftar Anggota", font=("Arial", 16, "bold"))
        self.label_tabel.pack(pady=20)
        
        # Tabel / Treeview
        columns = ("ID", "Nama Anggota", "Alamat")
        self.tabel = ttk.Treeview(self.frame_tabel, columns=columns, show="headings")
        
        for col in columns:
            self.tabel.heading(col, text=col)
            self.tabel.column(col, width=140, anchor="center")
            
        self.tabel.pack(fill="both", expand=True, padx=10, pady=10)