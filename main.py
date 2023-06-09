import os, time # Mengimpor modul os dan time
from datetime import datetime # Mengimport modul datetime

maxQueue = 10 # Menetapkan batas maksimum antrean
daftarPC = ['PC01', 'PC02', 'PC03', 'PC04', 'PC05', 'PC06', 'PC07', 'PC08', 'PC09', 'PC10'] # menetapkan jumlah dan nama/nomor PC

class Queue: # Menginisialisasi kelas 'Queue'
    def __init__(self, max_size):
        self.size = max_size
        self.current_size = 0
        self.data = []

    def isEmpty(self): # Fungsi jika antrean kosong
        if self.current_size == 0:
            return True
        else:
            return False

    def isFull(self): # Fungsi jika antrean penuh
        if self.current_size == self.size:
            return True
        else:
            return False

    def tambahdata(self): # Fungsi Menambahkan Data Antrean
        os.system("cls") # Menggunakan modul os untuk membersihkan layar terminal
        print("================ Menambah data antrean PC ================\n")
        if self.isFull():
            print("Maaf, Antrean penuh. Anda tidak dapat mengisi data antrean untuk saat ini.")
        else:
            nomor = 0
            print("Berikut daftar PC yang tersedia :")
            for i in daftarPC:
                nomor += 1
                print(f"[{nomor}] {i}")

            newdataPC = str(input("\nPilih PC [dengan memasukkan nama pc, contoh: pc01] : "))
            newdataNama = str(input("Masukkan nama pengantre : "))
            if newdataPC == 'PC01' or newdataPC == 'pc01':
                if "PC01" in daftarPC:
                    os.system("cls")
                    self.data.append(f"PC01 - {newdataNama}")
                    self.current_size = len(self.data)
                    daftarPC.remove("PC01")
                    print(f"\nBerhasil menambahkan antrean baru, dengan data sebagai berikut :\nNama pengantre: {newdataNama}\nAkan menempati: PC01")
                else:
                    print("Gagal menambahkan antrean baru, PC01 tidak tersedia.")
                    kembaliKeMenu2()
            elif newdataPC == 'PC02' or newdataPC == 'pc02':
                if "PC02" in daftarPC:
                    os.system("cls")
                    self.data.append(f"PC02 - {newdataNama}")
                    self.current_size = len(self.data)
                    daftarPC.remove("PC02")
                    print(f"\nBerhasil menambahkan antrean baru, dengan data sebagai berikut :\nNama pengantre: {newdataNama}\nAkan menempati: PC02")
                else:
                    print("Gagal menambahkan antrean baru, PC02 tidak tersedia.")
                    kembaliKeMenu2()
            elif newdataPC == 'PC03' or newdataPC == 'pc03':
                if "PC03" in daftarPC:
                    os.system("cls")
                    self.data.append(f"PC03 - {newdataNama}")
                    self.current_size = len(self.data)
                    daftarPC.remove("PC03")
                    print(f"\nBerhasil menambahkan antrean baru, dengan data sebagai berikut :\nNama pengantre: {newdataNama}\nAkan menempati: PC03")
                else:
                    print("Gagal menambahkan antrean baru, PC03 tidak tersedia.")
                    kembaliKeMenu2()
            elif newdataPC == 'PC04' or newdataPC == 'pc04':
                if "PC04" in daftarPC:
                    os.system("cls")
                    self.data.append(f"PC04 - {newdataNama}")
                    self.current_size = len(self.data)
                    daftarPC.remove("PC04")
                    print(f"\nBerhasil menambahkan antrean baru, dengan data sebagai berikut :\nNama pengantre: {newdataNama}\nAkan menempati: PC04")
                else:
                    print("Gagal menambahkan antrean baru, PC04 tidak tersedia.")
                    kembaliKeMenu2()
            elif newdataPC == 'PC05' or newdataPC == 'pc05':
                if "PC05" in daftarPC:
                    os.system("cls")
                    self.data.append(f"PC05 - {newdataNama}")
                    self.current_size = len(self.data)
                    daftarPC.remove("PC05")
                    print(f"\nBerhasil menambahkan antrean baru, dengan data sebagai berikut :\nNama pengantre: {newdataNama}\nAkan menempati: PC05")
                else:
                    print("Gagal menambahkan antrean baru, PC05 tidak tersedia.")
                    kembaliKeMenu2()
            elif newdataPC == 'PC06' or newdataPC == 'pc06':
                if "PC06" in daftarPC:
                    os.system("cls")
                    self.data.append(f"PC06 - {newdataNama}")
                    self.current_size = len(self.data)
                    daftarPC.remove("PC06")
                    print(f"\nBerhasil menambahkan antrean baru, dengan data sebagai berikut :\nNama pengantre: {newdataNama}\nAkan menempati: PC06")
                else:
                    print("Gagal menambahkan antrean baru, PC06 tidak tersedia.")
                    kembaliKeMenu2()
            elif newdataPC == 'PC07' or newdataPC == 'pc07':
                if "PC07" in daftarPC:
                    os.system("cls")
                    self.data.append(f"PC07 - {newdataNama}")
                    self.current_size = len(self.data)
                    daftarPC.remove("PC07")
                    print(f"\nBerhasil menambahkan antrean baru, dengan data sebagai berikut :\nNama pengantre: {newdataNama}\nAkan menempati: PC07")
                else:
                    print("Gagal menambahkan antrean baru, PC07 tidak tersedia.")
                    kembaliKeMenu2()
            elif newdataPC == 'PC08' or newdataPC == 'pc08':
                if "PC08" in daftarPC:
                    os.system("cls")
                    self.data.append(f"PC08 - {newdataNama}")
                    self.current_size = len(self.data)
                    daftarPC.remove("PC08")
                    print(f"\nBerhasil menambahkan antrean baru, dengan data sebagai berikut :\nNama pengantre: {newdataNama}\nAkan menempati: PC08")
                else:
                    print("Gagal menambahkan antrean baru, PC08 tidak tersedia.")
                    kembaliKeMenu2()
            elif newdataPC == 'PC09' or newdataPC == 'pc09':
                if "PC09" in daftarPC:
                    os.system("cls")
                    self.data.append(f"PC09 - {newdataNama}")
                    self.current_size = len(self.data)
                    daftarPC.remove("PC09")
                    print(f"\nBerhasil menambahkan antrean baru, dengan data sebagai berikut :\nNama pengantre: {newdataNama}\nAkan menempati: PC09")
                else:
                    print("Gagal menambahkan antrean baru, PC09 tidak tersedia.")
                    kembaliKeMenu2()
            elif newdataPC == 'PC10' or newdataPC == 'pc10':
                if "PC10" in daftarPC:
                    os.system("cls")
                    self.data.append(f"PC10 - {newdataNama}")
                    self.current_size = len(self.data)
                    daftarPC.remove("PC10")
                    print(f"\nBerhasil menambahkan antrean baru, dengan data sebagai berikut :\nNama pengantre: {newdataNama}\nAkan menempati: PC10")
                else:
                    print("Gagal menambahkan antrean baru, PC10 tidak tersedia.")
                    kembaliKeMenu2()
            else:
                print("\nGagal menambahkan data antrean!\nPeriksa kembali data yang anda masukkan, apakah memenuhi/sesuai syarat atau tidak.")
            kembaliKeMenu2()

    def hapusdataAntrean(self): # Fungsi menghapus Data Antrean
        os.system("cls")
        print("================ Menghapus data antrean PC ================\n")
        if self.isEmpty():
            kembaliKeMenu(3, "Maaf, antrean kosong. Tidak ada data antrean yang dapat dihapus.")
        else:
            datakeluar = self.data.pop() # Menghapus data antrean dengan menggunakan pop()
            self.current_size = len(self.data) 
            daftarPC.append(f"{datakeluar[0:4]}")  # Menambahkan kembali data pc yang terhapus ke list daftarPC
            kembaliKeMenu(3, f"\nBerhasil menghapus data antrean, dengan data sebagai berikut:\n{datakeluar}")

    def daftardataAntrean(self): # Fungsi menampilkan daftar data antrean saat ini
        os.system("cls")
        print("================ List data antrean ================\n")
        if self.isEmpty():
            print("[Data antrean]\nTidak terdapat satupun data Antrean...")
        else:
            dataAntrean = '\n'.join(self.data) # Menampilkan data antrean lalu diurutkan dengan menggunakan \n (new line/baris baru)
            print(f"[Data antrean]\n{dataAntrean}")
        kembaliKeMenu2()

    def statusAntrean(self): # Fungsi menampilkan status data antrean saat ini
        os.system("cls")
        print("================ Status antrean ================\n")
        print(f"Batas maksimum antrean : {self.size}")
        print(f"Antrean saat ini : {self.current_size}")
        if self.data != []:
            print("\nKeterangan lanjutan antrean :")
            print(f"Antrean terdepan : {self.data[0]}") # Menampilkan data antrean terdepan
            print(f"Antrean terakhir : {self.data[self.current_size-1]}") # Menampilkan data antrean terakhir
        else:
            print("\n[Data antrean]\nTidak terdapat satupun data Antrean...")
        kembaliKeMenu2()

