import penumpang
print('1.Tambah Penumpang')
print('2.Ubah Penumpang')
print('3.Hapus Penumpang')
print('4.Tampilkan Penumpang')
menu2 = int(input('[Penumpang]Pilih:'))

if (menu2==1):
    nama_penumpang = input ('Nama Penumpang:')
    umur_penumpang = int(input('Umur Penumpang:'))
    kelas_KA = input ('Kelas KA:')
    nama_KA = input ('Nama KA:')
    tanggal_pemberangkatan = input ('Tanggal Pemberangkatan:')
    asal_stasiun = input ('Asal stasiun:')
    tujuan_stasiun = input ('Tujuan stasiun:')
    jam_pemberangkatan = input ('Jam Pemberangkatan:')
    jam_pemberhentian = input ('Jam Pemberhentian:')
    no_kursi = int(input('No kursi:'))
    data = [nama_penumpang,umur_penumpang,kelas_KA,nama_KA,tanggal_pemberangkatan,asal_stasiun,tujuan_stasiun,jam_pemberangkatan,jam_pemberhentian,no_kursi] 
    penumpang.add(data)
elif(menu2==2):
    id_penumpang = int(input("No Penumpang: "))
    nama_penumpang = input ('Nama Penumpang:')
    umur_penumpang = int(input ('Umur Penumpang:'))
    kelas_KA = input ('Kelas KA:')
    nama_KA = input ('Nama KA:')
    tanggal_pemberangkatan =input ('Tanggal Pemberangkatan:')
    asal_stasiun = input ('Asal stasiun:')
    tujuan_stasiun = input ('Tujuan stasiun:')
    jam_pemberangkatan = input ('Jam Pemberangkatan:')
    jam_pemberhentian = input ('Jam Pemberhentian:')
    no_kursi = int(input ('No kursi:'))
    data = [nama_penumpang,umur_penumpang,kelas_KA,nama_KA,tanggal_pemberangkatan,asal_stasiun,tujuan_stasiun,jam_pemberangkatan,jam_pemberhentian,no_kursi,id_penumpang]
    penumpang.edit(data)
elif (menu2==3):
    id = input ('No Penumpang:')
    data = [id]
    penumpang.search(data)
    confirm = input ('Yakin menghapus penumpang ini?[Y/N]:')
    if (confirm == 'Y'):
        penumpang.delete(data)
    else :
        print ('Tidak jadi menghapus data penumpang!')
elif (menu2==4):
    penumpang.show()
else:
    print('Menu tidak tersedia')

