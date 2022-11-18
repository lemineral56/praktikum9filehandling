#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 14:37:15 2022

@author: rhenatabella
"""
def buatFile():
    nama = input('Masukkan Nama: ')
    Umur = input('Masukkan Umur: ')
    alamat = input('Masukkan alamat: ')
    email = input('Masukkan email: ')
    dosenwali = input('Masukkan dosen wali: ')

    print('\nBerikut biodatamu')
    file = open('Biodata.txt','w')
    file.write(f'Nama : {nama} \nUmur : {Umur} \nAlamat : {alamat} \nEmail : {email} \nDosen wali : {dosenwali}')
    file.close()
    
def bacaFile():
    file = open('Biodata.txt','r')
    text = file.read()
    print(text)
    file.close()
    
buatFile()
print("/n")
bacaFile()
