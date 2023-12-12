# -*- coding: utf-8 -*-
"""Latihan Praktikum Modul 3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WJcIrZoDmljiTn86YtYzG3S2do4oPudx
"""

# Latihan Praktikum Modul 3
# Kegiatan 1

def fungsi_ubah():
    konversi = {'minggu': 10080, 'hari': 1440, 'jam': 60, 'menit': 1}
    def ubah(waktu):
        total = 0
        for satuan in waktu.split():
            if satuan in konversi:
                total += int(sebelumnya) * konversi[satuan]
            sebelumnya = satuan
        return total
    return ubah

def fungsi_ubah_semua():
    ubah = fungsi_ubah()
    def ubah_semua(daftar):
        return [ubah(waktu) for waktu in daftar]
    return ubah_semua

ubah_semua = fungsi_ubah_semua()
data = ["3 minggu 3 hari 7 jam 21 menit"]
print(ubah_semua(data))

# Latihan Praktikum Modul 3
# Kegiatan 2

def ambil_angka(waktu):
    return list(filter(str.isdigit, waktu.split()))

def ambil_semua_angka(daftar):
    return [ambil_angka(waktu) for waktu in daftar]

data = ["3 minggu 3 hari 7 jam 21 menit"]
print(ambil_semua_angka(data))

# Latihan Praktikum Modul 3
# Kegiatan 3

daftar_acak = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# Fungsi untuk memfilter tipe data
def filter_float(x):
    return isinstance(x, float)

def filter_int(x):
    return isinstance(x, int)

def filter_string(x):
    return isinstance(x, str)

def petakan_angka(n):
    return {'satuan': n % 10, 'puluhan': n  % 100, 'ratusan': n  % 1000}

angka_float = filter(filter_float, daftar_acak)
angka_int = map(petakan_angka, filter(filter_int, daftar_acak))
kata_string = filter(filter_string, daftar_acak)

print("Angka float: ", list(angka_float))
print("Angka int: ", list(angka_int))
print("String: ", list(kata_string))