import networkx as nx
import matplotlib.pyplot as plt

print('-' * 10, 'SIGMA (Sistem Manajamen Grup Mahasiswa & Apresiasi Beasiswa)', '-' * 10)
print('-' * 28, 'PROJECT REGAN', '-' * 36)
print('-' * 32, 'F5212520064', '-' * 38, '\n')

# Data Mahasiswa
data_mahasiswa = [
    {'nim': '23001', 'nama': 'Lilbah', 'ipk': 3.90, 'prodi': 'Hukum', 'semester': 4},
    {'nim': '23002', 'nama': 'KinkOwi', 'ipk': 3.50, 'prodi': 'Sistem Informasi', 'semester': 6},
    {'nim': '23003', 'nama': 'Sawit', 'ipk': 3.80, 'prodi': 'Kedokteran', 'semester': 2},
    {'nim': '23004', 'nama': 'Herlambang', 'ipk': 3.95, 'prodi': 'Teknik Informatika', 'semester': 9},
    {'nim': '23005', 'nama': 'Anso', 'ipk': 3.75, 'prodi': 'Sistem Informasi', 'semester': 5}
]

# Modul 1: Array
def lihat_statistik():
    print("\nMenu Statistik Performa Akademik")
    if not data_mahasiswa:
        print("Tidak ada data mahasiswa di dalam sistem.")
        return

    print("Data Mentah Mahasiswa")
    for data in data_mahasiswa:
        print(f"NIM: {data['nim']} | Nama: {data['nama']} | IPK: {data['ipk']} | Semester: {data['semester']} | Prodi: {data['prodi']}")
    
    list_ipk = [data['ipk'] for data in data_mahasiswa]
    total_mahasiswa = len(list_ipk)
    ipk_tertinggi = max(list_ipk)
    ipk_terendah = min(list_ipk)
    rata_rata_angkatan = sum(list_ipk) / total_mahasiswa
    
    print("\nRingkasan Statistik Angkatan")
    print(f"Total Mahasiswa : {total_mahasiswa} orang")
    print(f"IPK Tertinggi   : {ipk_tertinggi:.2f}")
    print(f"IPK Terendah    : {ipk_terendah:.2f}")
    print(f"Rata-rata IPK   : {rata_rata_angkatan:.2f}")

# Modul 2: Stack & Queue
class LayananBeasiswa:
    def __init__(self, kapasitas=5):
        self.antrean = []
        self.notifikasi = []
        self.kapasitas = kapasitas

    def tambah_antrean(self, nim_target, data_utama):
        if len(self.antrean) >= self.kapasitas:
            print("Antrean loket sedang penuh.")
            return

        mhs_ditemukan = None
        for mhs in data_utama:
            if mhs['nim'] == nim_target:
                mhs_ditemukan = mhs
                break
        
        if mhs_ditemukan:
            self.antrean.append(mhs_ditemukan)
            print(f"Mahasiswa {mhs_ditemukan['nama']} masuk antrean loket.")
            self.tambah_notif(f"Antrean masuk: {mhs_ditemukan['nama']} (NIM: {nim_target})")
        else:
            print("Gagal: NIM tidak terdaftar di database sistem.")

    def proses_layanan(self):
        if self.antrean:
            siapa = self.antrean.pop(0)
            print(f"Selesai melayani pendaftaran: {siapa['nama']}")
        else:
            print("Tidak ada antrean.")

    def tambah_notif(self, pesan):
        self.notifikasi.append(pesan)

    def lihat_notif(self):
        print("\nRiwayat Notifikasi Terbaru:")
        if not self.notifikasi:
            print("Belum ada pesan.")
        else:
            for i in range(len(self.notifikasi)-1, -1, -1):
                print(f"- {self.notifikasi[i]}")

