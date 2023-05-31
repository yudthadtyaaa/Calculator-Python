# - CODE BY M.YUDITH ARYANTA ADITYA -
# UNTUK MEMERINTAH TERMINAL SECARA LANGSUNG TANPA HARUS MEMERINTAH DI TERMINAL LAGI BEGITULAH
import os

# UNTUK MENG-SET INFORMASI LOKAL PROGRAM MENGGUNAKAN SEMUA KONSTANTA YANG TERSEDIA
import locale
locale.setlocale(locale.LC_ALL, '')

# UNTUK MENAMBAHKAN FUNGSI MENAMPILKAN TABEL
from tabulate import tabulate

# LIST UNTUK RIWAYAT 
riwayat = []
# DICTIONARY UNTUK MENYIMPAN DATA KURS MATA UANG (DISINI ADA 2)
kurs = {
    "USD": 14300, 
    "KWD": 47200
    } 

# FUNGSI CREATE  ADA DI riwayat.append UNTUK MEMASUKKAN HASIL HITUNGAN KE RIWAYAT
# RUMUS LUAS BANGUN DATAR
def luas_persegi():
    s = int(input("Masukkan Sisi Persegi: "))
    luas = s * s
    print("hasilnya adalah ", luas)
    riwayat.append(["Hasil dari luas persegi: {}".format(luas)])
def luas_segitiga():
    a = int(input("Masukkan Alas Segitiga: "))
    t = int(input("Masukkan Tinggi Segitiga: "))
    luas = a * t
    print("Hasilnya adalah: ",luas)
    riwayat.append(["Hasil dari luas segitiga: {}".format(luas)])
def luas_persegi_panjang():
    p = int(input("Masukkan Panjang: "))
    l = int(input("Masukkan Lebar: "))
    luas = p*l
    print("Hasilnya adalah: ", luas)
    riwayat.append(["Hasil dari luas persegi panjang: {}".format(luas)])
def luas_trapesium():
    s = int(input("Masukkan Sisi: "))
    t = int(input("Masukkan Tinggi: "))
    luas = ((s+s)*t)/2
    print("Hasilnya adalah: ",luas)
    riwayat.append(["Hasil dari luas trapesium: {}".format(luas)])
def luas_jajargenjang():
    a = int(input("Masukkan Alas: "))
    t = int(input("Masukkan Tinggi: "))
    luas = a * t
    print("Hasilnya adalah: ", luas)
    riwayat.append(["Hasil dari luas jajargenjang: {}".format(luas)])
def luas_layang():
    d1 = int(input("Masukkan Diagonal 1: "))
    d2 = int(input("Masukkan Diagonal 2: "))
    luas = (d1*d2)/2
    print("Hasilnya adalah: ", luas)
    riwayat.append(["Hasil dari luas layang-layang: {}".format(luas)])
def luas_ketupat():
    d1 = int(input("Masukkan Diagonal 1: "))
    d2 = int(input("Masukkan Diagonal 2: "))
    luas = (d1*d2)/2
    print("Hasilnya adalah: ", luas)
    riwayat.append(["Hasil dari luas ketupat: {}".format(luas)])
def luas_lingkaran():
    phi1 = 3.14
    phi2 = 22/7
    r = int(input("Masukkan Jari-Jari: "))
    jari = r*r
    pil = int(input("""Pilih Phi yang ingin digunakan :
[1] Phi 3.14
[2] Phi 22/7
Pilih: """))
    if pil == 1:
        hasil = phi1*jari
        print("Hasilnya adalah: ", hasil)
        riwayat.append(["Hasil dari luas lingkaran dengan phi 3.14: {}".format(hasil)])
    elif pil == 2:
        hasil = phi2*jari
        print("Hasilnya adalah: ", hasil)
        riwayat.append(["Hasil dari luas: {}".format(hasil)])
    else:
        "Input Salah"
    return pil

# FUNGSI CREATE  ADA DI riwayat.append UNTUK MEMASUKKAN HASIL HITUNGAN KE RIWAYAT
# RUMUS KELILING BANGUN DATAR
def kel_persegi():
    s = int(input("Masukkan Sisi Persegi: "))
    kel = 4*s
    print("hasilnya adalah ", kel)
    riwayat.append(["Hasil dari keliling persegi: {}".format(kel)])
def kel_segitiga():
    s1 = int(input("Masukkan Sisi 1 Segitiga: "))
    s2 = int(input("Masukkan Sisi 2 Segitiga: "))
    s3 = int(input("Masukkan Sisi 3 Segitiga: "))
    kel = s1 + s2 + s3
    print("Hasilnya adalah: ",kel)
    riwayat.append(["Hasil dari keliling segitiga: {}".format(kel)])
