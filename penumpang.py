import mysql.connector
import connect
db = connect.koneksi ()

#menambahkan data baru ke dalam tabel penumpang
def add (data):
    cursor = db.cursor ()
    sql = """INSERT INTO penumpang (nama_penumpang,umur_penumpang,kelas_KA,nama_KA,tanggal_pemberangkatan,asal_stasiun,tujuan_stasiun,jam_pemberangkatan,jam_pemberhentian,no_kursi)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute (sql,data)
    db.commit ()
    print('{}Data penumpang berhasil ditambahkan!'.format(cursor.rowcount))

    
#menampilkan seluruh data dari tabel penumpang
def show ():
    cursor = db.cursor ()
    sql = """SELECT*FROM penumpang"""
    cursor.execute(sql)
    results = cursor.fetchall ()
    print ("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print ("|ID|NAMA\t|UMUR PENUMPANG\t|KELAS KA\t|NAMA KA\t|TANGGAL PEMBERANGKATAN\t|ASAL STASIUN\t|TUJUAN STASIUN\t|JAM BERANGKAT\t|JAM BERHENTI\t|NO KURSI|")
    print ("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for data in results :
             print("|",data[0],"|",data[1],"\t|",data[2],"\t\t|",data[3],"\t|",data[4],"\t|",data[5],"\t|",data[6],"\t|",data[7],"\t\t|",data[8],"\t|",data[9],"\t\t|",data[10],"|")
             print ("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

             
#mengubah data per record berdasarkan id pada tabel penumpang
def edit (data):
    cursor = db.cursor ()
    sql = """UPDATE penumpang SET nama_penumpang=%s,umur_penumpang=%s,kelas_KA=%s,nama_KA=%s,tanggal_pemberangkatan=%s,asal_stasiun=%s,tujuan_stasiun=%s,jam_pemberangkatan=%s,jam_pemberhentian=%s,no_kursi=%s WHERE id=%s"""
    cursor.execute(sql,data)
    db.commit ()
    print ('{}Data penumpang berhasil diubah!'.format (cursor.rowcount))

    
#menghapus data dari tabel penumpang
def delete(data):
    cursor = db.cursor ()
    sql = """DELETE FROM penumpang WHERE id=%s"""
    cursor.execute(sql,data)
    db.commit()
    print ('{}Data penumpang berhasil dihapus!'.format (cursor.rowcount))

    
#mencari data dari tabel penumpang
def search (id):
    cursor = db.cursor()
    sql = """SELECT*FROM penumpang WHERE id=%s"""
    cursor.execute(sql,id)
    results = cursor.fetchall ()
    print ("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print ("|ID|NAMA PENUMPANG\t|UMUR PENUMPANG\t|KELAS KA\t|NAMA KA\t|TANGGAL PEMBERANGKATAN\t|ASAL STASIUN\t|TUJUAN STASIUN\t|JAM PEMBERANGKATAN\t|JAM PEMBERHENTIAN\t|NO KURSI\t|")
    print ("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for data in results :
        print ("|",data[0],"\t|",data[1],"\t|",data[2],"\t|",data[3],"\t|",data[4],"\t|",data[5],"\t|",data[6],"\t|",data[7],"\t|",data[8],"\t|",data[9],"\t|",data[10],"\t|")
        print ("------------------------------------------------------------------------------------------------------------------------------------------------------------")
 
             

             

