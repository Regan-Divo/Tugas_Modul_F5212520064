from models.buku_model import BukuModel

model = BukuModel()

# 1. Menambah data buku baru ke MySQL Laragon
print("Menambahkan data buku...")
model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2024)
print("Data berhasil disimpan ke Laragon MySQL!")

# 2. Menampilkan seluruh data buku dari MySQL Laragon
print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"- [ID: {buku['id_buku']}] {buku['judul']} | {buku['penulis']} ({buku['tahun_terbit']})")