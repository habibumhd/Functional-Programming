# -*- coding: utf-8 -*-
"""Tugas Praktikum Modul 5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ni6o_Sox_5r5-zdeInr37kgq-pbpgvFj
"""

# Tugas Praktikum Modul 5
# Kegiatan 1

import matplotlib.pyplot as p
from functools import reduce

# Data Nilai Ujian Mahasiswa
nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]

# Menghitung Rata-rata menggunakan fungsi reduce
rata_rata = reduce(lambda a, b: a + b, nilai_mahasiswa) / len(nilai_mahasiswa)

# Membuat label mahasiswa (sumbu x)
mahasiswa = list(map(lambda x: ' ' + str(x+1), range(len(nilai_mahasiswa))))

# Visualisasi data dalam bentuk diagram batang
p.bar(mahasiswa, nilai_mahasiswa, color='darkgoldenrod')
p.axhline(y=rata_rata, color='darkolivegreen', linestyle='--')
p.legend(['Rata-rata: {:.2f}'.format(rata_rata)])
p.title('Diagram Batang Nilai Ujian Mahasiswa')
p.xlabel('Mahasiswa')
p.ylabel('Nilai Ujian')
p.show()

# Tugas Praktikum Modul 5
# Kegiatan 2

import matplotlib.pyplot as p

data_transaksi =  [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

# Ekstrak Harga Produk dan Jumlah Produk Terjual Untuk Visualisasi Pertama
harga_produk = list(map(lambda x: x[1], data_transaksi))
jumlah_terjual = list(map(lambda x: x[2], data_transaksi))

# Buat Scatter Plot untuk Hubungan Antara Harga Produk dan Jumlah Produk Terjual
p.figure(figsize=(10, 5))
p.subplot(1, 2, 1)
p.scatter(harga_produk, jumlah_terjual, color='darkgoldenrod', edgecolors='tan')
p.xlabel('Harga Produk')
p.ylabel('Jumlah Produk Terjual')
p.title('Hubungan Harga Produk dan Jumlah Produk Terjual')

# Hitung Total Pendapatan untuk Setiap Produk
pendapatan_produk = list(map(lambda x: x[1]*x[2], data_transaksi))

# Tambahkan Bar Chart untuk Menyajikan Pendapatan Produk
nama_produk = list(map(lambda x: x[0], data_transaksi))
p.subplot(1, 2, 2)
p.bar(nama_produk, pendapatan_produk, color='darkgoldenrod')
p.xlabel('Nama Produk')
p.ylabel('Pendapatan Produk')
p.title('Pendapatan Produk')
p.tight_layout()
p.show()

# Tugas Praktikum Modul 5
# Kegiatan 3

import matplotlib.pyplot as p
import numpy as np
from scipy.stats import norm

tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10

# Mengelompokkan tinggi badan dalam interval tertentu
def kelompokkan_tinggi(data, interval_size):
    data_kelompok = {}
    for tinggi in data:
        kelompok = tinggi // interval_size * interval_size
        data_kelompok[kelompok] = data_kelompok.get(kelompok, 0) + 1
    return data_kelompok

# Menghitung frekuensi tinggi badan dalam interval
frekuensi_tinggi = kelompokkan_tinggi(tinggi_badan, interval_size)

# Visualisasi data dalam bentuk histogram
p.bar(frekuensi_tinggi.keys(), frekuensi_tinggi.values(), width=interval_size, color='darkgoldenrod')
p.xlabel('Interval Tinggi Badan')
p.ylabel('Frekuensi')
p.title('Histogram Tinggi Badan')
p.show()

# Kurva PDF pada hasil visualisasi data
rata_rata, std = np.mean(tinggi_badan), np.std(tinggi_badan)

# Menghasilkan nilai untuk kurva PDF
x = np.linspace(min(tinggi_badan), max(tinggi_badan), 100)
pdf = norm.pdf(x, rata_rata, std)

p.bar(frekuensi_tinggi.keys(), frekuensi_tinggi.values(), width=interval_size, align='edge', color='darkgoldenrod', label='Histogram')
p.plot(x, pdf * len(tinggi_badan) * interval_size, color='darkolivegreen', label='PDF')
p.xlabel('Interval Tinggi Badan')
p.ylabel('Frekuensi')
p.title('Histogram PDF Tinggi Badan')
p.legend()
p.show()