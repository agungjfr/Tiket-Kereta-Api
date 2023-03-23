import datetime
from os import system

x = datetime.datetime.now()

system("cls")

def cek_login(username, password) :
    cek_akun = False
    global user_2
    for i in range (len(user)) :
        if ((user[i][0] == username) and (user[i][1] == password)) :
            user_2 = i
            cek_akun = True
        else :
            pass
    return cek_akun

def jadwal_kereta() :
    print()
    print("""
    ===========================================================================================
    |                                   ~~~~ EKONOMI ~~~~~                                    |
    |-----------------------------------------------------------------------------------------|
    |    |          |               Waktu            |             |              |           |
    | No |   Hari   |--------------------------------|   Tujuan    |    Harga     |   Promo   |
    |    |          |  Keberangkatan  |  Kedatangan  |             |              |           |
    |-----------------------------------------------------------------------------------------|
    | 1  | Senin    |      05.45      |     06.45    |  Surabaya   |  Rp. 5.000   |     -     |
    | 2  | Selasa   |      05.45      |     07.00    |  Madura     |  Rp. 7.000   |     -     |
    | 3  | Rabu     |      06.30      |     07.30    |  Mojokerto  |  Rp. 10.000  |     -     |
    | 4  | Kamis    |      05.45      |     08.45    |  Malang     |  Rp. 35.000  |     -     |
    | 5  | Jumat    |      06.00      |     07.15    |  Jombang    |  Rp. 10.000  |     -     |
    | 6  | Sabtu    |      05.30      |     08.30    |  Kediri     |  Rp. 25.000  |    10%    |
    | 7  | Minggu   |      05.30      |     07.00    |  Sidoarjo   |  Rp. 20.000  |    10%    |
    -------------------------------------------------------------------------------------------

    ===========================================================================================
    |                                   ~~~~ BISNIS ~~~~~                                     |
    |-----------------------------------------------------------------------------------------|
    |    |          |               Waktu            |             |              |           |
    | No |   Hari   |--------------------------------|   Tujuan    |    Harga     |   Promo   |
    |    |          |  Keberangkatan  |  Kedatangan  |             |              |           |
    |-----------------------------------------------------------------------------------------|
    | 1  | Senin    |      05.45      |     06.45    |  Surabaya   |  Rp. 20.000  |     -     |
    | 2  | Selasa   |      05.45      |     07.00    |  Madura     |  Rp. 25.000  |     -     |
    | 3  | Rabu     |      06.30      |     07.30    |  Mojokerto  |  Rp. 30.000  |     -     |
    | 4  | Kamis    |      05.45      |     08.45    |  Malang     |  Rp. 65.000  |     -     |
    | 5  | Jumat    |      06.00      |     07.15    |  Jombang    |  Rp. 20.000  |     -     |
    | 6  | Sabtu    |      05.30      |     08.30    |  Kediri     |  Rp. 50.000  |    10%    |
    | 7  | Minggu   |      05.30      |     07.00    |  Sidoarjo   |  Rp. 55.000  |    10%    |
    -------------------------------------------------------------------------------------------""")
    print()
    input("Tekan ENTER untuk kembali ke Menu")

def tampil_ekonomi() :
    system("cls")
    print("""
    ===========================================================================================
    |                                   ~~~~ EKONOMI ~~~~~                                    |
    |-----------------------------------------------------------------------------------------|
    |    |          |               Waktu            |             |              |           |
    | No |   Hari   |--------------------------------|   Tujuan    |    Harga     |   Promo   |
    |    |          |  Keberangkatan  |  Kedatangan  |             |              |           |
    |-----------------------------------------------------------------------------------------|
    | 1  | Senin    |      05.45      |     06.45    |  Surabaya   |  Rp. 5.000   |     -     |
    | 2  | Selasa   |      05.45      |     07.00    |  Madura     |  Rp. 7.000   |     -     |
    | 3  | Rabu     |      06.30      |     07.30    |  Mojokerto  |  Rp. 10.000  |     -     |
    | 4  | Kamis    |      05.45      |     08.45    |  Malang     |  Rp. 35.000  |     -     |
    | 5  | Jumat    |      06.00      |     07.15    |  Jombang    |  Rp. 10.000  |     -     |
    | 6  | Sabtu    |      05.30      |     08.30    |  Kediri     |  Rp. 25.000  |    10%    |
    | 7  | Minggu   |      05.30      |     07.00    |  Sidoarjo   |  Rp. 20.000  |    10%    |
    -------------------------------------------------------------------------------------------""")

