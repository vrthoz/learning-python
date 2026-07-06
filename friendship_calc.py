print("BERAPA LAMA PERTEMANAN KALIAN SUDAH BERLANGSUNG?")

# Input data dari user
nama_user = input("Masukkan namamu: ")
nama_teman = input("Lalu nama temanmu? ")
tahun_temu = int(input("Tahun berapa kalian bertemu? (Ex. 2014) "))
tahun_sekarang = int(input("Tahun sekarang? (Ex. 2026) "))

# Perhitungan lama pertemanan
lama_pertemanan = tahun_sekarang - tahun_temu
jumlah_hari = lama_pertemanan * 365

# The result
print(f"Selamat {nama_user} dan {nama_teman}, kalian sudah berteman selama {lama_pertemanan} tahun!")
print(f"Itu berarti, dalam hitungan hari kalian sudah berteman selama {jumlah_hari} hari.")
if lama_pertemanan >= 5:
    print("Bestie abizz! Semoga lancar terus, guys!")
elif 1 <= lama_pertemanan < 5:
    print("Oke, mulai asik, nih!")
else:
    print("Baru kenal, nih! Gas terus, ya!")
