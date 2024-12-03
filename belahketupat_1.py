# JUDUL PROGRAM
# Program Belah Ketupat 

#KAMUS
# tinggi (integer):
# i (integer):

# ALGORITMA
tinggi = int(input("Masukkan tinggi belah ketupat: "))

for i in range(1, tinggi + 1):
    print(" " * (tinggi - i), end="")
    print("*" * (2 * i - 1))

for i in range(tinggi - 1, 0, -1):
    print(" " * (tinggi - i), end="")
    print("*" * (2 * i - 1))