def tampil_bisnis() :
    system("cls")
    print("""
    ===========================================================================================
    |                                   ~~~~ BISNIS ~~~~~                                     |
    |-----------------------------------------------------------------------------------------|
    |    |          |               Waktu            |             |              |           |
    | No |   Hari   |--------------------------------|   Tujuan    |    Harga     |   Promo   |
    |    |          |  Keberangkatan  |  Kedatangan  |             |              |           |
    |-----------------------------------------------------------------------------------------|
    | 1  | Senin    |      05.45      |     06.45    |  Surabaya   |  Rp. 20.000  |     -     |
    | 2  | Selasa   |      05.45      |     07.00    |  Madura     |  Rp. 25.000  |     -     |
    | 3  | Rabu     |      06.30      |     07.30    |  Mojokerto  |  Rp. 30.000  |     -     |
    | 4  | Kamis    |      05.45      |     08.45    |  Malang     |  Rp. 65.000  |     -     |
    | 5  | Jumat    |      06.00      |     07.15    |  Jombang    |  Rp. 20.000  |     -     |
    | 6  | Sabtu    |      05.30      |     08.30    |  Kediri     |  Rp. 50.000  |    10%    |
    | 7  | Minggu   |      05.30      |     07.00    |  Sidoarjo   |  Rp. 55.000  |    10%    |
    -------------------------------------------------------------------------------------------""")

def pilih_ekonomi() :
    tampil_ekonomi()
    print()
    pilih_tiket  = int(input("\tPilih tiket  : "))
    pilih_tiket -= 1
    print()
    jumlah_tiket = int(input("\tJumlah pesan tiket : "))
    
    kelas  = "Ekonomi"
    nama   = user[user_2][2]
    hari   = ekonomi[pilih_tiket][0]
    jam    = ekonomi[pilih_tiket][1]
    jam_2  = ekonomi[pilih_tiket][2]
    tujuan = ekonomi[pilih_tiket][3]
    harga  = ekonomi[pilih_tiket][4]
    promo  = ekonomi[pilih_tiket][5]
    diskon = (jumlah_tiket*ekonomi[pilih_tiket][4]) * (ekonomi[pilih_tiket][5]/100)
    total  = (jumlah_tiket*ekonomi[pilih_tiket][4]) - diskon

    struk_beli(kelas, nama, hari, jam, jam_2, tujuan, harga, promo, jumlah_tiket, total)

def pilih_bisnis() :
    tampil_bisnis()
    print()
    pilih_tiket  = int(input("\tPilih tiket  : "))
    pilih_tiket -= 1
    print()
    jumlah_tiket = int(input("\tJumlah pesan tiket : "))

    kelas  = "Bisnis"
    nama   = user[user_2][2]
    hari   = bisnis[pilih_tiket][0]
    jam    = bisnis[pilih_tiket][1]
    jam_2  = bisnis[pilih_tiket][2]
    tujuan = bisnis[pilih_tiket][3]
    harga  = bisnis[pilih_tiket][4]
    promo  = bisnis[pilih_tiket][5]
    diskon = (jumlah_tiket*bisnis[pilih_tiket][4]) * (bisnis[pilih_tiket][5]/100)
    total  = (jumlah_tiket*bisnis[pilih_tiket][4]) - diskon

    struk_beli(kelas, nama, hari, jam, jam_2, tujuan, harga, promo, jumlah_tiket, total)

def struk_beli(kelas, nama, hari, jam, jam_2, tujuan, harga, promo, jumlah, total) :
    laporan_beli.append([kelas, nama, hari, jam, jam_2, tujuan, harga, promo, jumlah, total])
    print()
    print("--------------------------------------------")
    print("          STRUK PEMBELIAN                   ")
    print("--------------------------------------------")
    print(" {hari}       {jam}        {tanggal}".format(hari=x.strftime("%A"),jam=x.strftime("%X"),tanggal=x.date()))
    print("--------------------------------------------")
    print(" Nama Pembeli        : ", nama               )
    print(" Kelas Kereta        : ", kelas              )
    print(" Hari                : ", hari               )
    print(" Waktu Keberangkatan : ", jam                )
    print(" Waktu Kedatangan    : ", jam_2              )
    print(" Tujuan              : ", tujuan             )
    print(" Harga Tiket         : ", harga              )
    print(" Promo Weekend       : ", promo,"%"          )
    print(" Jumlah Tiket        : ", jumlah             )
    print(" Total Bayar         : ", round(total)       )
    print("--------------------------------------------")
    print()
    input("Tekan ENTER untuk kembali ke Menu")

