import tiket
print('1.Tambah data pembelian tiket')
print('2.Hapus data pembelian tiket')
print('3.Mencari data pembelian tiket:')
print('4.Tampilkan data pembelian tiket')
menu2 = int(input('[data]Pilih:'))
if (menu2==1):
    nama = input ('Nama:')
    hari = input ('Hari:')
    tanggal = input ('Tanggal [YYYY-MM-DD] :')
    nama_KA = input ('Nama KA:')
    no_kursi = input ('No Kursi:')
    print("1. kelas ekonomi = 50.000")
    print("2. kelas premium = 150.000")
    print("3. kelas bisnis = 200.000")
    print("4. kelas eksekutif = 500.000")
    print("5. kelas prioritas = 700.000")
    print("6. kelas sleeper = 1.000.000")
    pilih=int(input("masukkan tipe kelas kereta:"))
    if(pilih==1):
        print("kelas ekonomi = 50.000")
        kelas_KA=('kelas ekonomi')
        jumlah=int(input('jumlah pembelian:'))
        makan_siang=input("apakah ingin mendapatkan jatah makan siang? [Y/N] :")
        if(makan_siang=='Y'):
            makan_siang=30000
            harga=50000
            total=jumlah*(50000+30000)
        elif(makan_siang == 'N'):
            makan_siang=0
            harga=50000
            total=50000*jumlah
        else:
            print("menu tidak tersedia")
    if(pilih==2):
        print("kelas premium = 150.000")
        kelas_KA=('kelas premium')
        jumlah=int(input('jumlah pembelian:'))
        makan_siang=input("apakah ingin mendapatkan jatah makan siang? [Y/N] :")
        if(makan_siang=='Y'):
            makan_siang=30000
            harga=150000
            total=jumlah*(150000+30000)
        elif(makan_siang == 'N'):
            makan_siang=0
            harga=150000
            total=150000*jumlah
        else:
            print("menu tidak tersedia")
    if(pilih==3):
        print("kelas bisnis = 200.000")
        kelas_KA=('kelas bisnis')
        jumlah=int(input('jumlah pembelian:'))
        makan_siang=input("apakah ingin mendapatkan jatah makan siang? [Y/N] :")
        if(makan_siang=='Y'):
            makan_siang=30000
            harga=200000
            total=jumlah*(200000+30000)
        elif(makan_siang == 'N'):
            makan_siang=0
            harga=200000
            total=200000*jumlah
        else:
            print("menu tidak tersedia")
    if(pilih==4):
        print("kelas eksekutif = 500.000")
        kelas_KA=('kelas eksekutif')
        jumlah=int(input('jumlah pembelian:'))
        makan_siang=input("apakah ingin mendapatkan jatah makan siang? [Y/N] :")
        if(makan_siang=='Y'):
            makan_siang=30000
            harga=500000
            total=jumlah*(500000+30000)
        elif(makan_siang == 'N'):
            makan_siang=0
            harga=500000
            total=500000*jumlah
        else:
            print("menu tidak tersedia")
    if(pilih==5):
        print("kelas prioritas = 700.000")
        kelas_KA=('kelas prioritas')
        jumlah=int(input('jumlah pembelian:'))
        makan_siang=input("apakah ingin mendapatkan jatah makan siang? [Y/N] :")
        if(makan_siang=='Y'):
            makan_siang=30000
            harga=700000
            total=jumlah*(700000+30000)
        elif(makan_siang == 'N'):
            makan_siang=0
            harga=700000
            total=700000*jumlah
        else:
            print("menu tidak tersedia")
    if(pilih==6):
        print("kelas sleeper = 1.000.000")
        kelas_KA=('kelas sleeper')
        jumlah=int(input('jumlah pembelian:'))
        makan_siang=input("apakah ingin mendapatkan jatah makan siang? [Y/N] :")
        if(makan_siang=='Y'):
            makan_siang=30000
            harga=1000000
            total=jumlah*(1000000+30000)
        elif(makan_siang == 'N'):
            makan_siang=0
            harga=1000000
            total=1000000*jumlah
        else:
            print("menu tidak tersedia")
    else:
        print("menu tidak tersedia")
    print("total yang harus dibayar :Rp ",total)
                   
    data = [nama,hari,tanggal,kelas_KA,nama_KA,no_kursi,jumlah,makan_siang,harga,total] 
    tiket.add(data)
elif (menu2==2):
    id_tiket = input ('No.Tiket:')
    data = [id_tiket]
    tiket.search(data)
    confirm = input ('Yakin menghapus data pembelian tiket ini?[Y/N]:')
    if (confirm == 'Y'):
        tiket.delete(data)
    else :
        print ('Tidak jadi menghapus data tiket!')
elif (menu2==3):
    id_tiket = input('Masukkan id tiket yang anda cari = ')
    data=[id_tiket]
    tiket.search(data)
elif(menu2==4):
    tiket.show()
else:
    print('Menu tidak tersedia')









































    
 



