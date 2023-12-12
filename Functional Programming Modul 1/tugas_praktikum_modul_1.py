# -*- coding: utf-8 -*-
"""Tugas Praktikum Modul 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WR0249GfWRI1uAXoXg9beXWBMeRJRspl
"""

# Tugas Praktikum Modul 1

list_buku = []

def input_buku():
    judul = input("Judul buku: ")
    pengarang = input("Nama pengarang: ")
    buku = {'judul': judul, 'pengarang': pengarang, 'status': 'tersedia'}
    list_buku.append(buku)
    print("Buku '" + judul + "' oleh " + pengarang + " telah ditambahkan ke dalam list.")

def tampilkan_list_buku():
    print("\nDaftar Buku Tersedia:")
    for idx, buku in enumerate(list_buku):
        if buku['status'] == 'tersedia':
            print(str(idx+1) + ". " + buku['judul'] + " oleh " + buku['pengarang'] + " (" + buku['status'] + ")")

def edit_buku():
    tampilkan_list_buku()
    idx = int(input("Masukkan nomor buku yang ingin diedit: ")) - 1
    if idx >= 0 and idx < len(list_buku):
        judul = input("Masukkan judul buku yang baru: ")
        pengarang = input("Masukkan nama pengarang yang baru: ")
        list_buku[idx]['judul'] = judul
        list_buku[idx]['pengarang'] = pengarang
        print("Buku telah diubah menjadi '" + judul + "' oleh " + pengarang + ".")
    else:
        print("Nomor buku tidak valid.")

while True:
    print("\nAkun Admin:")
    print("1. Tambah Buku")
    print("2. Tampilkan List Buku")
    print("3. Edit Buku")
    print("4. Keluar")
    pilihan = input("Pilih: ")

    if pilihan == '1':
        input_buku()
    elif pilihan == '2':
        tampilkan_list_buku()
    elif pilihan == '3':
        edit_buku()
    elif pilihan == '4':
        break
    else:
        print("Pilihan tidak valid.")

def pinjam_buku(list_buku):
    nim = input("Masukkan NIM Anda: ")
    nama = input("Masukkan Nama Anda: ")
    judul = input("Masukkan judul buku yang ingin dipinjam: ")

    for buku in list_buku:
        if buku['judul'] == judul and buku['status'] == 'tersedia':
            buku['status'] = 'dipinjam oleh ' + nim + ' - ' + nama
            print(nama + ' dengan NIM ' + nim + ' telah meminjam buku \'' + judul + '\'.')
            return

    print('Buku \'' + judul + '\' tidak tersedia atau sudah dipinjam oleh pengguna lain.')

def kembalikan_buku(list_buku):
    nim = input("Masukkan NIM Anda: ")
    nama = input("Masukkan Nama Anda: ")
    judul = input("Masukkan judul buku yang ingin dikembalikan: ")

    for buku in list_buku:
        if buku['judul'] == judul and buku['status'].startswith('dipinjam oleh ' + nim + ' - ' + nama):
            buku['status'] = 'tersedia'
            print(nama + ' dengan NIM ' + nim + ' telah mengembalikan buku \'' + judul + '\'.')
            return

    print('Buku \'' + judul + '\' tidak dapat dikembalikan oleh ' + nama + ' dengan NIM ' + nim + '.')

def tampilkan_list_buku(list_buku):
    print("\nDaftar Buku Tersedia:")
    for buku in list_buku:
        if buku['status'] == 'tersedia':
            print(buku['judul'] + ' oleh ' + buku['pengarang'] + ' (' + buku['status'] + ')')

while True:
    tampilkan_list_buku(list_buku)
    print("\nMenu User:")
    print("1. Pinjam Buku")
    print("2. Kembalikan Buku")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        pinjam_buku(list_buku)
    elif pilihan == '2':
        kembalikan_buku(list_buku)
    elif pilihan == '3':
        break
    else:
        print("Pilihan tidak valid.")