def cek() :
    print()
    print("           - PESANAN -")
    if len(laporan_beli) == 0:
        print()
        print("\tBELUM ADA PEMESANAN")
    else:
        j = 1
        for i in range(len(laporan_beli)) :
            print()
            print("                   ", j)
            print("----------------------------------------------")
            print("               TIKET KERETA                   ")
            print(" {hari}       {jam}        {tanggal}".format(hari=x.strftime("%A"),jam=x.strftime("%X"),tanggal=x.date()))
            print("----------------------------------------------")
            print(" Nama Pembeli        : ", laporan_beli[i][1]   )
            print(" Kelas Kereta        : ", laporan_beli[i][0]   )
            print(" Hari                : ", laporan_beli[i][2]   )
            print(" Waktu Keberangkatan : ", laporan_beli[i][3]   )
            print(" Waktu Kedatangan    : ", laporan_beli[i][4]   ) 
            print(" Tujuan              : ", laporan_beli[i][5]   )
            print(" Harga Tiket         : ", laporan_beli[i][6]   )
            print(" Promo Weekend       : ", laporan_beli[i][7],"%")
            print(" Jumlah Tiket        : ", laporan_beli[i][8]   )
            print(" Total Bayar         : ", round(laporan_beli[i][9]))
            print("----------------------------------------------")
            j += 1
    print()
    total_semua1 = sum(z[9] for z in laporan_beli)
    print("----------------------------------------------------------------")
    print("Total harga semua pesanan Anda adalah : Rp.", round(total_semua1))
    print("----------------------------------------------------------------")
    print()
    input("Tekan ENTER untuk kembali ke Menu")

def cekout() :
    print()
    if len(laporan_beli) == 0 :
        print("\tBELUM ADA PEMESANAN")
        print()
        input("Tekan ENTER untuk kembali ke Menu")
    else :
        j = 1
        for i in range(len(laporan_beli)) :
            print()
            print("                   ", j)
            print("----------------------------------------------")
            print("               TIKET KERETA                   ")
            print(" {hari}       {jam}        {tanggal}".format(hari=x.strftime("%A"),jam=x.strftime("%X"),tanggal=x.date()))
            print("----------------------------------------------")
            print(" Nama Pembeli        : ", laporan_beli[i][1]   )
            print(" Kelas Kereta        : ", laporan_beli[i][0]   )
            print(" Hari                : ", laporan_beli[i][2]   )
            print(" Waktu Keberangkatan : ", laporan_beli[i][3]   )
            print(" Waktu Kedatangan    : ", laporan_beli[i][4]   ) 
            print(" Tujuan              : ", laporan_beli[i][5]   )
            print(" Harga Tiket         : ", laporan_beli[i][6]   )
            print(" Promo Weekend       : ", laporan_beli[i][7],"%")
            print(" Jumlah Tiket        : ", laporan_beli[i][8]   )
            print(" Total Bayar         : ", round(laporan_beli[i][9]))
            print("----------------------------------------------")
            j += 1
        total_semua = sum(z[9] for z in laporan_beli)
        print()
        print("----------------------------------------------------------------")
        print("Total harga semua pesanan Anda adalah : Rp.", round(total_semua))
        print("----------------------------------------------------------------")
        sisa  = 0
        global sisa1
        saldo_awal = 0
        saldo_awal += user[user_2][3]
        print()
        print("\tSaldo Anda saat ini : Rp.", saldo_awal)
        print()
        while True :
            print("\n\t[1] Lanjut\n\t[2] Kembali ke Menu")
            print()
            bayar = input("Pilihan Anda : ")
            if bayar == "1":
                if saldo_awal > total_semua :
                    sisa = saldo_awal - total_semua
                    print()
                    print("\tKembalian Anda adalah Rp.", round(sisa))
                    sisa1 = sisa
                    user[user_2][3] = sisa1
                    while laporan_beli:
                        laporan_beli.pop(0)
                    print()
                    print("\tTerimakasih!")
                    print()
                    input("Tekan ENTER untuk kembali ke Menu")
                    break
                else :
                    print()
                    print("\tMaaf Saldo anda kurang")
                    print()
                    input("Tekan ENTER untuk kembali ke Menu")
                    break
            elif bayar == "2" :
                print()
                input("Tekan ENTER untuk kembali ke Menu")
                break
            else :
                print()
                print("Input tidak dikenal")