def kel_persegi_panjang():
    p = int(input("Masukkan Panjang: "))
    l = int(input("Masukkan Lebar: "))
    kel = 2*(p+l)
    print("Hasilnya adalah: ", kel)
    riwayat.append(["Hasil dari keliling persegi panjang: {}".format(kel)])
def kel_trapesium():
    s1 = int(input("Masukkan Sisi Atas: "))
    s2 = int(input("Masukkan Sisi Bawah: "))
    s3 = int(input("Masukkan Sisi Miring: "))
    t = int(input("Masukkan Tinggi: "))
    kel = s1+s2+s3+t
    print("Hasilnya adalah: ",kel)
    riwayat.append(["Hasil dari keliling trapesium {}".format(kel)])
def kel_jajargenjang():
    a = int(input("Masukkan Alas: "))
    s = int(input("Masukkan Sisi Miring: "))
    kel = 2* (a + s)
    print("Hasilnya adalah: ", kel)
    riwayat.append(["Hasil dari keliling jajargenjang: {}".format(kel)])
def kel_layang():
    s1 = int(input("Masukkan Sisi 1: "))
    s2 = int(input("Masukkan Sisi 2: "))
    kel = 2*(s1+s2)
    print("Hasilnya adalah: ", kel)
    riwayat.append(["Hasil dari keliling layang-layang: {}".format(kel)])
def kel_ketupat():
    s = int(input("Masukkan Sisi: "))
    kel = 4*s
    print("Hasilnya adalah: ", kel)
    riwayat.append(["Hasil dari keliling ketupat: {}".format(kel)])
def kel_lingkaran():
    phi1 = 3.14
    phi2 = 22/7
    r = int(input("Masukkan Jari-Jari: "))
    jari = r*r
    pil = int(input("""Pilih Phi yang ingin digunakan :
[1] Phi 3.14
[2] Phi 22/7
Pilih: """))
    if pil == 1:
        hasil = 2*phi1*jari
        print("Hasilnya adalah: ", hasil)
        riwayat.append(["Hasil dari keliling lingkaran dengan phi 3.14: {}".format(hasil)])
    elif pil == 2:
        hasil = 2*phi2*jari
        print("Hasilnya adalah: ", hasil)
        riwayat.append(["Hasil dari keliling lingkaran dengan phi 22/7: {}".format(hasil)])
    else:
        "Input Salah"
    return pil

#FUNGSI UPDATE UNTUK SHOW_MENU DAN KONVERSI KURS KALKULATOR
def update_kurs(show_menu, konv_kurs, kurs):
    x = input("Masukkan Kurs yang ingin di update USD/KWD: ")
    if x.upper() == "USD":
        print("Kurs USD yang sebelumnya: ", kurs["USD"])
        b = kurs.get("USD")
        c = int(input("Masukkan jumlah kurs yang terkini: "))
        kurs.update({"USD" : c})
        riwayat.append(["Mengupdate Kurs USD {} menjadi {}".format ( f'{b:n}', f'{c:n}') ])
        s = input("Mau sekalian hitung bro? y/t: ")
        if s == "y":
            konv_kurs(kurs)
        elif s == "t":
            show_menu()
        else:
            print("salah brodi !!!")
    elif x.upper() == "KWD":
        print("Kurs KWD yang sebelumnya: ", kurs["KWD"])
        b = kurs.get("KWD")
        c = int(input("Masukkan jumlah kurs yang terkini: "))
        kurs.update({"KWD" : c})
        riwayat.append(["Mengupdate Kurs KWD {} dengan hasil IDR {}".format (f'{b:n}', f'{c:n}') ])
        s = input("Mau sekalian hitung bro? y/t: ")
        if s == "y":
                konv_kurs(kurs)
        elif s == "t":
                show_menu()
        else:
            print("salah brodi !!!")
    else:
        print("Input Salah")

def konv_kurs(kurs):
    x = input("Pilih Mata Uang\n[1] USD ke IDR\n[2] KWD ke IDR\nPilih Menu: ")
    if x == "1":
        c = int(input("Masukkan Jumlah USD: "))
        hasil = c*kurs["USD"]
        print("Hasil Konversinya adalah: Rp"f'{hasil:n}')
        riwayat.append(["Mengkonversikan USD {} dengan hasil IDR {}".format (int(c), f'{hasil:n}') ])
    elif x == "2":
        c = int(input("Masukkan Jumlah KWD: "))
        hasil = c*kurs["KWD"]
        print("Hasil Konversinya adalah: Rp"f'{hasil:n}')
        riwayat.append(["Mengkonversikan KWD {} dengan hasil IDR {}".format (int(c), f'{hasil:n}') ])
    else:
        print("input salah")

