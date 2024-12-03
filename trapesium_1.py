# JUDUL PROGRAM
# Program Trapesium

# KAMUS
# jumlah_baris  : integer
# panjang_atas  : integer
# baris         : integer
# panjang_baris : integer

# ALGORITMA
jumlah_baris = int(input("Masukkan jumlah baris trapesium: "))
panjang_atas = int(input("Masukkan panjang atas trapesium: "))

if panjang_atas < jumlah_baris:
    print("Panjang atas trapesium harus lebih besar atau sama dengan jumlah baris!")
else:
    for baris in range(jumlah_baris):
        panjang_baris = panjang_atas + 2 * baris
        print(" " * (panjang_atas + jumlah_baris - baris - 1), end="")
        print("*" * panjang_baris)
