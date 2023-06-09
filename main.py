import os, time
from datetime import timedelta, datetime

maxQueue = 10
daftarPC = ['PC01', 'PC02', 'PC03', 'PC04', 'PC05', 'PC06', 'PC07', 'PC08', 'PC09', 'PC10',]

class Queue:
    def __init__(self, max_size):
        self.size = max_size
        self.current_size = 0
        self.datapc = []
        self.datanama = []
        self.data = []

    def isEmpty(self):
        if self.current_size == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.current_size == self.size:
            return True
        else:
            return False

    def tambahdata(self):
        os.system("cls")
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
                    print(f"\nBerhasil menambahkan antrean baru, dengan data sebagai berikut :\n{newdataNama} (PC01)")
                else:
                    print("Gagal menambahkan antrean baru, PC01 tidak tersedia.")
                    kembaliKeMenu2()
            elif newdataPC == 'PC02' or newdataPC == 'pc02':
                if "PC02" in daftarPC:
                    os.system("cls")
                    self.data.append(f"PC02 - {newdataNama}")
                    self.current_size = len(self.data)
                    daftarPC.remove("PC02")
                    print(f"\nBerhasil menambahkan antrean baru, dengan data sebagai berikut :\n{newdataNama} (PC02)")
                else:
                    print("Gagal menambahkan antrean baru, PC02 tidak tersedia.")
                    kembaliKeMenu2()
            elif newdataPC == 'PC03' or newdataPC == 'pc03':
                if "PC03" in daftarPC:
                    os.system("cls")
                    self.data.append(f"PC03 - {newdataNama}")
                    self.current_size = len(self.data)
                    daftarPC.remove("PC03")
                    print(f"\nBerhasil menambahkan antrean baru, dengan data sebagai berikut :\n{newdataNama} (PC03)")
                else:
                    print("Gagal menambahkan antrean baru, PC03 tidak tersedia.")
                    kembaliKeMenu2()
            elif newdataPC == 'PC04' or newdataPC == 'pc04':
                if "PC04" in daftarPC:
                    os.system("cls")
                    self.data.append(f"PC04 - {newdataNama}")
                    self.current_size = len(self.data)
                    daftarPC.remove("PC04")
                    print(f"\nBerhasil menambahkan antrean baru, dengan data sebagai berikut :\n{newdataNama} (PC04)")
                else:
                    print("Gagal menambahkan antrean baru, PC04 tidak tersedia.")
                    kembaliKeMenu2()
            elif newdataPC == 'PC05' or newdataPC == 'pc05':
                if "PC05" in daftarPC:
                    os.system("cls")
                    self.data.append(f"PC05 - {newdataNama}")
                    self.current_size = len(self.data)
                    daftarPC.remove("PC05")
                    print(f"\nBerhasil menambahkan antrean baru, dengan data sebagai berikut :\n{newdataNama} (PC05)")
                else:
                    print("Gagal menambahkan antrean baru, PC05 tidak tersedia.")
                    kembaliKeMenu2()
            elif newdataPC == 'PC06' or newdataPC == 'pc06':
                if "PC06" in daftarPC:
                    os.system("cls")
                    self.data.append(f"PC06 - {newdataNama}")
                    self.current_size = len(self.data)
                    daftarPC.remove("PC06")
                    print(f"\nBerhasil menambahkan antrean baru, dengan data sebagai berikut :\n{newdataNama} (PC06)")
                else:
                    print("Gagal menambahkan antrean baru, PC06 tidak tersedia.")
                    kembaliKeMenu2()
            elif newdataPC == 'PC07' or newdataPC == 'pc07':
                if "PC07" in daftarPC:
                    os.system("cls")
                    self.data.append(f"PC07 - {newdataNama}")
                    self.current_size = len(self.data)
                    daftarPC.remove("PC07")
                    print(f"\nBerhasil menambahkan antrean baru, dengan data sebagai berikut :\n{newdataNama} (PC07)")
                else:
                    print("Gagal menambahkan antrean baru, PC07 tidak tersedia.")
                    kembaliKeMenu2()
            elif newdataPC == 'PC08' or newdataPC == 'pc08':
                if "PC08" in daftarPC:
                    os.system("cls")
                    self.data.append(f"PC08 - {newdataNama}")
                    self.current_size = len(self.data)
                    daftarPC.remove("PC08")
                    print(f"\nBerhasil menambahkan antrean baru, dengan data sebagai berikut :\n{newdataNama} (PC08)")
                else:
                    print("Gagal menambahkan antrean baru, PC08 tidak tersedia.")
                    kembaliKeMenu2()
            elif newdataPC == 'PC09' or newdataPC == 'pc09':
                if "PC09" in daftarPC:
                    os.system("cls")
                    self.data.append(f"PC09 - {newdataNama}")
                    self.current_size = len(self.data)
                    daftarPC.remove("PC09")
                    print(f"\nBerhasil menambahkan antrean baru, dengan data sebagai berikut :\n{newdataNama} (PC09)")
                else:
                    print("Gagal menambahkan antrean baru, PC09 tidak tersedia.")
                    kembaliKeMenu2()
            elif newdataPC == 'PC10' or newdataPC == 'pc10':
                if "PC10" in daftarPC:
                    os.system("cls")
                    self.data.append(f"PC10 - {newdataNama}")
                    self.current_size = len(self.data)
                    daftarPC.remove("PC10")
                    print(f"\nBerhasil menambahkan antrean baru, dengan data sebagai berikut :\n{newdataNama} (PC10)")
                else:
                    print("Gagal menambahkan antrean baru, PC10 tidak tersedia.")
                    kembaliKeMenu2()
            else:
                print("\nGagal menambahkan data antrean!\nPeriksa kembali data yang anda masukkan, apakah memenuhi/sesuai syarat atau tidak.")
        kembaliKeMenu2()

    def hapusdataAntrean(self):
        os.system("cls")
        print("================ Menghapus data antrean PC ================\n")
        if self.isEmpty():
            kembaliKeMenu(3, "Maaf, antrean kosong. Tidak ada data antrean yang dapat dihapus.")
        else:
            datakeluar = self.data.pop()
            kembaliKeMenu(3, f"\nBerhasil menghapus data antrean, dengan data sebagai berikut:\n{datakeluar}")
            self.current_size = len(self.data)
            daftarPC.append(f"{datakeluar[0:4]}")

    def daftardataAntrean(self):
        os.system("cls")
        print("================ List data antrean ================\n")
        if self.isEmpty():
            print("[Data antrean]\nTidak terdapat satupun data Antrean...")
        else:
            datalist = '\n'.join(self.data)
            print(f"[Data antrean]\n{datalist}")
        kembaliKeMenu2()

    def statusAntrean(self):
        os.system("cls")
        print("================ Status antrean ================\n")
        print(f"Batas maksimum antrean : {self.size}")
        print(f"Antrean saat ini : {self.current_size}")
        if self.isEmpty():
            print("\n[Data antrean]\nTidak terdapat satupun data Antrean...")
        else:
            print("\nKeterangan lanjutan antrean :")
            print(f"Antrean terdepan : {self.data[0]}")
            print(f"Antrean terakhir : {self.data[self.current_size-1]}")
        kembaliKeMenu2()

def kembaliKeMenu(detik, pesan):
    print(pesan)
    time.sleep(detik)
    menu()

def kembaliKeMenu2():
    input("\nSentuh tombol <enter> untuk kembali ke menu.")
    menu()

def menu():
    os.system("cls")
    print("================ Program Antrean PC Warnet ================")
    print(f"\t\t\t{datetime.now().strftime('%d/%m/%Y (%H:%M)')}")
    print("\nBerikut daftar Menu program yang tersedia :")
    print("[1] Masukkan data antrean")
    print("[2] Hapus data antrean")
    print("[3] Melihat list data antrean")
    print("[4] Melihat informasi data antrean")
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
        exit()
    else:
        os.system("cls")
        print(f"Pilihan {pilihan} tidak ditemukan.")
        time.sleep(1)
        menu()

Qstart = Queue(maxQueue)
menu()