# Modul 3: Sorting & Searching
def quick_sort_ipk(data):
    if len(data) <= 1:
        return data
    pivot  = data[len(data) // 2]
    left   = [x for x in data if x["ipk"] > pivot["ipk"]]
    middle = [x for x in data if x["ipk"] == pivot["ipk"]]
    right  = [x for x in data if x["ipk"] < pivot["ipk"]]
    return quick_sort_ipk(left) + middle + quick_sort_ipk(right)

def quick_sort_nim(data):
    if len(data) <= 1:
        return data
    pivot  = data[len(data) // 2]
    left   = [x for x in data if x["nim"] < pivot["nim"]]
    middle = [x for x in data if x["nim"] == pivot["nim"]]
    right  = [x for x in data if x["nim"] > pivot["nim"]]
    return quick_sort_nim(left) + middle + quick_sort_nim(right)

def binary_search(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid]["nim"] == target:
            return mid
        elif data[mid]["nim"] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def linear_search(data, target):
    hasil = []
    for mahasiswa in data:
        if target.lower() in mahasiswa["nama"].lower():
            hasil.append(mahasiswa)
    return hasil

def tampilkan_ranking(data):
    print("\nRanking Beasiswa Berdasarkan IPK (Maksimal Semester 8)")
    data_layak = [mhs for mhs in data if mhs['semester'] <= 8]
    hasil_sort = quick_sort_ipk(data_layak)
    print(f"Total Mahasiswa Memenuhi Syarat: {len(hasil_sort)}\n")

    for i in range(len(hasil_sort)):
        print(f"Ranking {i + 1}")
        print(f"Nama     : {hasil_sort[i]['nama']}")
        print(f"NIM      : {hasil_sort[i]['nim']}")
        print(f"Semester : {hasil_sort[i]['semester']}")
        print(f"IPK      : {hasil_sort[i]['ipk']}\n")

def cari_mahasiswa(data):
    print("\nMenu Pencarian Mahasiswa")
    print("1. Cari berdasarkan NIM")
    print("2. Cari berdasarkan Nama")
    pilihan = input("Pilih menu pencarian: ")

    if pilihan == "1":
        data_urut = quick_sort_nim(data)
        nim       = input("Masukkan NIM mahasiswa: ")
        hasil     = binary_search(data_urut, nim)

        if hasil != -1:
            print("\nData Mahasiswa Ditemukan")
            print(f"Nama     : {data_urut[hasil]['nama']}")
            print(f"NIM      : {data_urut[hasil]['nim']}")
            print(f"Semester : {data_urut[hasil]['semester']}")
            print(f"IPK      : {data_urut[hasil]['ipk']}")
        else:
            print("Mahasiswa tidak ditemukan")

    elif pilihan == "2":
        nama  = input("Masukkan nama mahasiswa (bisa sebagian nama): ")
        hasil = linear_search(data, nama)

        if len(hasil) > 0:
            print("\nData Mahasiswa Ditemukan")
            for mahasiswa in hasil:
                print(f"Nama     : {mahasiswa['nama']}")
                print(f"NIM      : {mahasiswa['nim']}")
                print(f"Semester : {mahasiswa['semester']}")
                print(f"IPK      : {mahasiswa['ipk']}\n")
        else:
            print("Mahasiswa tidak ditemukan")
    else:
        print("Pilihan pencarian tidak valid")

# Modul 4: Tree 
class NodeTree:
    def __init__(self, info):
        self.info = info
        self.anak = []
        self.induk = None

    def tambah_anak(self, child):
        child.induk = self
        self.anak.append(child)

    def level(self):
        tingkat = 0
        p = self.induk
        while p:
            tingkat += 1
            p = p.induk
        return tingkat

    def tampilkan(self):
        jarak = '    ' * self.level()
        garis = jarak + "|-- " if self.induk else ""
        print(garis + self.info)
        for child in self.anak:
            child.tampilkan()

def buat_pohon_beasiswa(data_input):
    root = NodeTree("Program Beasiswa SIGMA")
    sangat_layak = NodeTree("Sangat Layak (IPK >= 3.8)")
    layak = NodeTree("Layak (3.5 - 3.79)")
    pertimbangan = NodeTree("Pertimbangan (< 3.5)")
    tidak_layak = NodeTree("Tidak Layak (Semester > 8)")
    
    root.tambah_anak(sangat_layak)
    root.tambah_anak(layak)
    root.tambah_anak(pertimbangan)
    root.tambah_anak(tidak_layak)

    for m in data_input:
        mhs_node = NodeTree(f"{m['nama']} (Sem: {m['semester']}, IPK: {m['ipk']})")
        if m['semester'] > 8:
            tidak_layak.tambah_anak(mhs_node)
        elif m['ipk'] >= 3.8:
            sangat_layak.tambah_anak(mhs_node)
        elif m['ipk'] >= 3.5:
            layak.tambah_anak(mhs_node)
        else:
            pertimbangan.tambah_anak(mhs_node)
            
    return root

# Modul 5: Graph 
class GrafSIGMA:
    def __init__(self):
        self.G = nx.DiGraph()

    def sinkronisasi(self, data):
        for m in data:
            self.G.add_node(m['nama'])
        relasi = [
            ("Lilbah", "KinkOwi"), 
            ("KinkOwi", "Sawit"),
            ("Sawit", "Herlambang"), 
            ("Herlambang", "Anso"),
            ("Anso", "Lilbah")
        ]
        self.G.add_edges_from(relasi)

    def tampilkan_grafik(self):
        print("Tutup grafik untuk kembali ke menu.")
        plt.figure(figsize=(7, 5))
        posisi = nx.spring_layout(self.G)
        nx.draw(self.G, posisi, with_labels=True, node_color="orange", node_size=2000)
        plt.title("Jejaring Kolaborasi dan Relasi Mahasiswa")
        plt.show()

# Modul 6: Linked List 
class NodeLL:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListPendaftar:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        new_node = NodeLL(data)
        if not self.head: 
            self.head = new_node
        else:
            curr = self.head
            while curr.next: 
                curr = curr.next
            curr.next = new_node

    def hapus(self, nim_target):
        curr = self.head
        if curr and curr.data['nim'] == nim_target:
            self.head = curr.next
            return True
        prev = None
        while curr and curr.data['nim'] != nim_target:
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next
            return True
        return False

    def tampilkan(self):
        print("\nDaftar Mahasiswa Aktif (Linked List):")
        curr = self.head
        if not curr: 
            print("Daftar Kosong.")
        while curr:
            print(curr.data['nama'], end=" -> ") 
            curr = curr.next
        if self.head:
            print("None")

# Program Utama
def main():
    sistem_layanan = LayananBeasiswa()
    grafik = GrafSIGMA()
    ll_data = LinkedListPendaftar()
    
    for m in data_mahasiswa:
        ll_data.tambah(m)
    grafik.sinkronisasi(data_mahasiswa)

    while True:
        print("\n=========================================")
        print("Sistem Manajamen Grup Mahasiswa & Apresiasi Beasiswa - SIGMA\n")
        print("1. Array (Statistik IPK)")
        print("2. Stack & Queue (Layanan & Notifikasi)")
        print("3. Sorting (Ranking Beasiswa)")
        print("4. Searching (Cari Data Mahasiswa)")
        print("5. Tree (Pohon Kelayakan Syarat)")
        print("6. Graph (Relasi Kolaborasi)")
        print("7. Linked List (Manajemen Data Dinamis)")
        print("0. Keluar")
        print("=========================================")
        
        pilih = input("\nPilih Menu: ")

        if pilih == '1':
            lihat_statistik()
        elif pilih == '2':
            print("\n1. Masuk Antrean | 2. Proses Antrean | 3. Riwayat")
            sub = input("Pilih opsi: ")
            if sub == '1':
                nim_antre = input("Masukkan NIM mahasiswa yang antre: ")
                sistem_layanan.tambah_antrean(nim_antre, data_mahasiswa)
            elif sub == '2':
                sistem_layanan.proses_layanan()
            elif sub == '3':
                sistem_layanan.lihat_notif()
        elif pilih == '3':
            tampilkan_ranking(data_mahasiswa)
        elif pilih == '4':
            cari_mahasiswa(data_mahasiswa)
        elif pilih == '5':
            pohon = buat_pohon_beasiswa(data_mahasiswa)
            print("\nHierarki Syarat Kelayakan Beasiswa:")
            pohon.tampilkan()
        elif pilih == '6':
            grafik.tampilkan_grafik()
        elif pilih == '7':
            ll_data.tampilkan()
            print("\n1. Tambah Data | 2. Hapus Data")
            sub = input("Pilih opsi: ")
            if sub == '1':
                nim_b = input("NIM: ")
                nama_b = input("Nama: ")
                ipk_b = float(input("IPK: "))
                semester_b = int(input("Semester: "))
                prodi_b = input("Prodi: ")
                data_b = {'nim': nim_b, 'nama': nama_b, 'ipk': ipk_b, 'semester': semester_b, 'prodi': prodi_b}
                data_mahasiswa.append(data_b)
                ll_data.tambah(data_b)
                grafik.G.add_node(nama_b)
                print("Data berhasil ditambahkan.")
            elif sub == '2':
                target_h = input("Masukkan NIM yang akan dihapus: ")
                if ll_data.hapus(target_h):
                    data_mahasiswa[:] = [d for d in data_mahasiswa if d['nim'] != target_h]
                    print("Data berhasil dihapus.")
                else:
                    print("Data tidak ditemukan.")
        elif pilih == '0':
            print("Program selesai. Adiossss")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()