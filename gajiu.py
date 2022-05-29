import streamlit as st

st.write(""" # Aplikasi Penghitung Gaji Karyawan """)
nip = st.number_input('Masukan NIP', 0)
nama = st.text_input('Masukan Nama', 0)
st.write("1. Rektor \n2. Dekan \n3. Kepala Jurusan \n4. Sekjur \n5. Dosen \n6. Staff Lain")
jabatan = st.number_input('Masukan Jabatan', 0)
alamat = st.text_input('Masukan Alamat', 0)
jml_anak = st.number_input('Masukan Jumlah Anak', 0)
lembur = st.number_input('Total jam lembur', 0)
ijin = st.number_input('Total hari ijin', 0)

hitung_gaji = st.button('Hitung gaji')

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
if(jml_anak=='5'):
    tunjangan=1000000
elif(jml_anak =='3'):
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
elif (ijin == '4'):
    pengurangan = 100000
else:
    pengurangan =0

if hitung_gaji :
    gaji_bersih = gaji_pokok+tunjangan+tambahan+pengurangan
    st.write("Gaji Bersih Karyawan adalah ", gaji_bersih)
