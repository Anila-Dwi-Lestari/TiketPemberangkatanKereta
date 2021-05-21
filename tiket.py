import mysql.connector
import connect
db = connect.koneksi ()
#menambahkan data baru ke dalam tabel tiket
def add (data):
    cursor = db.cursor ()
    sql = """INSERT INTO tiket (nama,hari,tanggal,kelas_KA,nama_KA,no_kursi,jumlah,makan_siang,harga,total)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute (sql,data)
    db.commit ()
    print('{}Data tiket berhasil ditambahkan!'.format(cursor.rowcount))
#menampilkan seluruh data dari tabel tiket
def show ():
    cursor = db.cursor ()
    sql = """SELECT*FROM tiket"""
    cursor.execute(sql)
    results = cursor.fetchall ()
    print ("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print ("|ID|NAMA\t|HARI\t\t|TANGGAL\t|KELAS_KA\t\t|NAMA_KA\t|NO_KURSI\t|JUMLAH\t\t|MAKAN_SIANG\t|HARGA\t\t|TOTAL\t\t|")
    print ("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for data in results :
             print("|",data[0],"|",data[1],"\t|",data[2],"\t|",data[3],"\t|",data[4],"\t|",data[5],"\t|",data[6],"\t\t|",data[7],"\t\t|",data[8],"\t|",data[9],"\t|",data[10],"\t|")
             print ("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#menghapus data dari tabel tiket
def delete(data):
    cursor = db.cursor ()
    sql = """DELETE FROM tiket WHERE id=%s"""
    cursor.execute(sql,data)
    db.commit()
    print ('{}Data tiket berhasil dihapus!'.format (cursor.rowcount))
#mencari data dari tabel tiket
def search (id_tiket):
    cursor = db.cursor()
    sql = """SELECT*FROM tiket WHERE id=%s"""
    cursor.execute(sql,id_tiket)
    results = cursor.fetchall ()
    print ("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print ("|ID|NAMA\t|HARI\t\t|TANGGAL\t|KELAS_KA\t\t|NAMA_KA\t|NO_KURSI\t|JUMLAH\t\t|MAKAN_SIANG\t|HARGA\t\t|TOTAL\t\t|")
    print ("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for data in results :
        print ("|",data[0],"|",data[1],"\t|",data[2],"\t|",data[3],"\t|",data[4],"\t|",data[5],"\t|",data[6],"\t\t|",data[7],"\t\t|",data[8],"\t|",data[9],"\t|",data[10],"\t|")
        print ("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
 
             

             