def batal() :
    print()
    print("            - PESANAN -")
    if len(laporan_beli) == 0:
        print()
        print("\tBELUM ADA PEMESANAN")
        print()
        input("Tekan ENTER untuk kembali ke Menu")
    else:
        while True :
            j = 1
            for i in range(len(laporan_beli)) :
                print("                   ", j)
                print("----------------------------------------------")
                print("               TIKET KERETA                   ")
                print(" {hari}       {jam}        {tanggal}".format(hari=x.strftime("%A"),jam=x.strftime("%X"),tanggal=x.date()))
                print("----------------------------------------------")
                print(" Nama Pembeli        : ", laporan_beli[i][1]   )
                print(" Kelas Kereta        : ", laporan_beli[i][0]   )
                print(" Hari                : ", laporan_beli[i][2]   )
                print(" Waktu Keberangkatan : ", laporan_beli[i][3]   )
                print(" Waktu Kedatangan    : ", laporan_beli[i][4]   ) 
                print(" Tujuan              : ", laporan_beli[i][5]   )
                print(" Harga Tiket         : ", laporan_beli[i][6]   )
                print(" Promo Weekend       : ", laporan_beli[i][7],"%")
                print(" Jumlah Tiket        : ", laporan_beli[i][8]   )
                print(" Total Bayar         : ", round(laporan_beli[i][9]))
                print("----------------------------------------------")
                j += 1
                print("\t[1] Batalkan Pesanan\n\t[2] Pesanan selanjutnya\n\n[3] Kembali ke Menu")
                print()
                pilih = input("Pilih Menu(nomer) : ")
                if pilih == "1" :
                    pilihHapus = int(input("Ketik nomer pesanan jika ingin membatalkan : "))
                    pilihHapus -= 1
                    del laporan_beli[pilihHapus]
                    print()
                    print("\tPesanan telah dibatalkan")
                    print()
                    input("Tekan ENTER untuk kembali ke Menu")
                elif pilih == "2" :
                    print()
                elif pilih == "3" :
                    return True
                else :
                    print()
                    print("Input Tidak Dikenal!")

def akun() :
    print()
    print("Nama Pengguna  : ", user[user_2][2]       )
    print("Username       : ", user[user_2][0]       )
    print("Password       : ", user[user_2][1]       )
    print("Saldo          : ", round(user[user_2][3]))
    print()
    input("Tekan ENTER untuk kembali ke Menu")

def isi_saldo() :
    print()
    print("\t[1] Lanjut\n\t[2] Kembali ke Menu")
    print()
    tanya = input("Pilihan Anda : ")
    if tanya == "1" :
        saldo = int(input("\tMasukkan nominal uang : Rp. "))
        user[user_2].append(saldo)
        user[user_2][3] = user[user_2][3] + user[user_2][4]
        user[user_2].remove(user[user_2][4])
        print()
        print("\tSaldo telah di isi")
        print()
        input("Tekan ENTER untuk kembali ke Menu")
    else :
        print()
        input("Tekan ENTER untuk kembali ke Menu")