# FUNGSI SHOW/READ RIWAYAT KALKULATOR
def tampil_riwayat(riwayat):
    
    print(tabulate(riwayat, headers=["Riwayat Kalkulator"], tablefmt="fancy_grid"))

# FUNGSI DELETE RIWAYAT KALKULATOR
def hapus_riwayat(tampil_riwayat, riwayat):
    tampil_riwayat(riwayat)
    print("\n")
    x = int(input("Masukkan Nomor Riwayat yang ingin di hapus: "))
    del riwayat[x-1]
    os.system("cls")
    tampil_riwayat(riwayat)

# FUNGSI SHOW MENU PROGRAM KALKULATOR
def show_menu():
    print("\n")
    y = [["Pilih Menu:\n1 ). Persegi\n2 ). Segitiga\n3 ). Persegi Panjang\n4 ). Trapesium\n5 ). Jajargenjang\n6 ). Layang-Layang\n7 ). Belah Ketupat\n8 ). Lingkaran\n9 ). Kurs Mata Uang\n10). Tampilkan Riwayat\n11). Hapus Riwayat\n12). Exit"]]
    print(tabulate(y, headers=["      Kalkulator"], tablefmt="fancy_grid"))
    pil = int(input("PILIH MENU:  "))
    print("\n") 
    os.system("cls")
    # PERSEGI
    if pil == 1:
        rumus = input("Rumus\n[1] Cari Luas\n[2] Cari Keliling\nPilih Rumus: ")
        if rumus == "1":
            luas_persegi()
        elif rumus == "2":
            kel_persegi()
    #SEGITIGA
    elif pil == 2:
        rumus = input("Rumus\n[1] Cari Luas\n[2] Cari Keliling\nPilih Rumus: ")
        if rumus == "1":
            luas_segitiga()
        elif rumus == "2":
            kel_segitiga()
    #PERSEGI PANJANG
    elif pil == 3:
        rumus = input("Rumus\n[1] Cari Luas\n[2] Cari Keliling\nPilih Rumus: ")
        if rumus == "1":
            luas_persegi_panjang()
        elif rumus == "2":
            kel_persegi_panjang()
    #TRAPESIUM
    elif pil == 4:
        rumus = input("Rumus\n[1] Cari Luas\n[2] Cari Keliling\nPilih Rumus: ")
        if rumus == "1":
            luas_trapesium()
        elif rumus == "2":
            kel_trapesium()
    #JAJARGENJANG
    elif pil == 5:
        rumus = input("Rumus\n[1] Cari Luas\n[2] Cari Keliling\nPilih Rumus: ")
        if rumus == "1":
            luas_jajargenjang()
        elif rumus == "2":
            kel_jajargenjang()
    #LAYANG-LAYANG
    elif pil == 6:
        rumus = input("Rumus\n[1] Cari Luas\n[2] Cari Keliling\nPilih Rumus: ")
        if rumus == "1":
            luas_layang()
        elif rumus == "2":
            kel_layang()
    # BELAH KETUPAT
    elif pil == 7:
        rumus = input("Rumus\n[1] Cari Luas\n[2] Cari Keliling\nPilih Rumus: ")
        if rumus == "1":
            luas_ketupat()
        elif rumus == "2":
            kel_ketupat()
    # LINGKARAN
    elif pil == 8:
        rumus = input("Rumus\n[1] Cari Luas\n[2] Cari Keliling\nPilih Rumus: ")
        if rumus == "1":
            luas_lingkaran()
        elif rumus == "2":
            kel_lingkaran()
    # KURS MATA UANG
    elif pil == 9:
        i = input("Rumus\n[1] Update Kurs Terkini\n[2] Konversikan Mata uang\nPilih Rumus: ")
        if i == "1":
            update_kurs(show_menu, konv_kurs, kurs)
        elif i == "2":
            konv_kurs(kurs)
    # MENAMPILKAN RIWAYAT
    elif pil == 10:
        tampil_riwayat(riwayat)
    # MENGHAPUS RIWAYAT
    elif pil == 11:
        hapus_riwayat(tampil_riwayat, riwayat)
    # EXIT PROGRAM
    elif pil == 12:
        print("--- Program Closed ---")
        exit()
    else: 
       print("Salah tekan brodi, Engga ada nomornya!")




while True:
    show_menu()        