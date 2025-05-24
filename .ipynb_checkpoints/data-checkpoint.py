import mysql.connector

# Koneksi ke MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_db"
)

if conn.is_connected():
    print("Koneksi ke MySQL berhasil!")

# Tutup koneksi
conn.close()