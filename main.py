import mysql.connector

# Fungsi koneksi ke database
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="toko_db"
    )

# Fungsi tambah produk
def tambah_produk():
    conn = connect()
    cursor = conn.cursor()

    nama = input("Nama Produk: ")
    harga = float(input("Harga: "))
    stok = int(input("Stok: "))
    deskripsi = input("Deskripsi: ")

    sql = "INSERT INTO produk (nama_produk, harga, stok, deskripsi) VALUES (%s, %s, %s, %s)"
    val = (nama, harga, stok, deskripsi)
    cursor.execute(sql, val)

    conn.commit()
    print("Produk berhasil ditambahkan!")

    cursor.close()
    conn.close()

# Fungsi lihat produk
def lihat_produk():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produk")
    hasil = cursor.fetchall()

    print("\n Daftar Produk:")
    for row in hasil:
        print(f"ID: {row[0]} | Nama: {row[1]} | Harga: {row[2]} | Stok: {row[3]} | Deskripsi: {row[4]}")

    cursor.close()
    conn.close()

# Fungsi update produk
def update_produk():
    conn = connect()
    cursor = conn.cursor()

    id_produk = input("Masukkan ID produk yang akan diupdate: ")
    nama = input("Nama baru: ")
    harga = float(input("Harga baru: "))
    stok = int(input("Stok baru: "))
    deskripsi = input("Deskripsi baru: ")

    sql = "UPDATE produk SET nama_produk=%s, harga=%s, stok=%s, deskripsi=%s WHERE id=%s"
    val = (nama, harga, stok, deskripsi, id_produk)
    cursor.execute(sql, val)

    conn.commit()
    print("Produk berhasil diperbarui!")

    cursor.close()
    conn.close()

# Fungsi hapus produk
def hapus_produk():
    conn = connect()
    cursor = conn.cursor()

    id_produk = input("Masukkan ID produk yang akan dihapus: ")

    sql = "DELETE FROM produk WHERE id=%s"
    val = (id_produk,)
    cursor.execute(sql, val)

    conn.commit()
    print("Produk berhasil dihapus!")

    cursor.close()
    conn.close()

# Menu utama
def menu():
    while True:
        print("\n=== SISTEM CRUD PRODUK TOKO ===")
        print("1. Tambah Produk")
        print("2. Lihat Produk")
        print("3. Update Produk")
        print("4. Hapus Produk")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_produk()
        elif pilihan == "2":
            lihat_produk()
        elif pilihan == "3":
            update_produk()
        elif pilihan == "4":
            hapus_produk()
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program
if __name__ == "__main__":
    menu()
    
