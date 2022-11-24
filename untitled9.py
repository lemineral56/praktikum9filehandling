#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 22:39:17 2022

@author: rhenatabella
""
"""
def handling():
    print()
    print("===PROGRAM FILE HANDLING===")
    print("1. Membuat dan menulis file")
    print("2. Membaca File")
    print("3. Menambahkan Text Pada File")
    print("4. Keluar dari Program")
    print()


def numer(x):
    if x == '1':
        namafile = input("Masukan nama file: ")
        nama = input("Masukan nama anda: ")
        nim = input("Masukan NIM anda: ")
        angkatan = input("Masukan tahun angkatan: ")
        print()
        print("File berhasil dibuat")
        print("---------------------------")
        print()
        file = open(namafile,'w')
        file.write(f'nama: {nama} \nnim: {nim} \nangkatan: {angkatan}')
        file.close
    elif x == '2':
        cari = input("Masukkan nama file: ")
        file = open(cari,'r')
        text = file.read()
        print(text)
        print("---------------------------")
        print()
        file.close()
    elif x == '3':
        cari = input("Masukkan nama file yg ingin ditambahkan: ")
        sahabat = input("Masukan nama sahabatmu: ")
        catatan = input("Masukan catatan tambahan anda: ")
        file = open(cari,'a')
        file.write(f'\nSahabat: {sahabat} \ncatatan: {catatan}')
        print()
        print("Data berhasil ditambahkan")
        print()
        print("---------------------------")
        file.close


while True:
    handling()
    choose = input("Masukan Pilihan Berupa Angka 1-4: ")
    if choose == '4':
        print("Terima kasih telah menggunakan program ini")
        break
    elif choose == '1' or choose == '2' or choose == '3':
        numer(1)
    else:
        print("Error...silahkan masukan input 1-4")
    numer(choose)