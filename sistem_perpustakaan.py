import os

FILE = "data_buku.txt"

# Membaca Data dari File
def baca_data():
    data = []

    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            for baris in file:
                baris = baris.strip()

                if baris != "":
                    kode, judul, penulis, tahun = baris.split(",")
                    data.append([kode, judul, penulis, tahun])

    return data

# Menyimpan Data ke File
def simpan_data(data):
    with open(FILE, "w") as file:
        for buku in data:
            file.write(",".join(buku) + "\n")

# Tambah Buku
def tambah_buku(data):

    print("\n===== TAMBAH BUKU =====")

    kode = input("Kode Buku    : ")

    for buku in data:
        if buku[0] == kode:
            print("Kode buku sudah terdaftar!")
            return

    judul = input("Judul Buku   : ")
    penulis = input("Penulis      : ")
    tahun = input("Tahun Terbit : ")

    data.append([kode, judul, penulis, tahun])

    simpan_data(data)

    print("Data berhasil ditambahkan.")

# Tampilkan Daftar Buku
def tampilkan_buku(data):

    print("\n========== DAFTAR BUKU ==========")

    if len(data) == 0:
        print("Belum ada data buku.")
        return

    print("{:<10}{:<30}{:<20}{:<10}".format(
        "Kode", "Judul", "Penulis", "Tahun"))
    print("-" * 70)

    for buku in data:
        print("{:<10}{:<30}{:<20}{:<10}".format(
            buku[0],
            buku[1],
            buku[2],
            buku[3]
        ))

# Cari Buku
def cari_buku(data):

    kode = input("\nMasukkan Kode Buku : ")

    for buku in data:

        if buku[0] == kode:

            print("\n===== DATA DITEMUKAN =====")
            print("Kode Buku    :", buku[0])
            print("Judul Buku   :", buku[1])
            print("Penulis      :", buku[2])
            print("Tahun Terbit :", buku[3])

            return

    print("Data tidak ditemukan.")

# Edit Data Buku
def edit_buku(data):

    kode = input("\nMasukkan Kode Buku yang akan diedit : ")

    for buku in data:

        if buku[0] == kode:

            print("\n===== DATA BUKU =====")
            print("1. Kode Buku    :", buku[0])
            print("2. Judul Buku   :", buku[1])
            print("3. Penulis      :", buku[2])
            print("4. Tahun Terbit :", buku[3])

            print("\nData apa yang ingin diedit?")
            print("1. Kode Buku")
            print("2. Judul Buku")
            print("3. Penulis")
            print("4. Tahun Terbit")

            pilihan = input("Pilih (1-4) : ")

            if pilihan == "1":
                kode_baru = input("Masukkan Kode Buku Baru : ")

                # Cek apakah kode sudah digunakan
                for b in data:
                    if b[0] == kode_baru:
                        print("Kode buku sudah digunakan!")
                        return

                buku[0] = kode_baru

            elif pilihan == "2":
                buku[1] = input("Masukkan Judul Buku Baru : ")

            elif pilihan == "3":
                buku[2] = input("Masukkan Penulis Baru : ")

            elif pilihan == "4":
                buku[3] = input("Masukkan Tahun Terbit Baru : ")

            else:
                print("Pilihan tidak valid.")
                return

            simpan_data(data)

            print("\nData berhasil diperbarui.")
            return

    print("Data tidak ditemukan.")

# Hapus Buku
def hapus_buku(data):

    kode = input("\nMasukkan Kode Buku yang akan dihapus : ")

    for buku in data:
        if buku[0] == kode:
            data.remove(buku)
            simpan_data(data)

            print("Data berhasil dihapus.")
            return

    print("Data tidak ditemukan.")

# Urutkan Buku Berdasarkan Judul
def urut_judul(data):

    if len(data) == 0:
        print("\nBelum ada data buku.")
        return

    data.sort(key=lambda x: x[1].lower())
    simpan_data(data)

    print("\nData berhasil diurutkan berdasarkan Judul.\n")

    tampilkan_buku(data)

# Urutkan Buku Berdasarkan Tahun Terbit
def urut_tahun(data):

    if len(data) == 0:
        print("\nBelum ada data buku.")
        return

    data.sort(key=lambda x: int(x[3]))
    simpan_data(data)

    print("\nData berhasil diurutkan berdasarkan Tahun Terbit.\n")

    tampilkan_buku(data)

# Hitung Jumlah Buku
def hitung_buku(data):

    print("\nJumlah Buku :", len(data))

# Tampilkan Buku Terlama
def buku_terlama(data):

    if len(data) == 0:
        print("\nBelum ada data buku.")
        return

    buku = min(data, key=lambda x: int(x[3]))

    print("\n===== BUKU TERLAMA =====")
    print("Kode Buku    :", buku[0])
    print("Judul Buku   :", buku[1])
    print("Penulis      :", buku[2])
    print("Tahun Terbit :", buku[3])

# Tampilkan Buku Terbaru
def buku_terbaru(data):

    if len(data) == 0:
        print("\nBelum ada data buku.")
        return

    buku = max(data, key=lambda x: int(x[3]))

    print("\n===== BUKU TERBARU =====")
    print("Kode Buku    :", buku[0])
    print("Judul Buku   :", buku[1])
    print("Penulis      :", buku[2])
    print("Tahun Terbit :", buku[3])

# Menu Utama
def menu():

    data = baca_data()

    while True:
        print("\n================================")
        print("      SISTEM PERPUSTAKAAN")
        print("================================")
        print("1. Tambah Buku")
        print("2. Tampilkan Daftar Buku")
        print("3. Cari Buku")
        print("4. Edit Data Buku")
        print("5. Hapus Buku")
        print("6. Urutkan Buku Berdasarkan Judul")
        print("7. Urutkan Buku Berdasarkan Tahun Terbit")
        print("8. Hitung Jumlah Buku")
        print("9. Tampilkan Buku Terlama")
        print("10. Tampilkan Buku Terbaru")
        print("11. Keluar")

        pilihan = input("\nPilih Menu : ")
        if pilihan == "1":
            tambah_buku(data)
        elif pilihan == "2":
            tampilkan_buku(data)
        elif pilihan == "3":
            cari_buku(data)
        elif pilihan == "4":
            edit_buku(data)
        elif pilihan == "5":
            hapus_buku(data)
        elif pilihan == "6":
            urut_judul(data)
        elif pilihan == "7":
            urut_tahun(data)
        elif pilihan == "8":
            hitung_buku(data)
        elif pilihan == "9":
            buku_terlama(data)
        elif pilihan == "10":
            buku_terbaru(data)
        elif pilihan == "11":
            print("\nTerima kasih telah menggunakan Sistem Perpustakaan.")
            break
        else:
            print("\nMenu tidak tersedia. Silakan pilih kembali.")

# Program Utama
menu()