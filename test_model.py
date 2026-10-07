from models.buku_model import BukuModel
from models.anggota_model import AnggotaModel

buku_model = BukuModel()
anggota_model = AnggotaModel()

print("\n==========================================")
print("PENGUJIAN BUKU MODEL (UPDATE & DELETE)")
print("==========================================")
# 1A. Menguji Update (Memastikan ID 6 adalah Nama & NIM kamu)
buku_model.update_buku(6, "Tugas Modul 4 - F5212520064", "Regan Musholli D R", 2026)
print("[+] Data buku ID 6 berhasil di-update.")

# 1B. Menguji Delete (Menghapus duplikasi ID 9 dan 10 jika masih ada)
buku_model.delete_buku(9)
buku_model.delete_buku(10)
print("[+] Data buku ID 9 dan 10 berhasil dihapus.\n")

print("--- Daftar Buku Terbaru ---")
daftar_buku = buku_model.get_all_buku()
if not daftar_buku:
    print("Data buku kosong.")
else:
    for buku in daftar_buku:
        print(f"ID: {buku['id_buku']} | Judul: {buku['judul']} | Penulis: {buku['penulis']}")


print("\n==========================================")
print("PENGUJIAN ANGGOTA MODEL (CREATE & READ)")
print("==========================================")

# FITUR ANTI-DUPLIKAT: Reset/Bersihkan tabel anggota terlebih dahulu
if anggota_model.conn:
    cursor = anggota_model.conn.cursor()
    # 1. Matikan pengecekan foreign key sementara
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;") 
    # 2. Kosongkan tabel anggota dan reset ID ke 1
    cursor.execute("TRUNCATE TABLE anggota;") 
    # 3. Nyalakan kembali pengecekan foreign key
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;") 
    
    anggota_model.conn.commit()
    cursor.close()

# 2A. Menguji Create Anggota
anggota_model.create_anggota("Regan Musholli D R", "Palu, Sulawesi Tengah")
anggota_model.create_anggota("Budi Santoso", "Jl. Merdeka No. 45")
print("[+] Data anggota baru berhasil disimpan ke database.\n")

# 2B. Menguji Read Anggota
print("--- Daftar Seluruh Anggota ---")
daftar_anggota = anggota_model.get_all_anggota()
if not daftar_anggota:
    print("Data anggota kosong.")
else:
    for anggota in daftar_anggota:
        print(f"ID: {anggota['id_anggota']} | Nama: {anggota['nama']} | Alamat: {anggota['alamat']}")
print("==========================================\n")