def kembaliKeMenu(detik, pesan): # Fungsi Kembali Ke Menu (dengan loading)
    print(pesan)
    time.sleep(detik) # Membuat seakan2 loading/memproses menggunakan fungsi sleep() dari modul time
    menu()

def kembaliKeMenu2(): # Fungsi Kembali Ke Menu (dengan user's trigger)
    input("\nSentuh tombol <enter> untuk kembali ke menu.")
    menu()

def menu(): # Fungsi Menu
    os.system("cls")
    print("================ Program Antrean PC Warnet ================")
    print(f"\t\t\t{datetime.now().strftime('%d/%m/%Y (%H:%M)')}") # Menampilkan waktu terkini (sesuai local time) menggunakan modul datetime
    print("\nBerikut daftar Menu program yang tersedia :")
    print("[1] Masukkan Data Antrean")
    print("[2] Hapus Data Antrean")
    print("[3] Melihat Daftar Data Antrean")
    print("[4] Melihat Informasi Data Antrean")
    print("[5] Akhiri Program Antrean PC Warnet\n")
    pilihan = input("Pilih menu [sesuai nomor urut menu] : ")
    if pilihan == "1":
        Qstart.tambahdata()
    elif pilihan == "2":
        Qstart.hapusdataAntrean()
    elif pilihan == "3":
        Qstart.daftardataAntrean()
    elif pilihan == "4":
        Qstart.statusAntrean()
    elif pilihan == "5":
        os.system("cls")
        print("Terima kasih telah menggunakan Program Antrean PC Warnet, Kami menerima Kritik & Saran apabila pengguna ingin menyampaikan.")
        time.sleep(3)
        exit()
    else:
        os.system("cls")
        print(f"Pilihan {pilihan} tidak ditemukan.")
        time.sleep(1)
        menu()

Qstart = Queue(maxQueue) # Mengalokasikan kelas Queue kedalam variabel Qstart
menu() # Memanggil fungsi menu untuk ditampilkan