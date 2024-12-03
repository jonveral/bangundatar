# JUDUL PROGRAM
# Program Segitiga

# KAMUS
# n : integer
# i : integer

# ALGORITMA
n = int(input("Masukkan jumlah baris: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))
