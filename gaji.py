
import streamlit as st
import numpy as np
import pandas as pd

lagi='y'
while lagi=='y':

    print ("\t \t Gaji Karyawan")
    print ("===============================================================================")
    nip=input("Masukan No Induk Pegawai \t: ")
    nama=input("Masukan Nama Dosen/Staff \t: ")
    print ("1. Rektor \n2. Dekan \n3. Kepala Jurusan \n4. Sekjur \n5. Dosen \n6. Staff Lain")
    jabatan=input("Masukan Jabatan \t\t: ")
    alamat=input("Masukan Alamat \t\t\t: ")
    jml_anak=input("Masukan Jumlah Anak \t\t: ")
    lembur = input("Masukan jumlah lembur \t\t: ")
    ijin = input("Masukan jumlah ijin \t\t: ")

    #fungsi gaji pokok
    if (jabatan=='1'):
        gaji_pokok=10000000
        jab="Rektor"
    elif(jabatan=='2'):
        gaji_pokok=8500000
        jab="Dekan"
    elif(jabatan=='3'):
        gaji_pokok=6000000
        jab="Kepala Jurusan"
    elif(jabatan=='4'):
        gaji_pokok=5000000
        jab="Sekjur"
    elif(jabatan=='5'):
        gaji_pokok=4000000
        jab="Dosen"
    else:
        gaji_pokok=3000000
        jab="Staff Lain"

    #fungsi tunjangan anak
    if(jml_anak>='5'):
        tunjangan=1000000
    elif(jml_anak <='3'):
        tunjangan=750000
    else:
        tunjangan=500000

    #fungsi lembur
    if(lembur == '1'):
        tambahan=10000
    elif(lembur == '2'):
        tambahan=15000
    elif(lembur == '3'):
        tambahan=30000
    else:
        tambahan=0

    #fungsi ijin
    if (ijin == '1'):
        pengurangan = 5000
    elif(ijin == '2'):
        pengurangan = 10000
    elif (ijin == '3'):
        pengurangan = 15000
    elif (ijin >= '4'):
        pengurangan = 100000
    else:
        pengurangan =0

    gaji_bersih = gaji_pokok+tunjangan+tambahan+pengurangan

    print ("")

    print ("\n")
    print ("===============================================================================")
    print ("\t\t\t Slip Gaji Karyawan")
    print ("===============================================================================")
    print ("")
    print ("Nip \t\t: ",nip)
    print ("Nama \t\t: ",nama)
    print ("Jabatan \t: ",jab)
    print ("Alamat \t\t: ",alamat)
    print ("===============================================================================")
    print ("Gaji pokok\t: ", gaji_pokok)
    print ("-------------------------------------------------------------------------------")
    print ("Lembur \t\t: ",lembur, "jam")
    print ("Ijin \t\t: ", ijin, "hari")
    print ("Gaji bersih \t: ",gaji_bersih)
    print ("")
    print ("===============================================================================")
    print ("")
    lagi=input("Ambil Data Lagi [y/n]? : ")