def menu() :
    print()
    print("--------------------------------------------------------")
    print("\tSelamat Datang {nama}".format(nama=user[user_2][2]))
    print("--------------------------------------------------------")
    print()
    while True :
        print()
        print("\t[1] Jadwal dan Harga Tiket")
        print("\t[2] Pesan Tiket           ")
        print("\t[3] Cek Pesanan           ")
        print("\t[4] Cekout                ")
        print("\t[5] Batalkan pesanan      ")
        print("\t[6] Info Akun             ")
        print("\t[7] Isi Saldo             ")
        print()
        print("\t[8] Keluar                ")
        print()
        pilih_menu = input("Masukkan pilihan Anda : ")
        if pilih_menu == "1" :
            jadwal_kereta()
        elif pilih_menu == "2" :
            print("------------------------------------------------------")
            print("\t[1] Ekonomi\n\t[2] Bisnis\n\n[ENTER] Kembali ke Menu")
            print()
            pilih_kelas = input("Pilih Kelas Tiket : ")
            if pilih_kelas == "1" :
                pilih_ekonomi()
            elif pilih_kelas == "2" :
                pilih_bisnis()
            else :
                input("Tekan ENTER untuk kembali ke Menu")
        elif pilih_menu == "3" :
            cek()
        elif pilih_menu == "4" :
            cekout()
        elif pilih_menu == "5" :
            batal()
        elif pilih_menu == "6" :
            akun()
        elif pilih_menu == "7" :
            isi_saldo()
        elif pilih_menu == "8" :
            return True
        else :
            print("Input Tidak Dikenal")

user         = []

laporan_beli = []

ekonomi = [["Senin  ",  "05.30", "06.45 ",  "Surabaya  ", 5000   ,   0],
           ["Selasa ",  "05.30", "07.00 ",  "Madura    ", 7000   ,   0],
           ["Rabu   ",  "06.30", "07.30 ",  "Mojokerto ", 10000  ,   0],
           ["Kamis  ",  "05.45", "08.45 ",  "Malang    ", 35000  ,   0],
           ["Jumat  ",  "06.00", "07.15 ",  "Jombang   ", 10000  ,   0],
           ["Sabtu  ",  "05.30", "08.30 ",  "Kediri    ", 25000  ,  10],
           ["Minggu ",  "05.30", "07.00 ",  "Sidoarjo  ", 20000  ,  10]]

bisnis  = [["Senin  ",  "05.30", "06.45 ",  "Surabaya  ", 20000  ,   0],
           ["Selasa ",  "05.30", "07.00 ",  "Madura    ", 25000  ,   0],
           ["Rabu   ",  "06.30", "07.30 ",  "Mojokerto ", 30000  ,   0],
           ["Kamis  ",  "05.45", "08.45 ",  "Malang    ", 65000  ,   0],
           ["Jumat  ",  "06.00", "07.15 ",  "Jombang   ", 20000  ,   0],
           ["Sabtu  ",  "05.30", "08.30 ",  "Kediri    ", 50000  ,  10],
           ["Minggu ",  "05.30", "07.00 ",  "Sidoarjo  ", 55000  ,  10]]

def main() :
    while True :
        print()
        print("====================================================================")
        print("|                            TIKET.KU                              |")
        print("|               Aplikasi Pemesanan Tiket Kereta Api                |")
        print("|                                                                  |")
        print("|  {hari}                      {jam}               {tanggal}   |".format(hari=x.strftime("%A"), jam=x.strftime("%X"), tanggal=x.date()))
        print("--------------------------------------------------------------------")
        print()
        print("\t[1] Masuk\n\t[2] Daftar\n\n\t[3] Keluar Aplikasi")
        print()
        pilih1 = input("Silihkan masukkan pilihan Anda : ")
        if pilih1 == "1" :
            print()
            username = input("\tUsername : ")
            password = input("\tPassword : ")
            print()
            if (cek_login(username, password) == True) :
                menu()
            else :
                print("\tUsername atau Password tidak valid!")
                print()
                input("\tTekan ENTER untuk kembali")
        elif pilih1 == "2" :
            print()
            nama        = input("\tMasukkan Nama Lengkap : ")
            username    = input("\tBuat Username         : ")
            password    = input("\tBuat Password         : ")
            saldo_mula  = 0
            user.append([username, password, nama, saldo_mula])
            print()
            print("\tPendaftaran Sukses!")
            print()
            input("Tekan ENTER untuk kembali ke Menu")
            continue
        elif pilih1 == "3" :
            print("--------------------------------------------------------------------")
            print("                             Terimahkasih                           ")
            print("--------------------------------------------------------------------")
            return True
        else : 
            print()
            print("Input Tidak Dikenal")
            input("Tekan ENTER untuk kembali ke Menu")
main()