# JUDUL PROGRAM
# Program Trapesium Siku-siku

# KAMUS
# sisi_atas   :  integer
# sisi_bawah  :  integer
# tinggi      :  integer
# bintang     :  integer
# i           :  integer

# ALGORTIMA
def cetak_trapesium(sisi_atas, sisi_bawah, tinggi):
    for i in range(tinggi):
        bintang = sisi_atas + i
        print("*" * bintang + " " * (sisi_bawah - bintang))

sisi_atas = int(input("Masukkan panjang sisi atas: "))
sisi_bawah = int(input("Masukkan panjang sisi bawah: "))
tinggi = int(input("Masukkan tinggi trapesium: "))

if sisi_bawah < sisi_atas:
    sisi_atas, sisi_bawah = sisi_atas, sisi_bawah

cetak_trapesium(sisi_atas, sisi_bawah, tinggi)
