# Self Automated Cashier Sumber Makmur
![People Happily 0](https://github.com/ardygfr/ardygfr/assets/135483133/e6cda722-5772-4e3a-ae21-bbcefbe921ab)
### Ilustrasi Toko Sumber Makmur, Dibuat dengan AI https://gencraft.com

## Self Cashier Python
Self Cashier Python adalah program simulasi toko online yang memungkinkan pengguna untuk melakukan pembelian produk dalam berbagai kategori. Program ini juga menghitung total harga belanja dan memberikan potensi diskon. Program ini ditulis dalam bahasa pemrograman Python dan terdiri dari beberapa modul yang bekerja bersama untuk menjalankan fungsionalitasnya.

## Tujuan Pengerjaan Project
1.  Membuat program self cashier sederhana dengan menggunakan bahasa pemrograman Python.
2.  Menerapkan konsep pembuatan modul dan fungsi dalam Python.
3.  Menggunakan objek untuk merepresentasikan pengguna dan kategori produk.
4.  Menghitung total harga belanja dengan potensi diskon berdasarkan total harga belanjaan.
5.  Menggunakan daftar pengguna yang sudah terdaftar sebelumnya untuk login atau membuat akun baru.
6.  Memberikan penggunaan contoh dan penjelasan pada setiap modul.

## Flowchart / Tabel Alur
![Super Cashier Flow Chart_page-0001](https://github.com/ardygfr/ardygfr/assets/135483133/adb24537-4551-4568-8227-c9ef8a8fabfc)
### Gambar Tabel Alur Proses Pembelanjaan di Toko Sumber Makmur

# Technical explain

proyek ini terdiri dari 2 file yaitu main.py dan modul.py yang masing-masing memiliki kegunaan.
- file main.py digunakan sebagai file utama untuk menjalankan program *super cashier* dan hanya berisi object dari class Transaction.
- file modul.py digunakan sebagai modul yang berisi *class, function dan attributes*. penjelasan dari isi file sebagai berikut:

```
from modul_account import login, create_account
from modul_discount import calculate_discount
from modul_item import (
    Category,
    food_category,
    toys_category,
    toiletries_category,
    beverages_category,
    electricals_category,
    clothing_category
)
from existing_users import existing_users

"""
Susunan Kode untuk memanggil modul-modul yang ada
"""
```


```
class Transaction:
    """
    Sebuah class untuk kasir self-service disupermarket

    ...

    Attributes
    ----------
    id_transaksi : int
        id_transaksi berjenis input untuk hasil transaksi customer
    data_all_item : dict
        data_all_item adalah tempat penyimpanan data order transaksi yang berhasil diinput oleh customer kedalam sistem
    """

    data_all_item = {"Nama item": [], "Jumlah item": [], "Harga per item": [], "Total Harga": []}
```

```
def __init__(self):
    """
    Constructor untuk sebuah class Transaction

    Parameters
    ----------
    Tidak terdapat parameter pada fungsi Constructor

    Attributes
    ----------
    id_transaksi : int
      id_transaksi berjenis input untuk hasil transaksi customer
    """

    print("<-----------------Welcome to Super Cashier----------------->")
    while 1:
      try:
          id_transaksi = int(input("Masukkan ID Transaksi anda: "))
          print("ID Transaksi anda {}".format(id_transaksi))
          print("\n")
          break
      except ValueError:
          print("ID Transaksi tidak valid!")
          continue
    while 1:
      print("<-----------------------list perintah----------------------->")
      print("- tambah order transaksi ketik: add_item")
      print("- ubah nama item order transaksi ketik: update_item_name")
      print("- ubah jumlah item order transaksi ketik: update_item_qty")
      print("- ubah harga per item order transaksi ketik: update_item_price")
      print("- validasi order transaksi ketik: check_order_item")
      print("- hapus salah satu order transaksi ketik: delete_item")
      print("- hapus seluruh order transaksi ketik: reset_transaction")
      print("- tampilkan biaya untuk seluruh order transaksi ketik: total_price")
      print("- keluar dari program ketik: keluar")
      print("\n")
      perlu = input("Masukkan perintah sesuai keperluan: ")
      if perlu.lower() == "add_item":
          self.add_item()
          print("\n")
      elif perlu.lower() == "update_item_name":
          self.update_item_name()
          print("\n")
      elif perlu.lower() == "update_item_qty":
          self.update_item_qty()
          print("\n")
      elif perlu.lower() == "update_item_price":
          self.update_item_price()
          print("\n")
      elif perlu.lower() == "check_order_item":
          self.check_order_item()
          print("\n")
      elif perlu.lower() == "delete_item":
          self.delete_item()
          print("\n")
      elif perlu.lower() == "reset_transaction":
          self.reset_transaction()
          print("\n")
      elif perlu.lower() == "total_price":
          self.total_price()
          print("\n")
      elif perlu.lower() == "keluar":
          # break
          os._exit(0)
      else:
          print("Mohon masukkan perintah dengan benar dan sesuai!")
          print("\n")
```

```
def add_item(self):
  """
  Sebuah fungsi untuk menambahkan item baru kedalam keranjang

  Parameters
  ----------
  Tidak terdapat parameter pada fungsi add_item

  Attributes
  ----------
  nama_item : str
      nama_item berjenis input untuk nama item yang dimasukkan kedalam keranjang
  jumlah_item : int
      jumlah_item berjenis input untuk jumlah item yang dimasukkan kedalam keranjang
  harga : int
      harga berjenis input untuk harga per item yang dimasukkan kedalam keranjang
  total_harga : int
      Penghitung total_harga dengan melakukan perkalian terhadap jumlah item dan harga per item

  Return
  ------
  Menyimpan seluruh data yang berhasil diinput oleh customer kedalam database
  """

  nama_item = input("Nama item yang dibeli: ")

  while 1:
      try:
          jumlah_item = int(input("Jumlah item yang dibeli: "))
          break
      except ValueError:
          print("Input berupa angka!")
          continue

  while 1:
      try:
          harga = int(input("Harga per item yang dibeli: "))
          break
      except ValueError:
          print("Input berupa angka!")
          continue

  self.data_all_item["Nama item"].append(nama_item)
  self.data_all_item["Jumlah item"].append(jumlah_item)
  self.data_all_item["Harga per item"].append(harga)
  self.data_all_item["Total Harga"].append(jumlah_item * harga)
```

```
def update_item_name(self):
  """
  Sebuah fungsi untuk mengubah data nama item pada order transaksi yang telah diinput oleh customer

  Parameters
  ----------
  Tidak terdapat parameter pada fungsi update_item_name

  Attributes
  ----------
  nama_item : str
      nama_item berjenis input untuk nama item yang ingin dilakukan perubahan pada nama item
  update_nama_item : int
      update_nama_item berjenis input untuk nama item terbaru
  idx_item : int
      idx_item untuk menyimpan posisi index dari nama item yang customer input

  Return
  ------
  Menyimpan seluruh data perubahan pada nama item yang berhasil diinput oleh customer kedalam database
  """

  while 1:
      nama_item = input("Nama item sebelum diubah: ")

      if nama_item in self.data_all_item.get("Nama item"):
          update_nama_item = input("Update nama item yang ingin diubah: ")
          idx_item = self.data_all_item['Nama item'].index(nama_item)
          self.data_all_item['Nama item'][idx_item] = update_nama_item
          print("Berhasil dirubah!")
          break

      else:
          print("Tidak terdapat nama item tersebut!")
```

```
def update_item_qty(self):
  """
  Sebuah fungsi untuk mengubah data jumlah item pada order transaksi yang telah diinput oleh customer

  Parameters
  ----------
  Tidak terdapat parameter pada fungsi update_item_qty

  Attributes
  ----------
  nama_item : str
      nama_item berjenis input untuk nama item yang ingin dilakukan perubahan pada jumlah item
  update_jumlah_item : int
      update_jumlah_item berjenis input untuk jumlah item terbaru
  idx_item : int
      idx_item untuk menyimpan posisi index dari nama item yang customer input

  Return
  ------
  Menyimpan seluruh data perubahan pada jumlah item yang berhasil diinput oleh customer kedalam database
  """

  while 1:
      nama_item = input("Nama item yang ingin diubah: ")

      if nama_item in self.data_all_item.get("Nama item"):
          while 1:
              try:
                  update_jumlah_item = int(input("Update jumlah item yang dibeli: "))
                  break
              except ValueError:
                  print("Input berupa angka!")
                  continue
          idx_item = self.data_all_item['Nama item'].index(nama_item)
          self.data_all_item['Jumlah item'][idx_item] = update_jumlah_item

          self.data_all_item["Total Harga"][idx_item] = (
                      update_jumlah_item * self.data_all_item["Harga per item"][idx_item])

          print("Berhasil dirubah!")
          break

      else:
          print("Tidak terdapat nama item tersebut!")
```

```
def update_item_price(self):
  """
  Sebuah fungsi untuk mengubah data harga per item pada order transaksi yang telah diinput oleh customer

  Parameters
  ----------
  Tidak terdapat parameter pada fungsi update_item_price

  Attributes
  ----------
  nama_item : str
      nama_item berjenis input untuk nama item yang ingin dilakukan perubahan pada harga per item
  update_harga_item : int
      update_harga_item berjenis input untuk harga per item terbaru
  idx_item : int
      idx_item untuk menyimpan posisi index dari nama item yang customer input

  Return
  ------
  Menyimpan seluruh data perubahan pada harga per item yang berhasil diinput oleh customer kedalam database
  """

  while 1:
      nama_item = input("Nama item yang ingin diubah: ")

      if nama_item in self.data_all_item.get("Nama item"):
          while 1:
              try:
                  update_harga_item = int(input("Update harga per item yang dibeli: "))
                  break
              except ValueError:
                  print("Input berupa angka!")
                  continue
          idx_item = self.data_all_item['Nama item'].index(nama_item)
          self.data_all_item['Harga per item'][idx_item] = update_harga_item

          self.data_all_item["Total Harga"][idx_item] = (
                      update_harga_item * self.data_all_item["Jumlah item"][idx_item])

          print("Berhasil dirubah!")
          break

      else:
          print("Tidak terdapat nama item tersebut!")
```

```
def check_order_item(self):
  """
  Sebuah fungsi untuk melihat apakah terdapat kesalahan penginputan data pada transaksi

  Parameters
  ----------
  Tidak terdapat parameter pada fungsi check_order_item

  Attributes
  ----------
  df : dataframe
      df digunakan untuk menampilkan data-data order transaksi dalam bentuk dataframe atau tabular

  Return
  ------
  Menampilkan apakah terdapat kesalahan dalam penginputan data pada transaksi dan data yang berhasil diinput oleh customer
  """

  if not any(self.data_all_item.values()):
      print("Tidak ada data transaksi!")
  elif '' in self.data_all_item['Nama item']:
      print("Mohon mengisi nama item yang kosong!")
      print("<--------List order item-------->")
      df = pd.DataFrame(self.data_all_item)
      print(df)
  else:
      print("Data transaksi sudah benar!")
      print("<--------List order item-------->")
      df = pd.DataFrame(self.data_all_item)
      print(df)
```

```
def delete_item(self):
  """
  Sebuah fungsi untuk menghapus salah satu item yang berhasil diinput oleh customer pada transaksi

  Parameters
  ----------
  Tidak terdapat parameter pada fungsi delete_item

  Attributes
  ----------
  nama_item : str
      nama_item berjenis input untuk nama item yang ingin dilakukan penghapusan order transaksi
  df : dataframe
      df digunakan untuk menampilkan data-data order transaksi dalam bentuk dataframe atau tabular
  idx_item : int
      idx_item untuk menyimpan posisi index dari nama item yang customer input

  Return
  ------
  Menghapus salah satu order transaksi pada data database
  """

  while 1:
      nama_item = input("Nama item yang ingin dihapus: ")

      if nama_item in self.data_all_item.get("Nama item"):
          idx_item = self.data_all_item['Nama item'].index(nama_item)
          for key in list(self.data_all_item.keys()):
              del self.data_all_item[key][idx_item]

          print("Berhasil dihapus!")
          if not any(self.data_all_item.values()):
              print("Tidak ada data transaksi!")
          else:
              df = pd.DataFrame(self.data_all_item)
              print(df)
          break

      else:
          print("Tidak terdapat nama item tersebut!")
```

```
def reset_transaction(self):
  """
  Sebuah fungsi untuk menghapus seluruh item yang berhasil diinput oleh customer pada transaksi

  Parameters
  ----------
  Tidak terdapat parameter pada fungsi reset_transaction

  Attributes
  ----------
  Tidak terdapat attribute pada fungsi reset_transaction

  Return
  ------
  Menghapus seluruh order transaksi pada data database
  """

  for key in list(self.data_all_item.keys()):
      del self.data_all_item[key][:]

  print("Berhasil menghapus seluruh transaksi!")
```

```
def total_price(self):
  """
  Sebuah fungsi untuk menghitung total biaya yang harus dibayarkan customer dari item-item pada data transaksi

  Parameters
  ----------
  Tidak terdapat parameter pada fungsi total_price

  Attributes
  ----------
  df : dataframe
      df digunakan untuk menampilkan data-data order transaksi dalam bentuk dataframe atau tabular

  Return
  ------
  Menampilkan total biaya yang harus dibayar oleh customer tersebut dengan beberapa kriteria yaitu
  - diatas Rp. 500.000 akan mendapatkan potongan biaya sebesar 10% dari total biaya yang harus dibayarkan
  - diatas Rp. 300.000 akan mendapatkan potongan biaya sebesar 8% dari total biaya yang harus dibayarkan
  - diatas Rp. 200.000 akan mendapatkan potongan biaya sebesar 5% dari total biaya yang harus dibayarkan
  """

  if not any(self.data_all_item.values()):
      print("Tidak ada data transaksi!")
  else:
      df = pd.DataFrame(self.data_all_item)
      print(df)
      if sum(self.data_all_item["Total Harga"]) > 500000:
          print("Sebelum mendapatkan diskon 10%: Rp.{}".format(sum(self.data_all_item["Total Harga"])))
          print("Setelah mendapatkan diskon 10%: Rp.{}".format(
              int(sum(self.data_all_item["Total Harga"]) - (sum(self.data_all_item["Total Harga"]) * 0.10))))
      elif sum(self.data_all_item["Total Harga"]) > 300000:
          print("Sebelum mendapatkan diskon 8%: Rp.{}".format(sum(self.data_all_item["Total Harga"])))
          print("Setelah mendapatkan diskon 8%: Rp.{}".format(
              sum(int(self.data_all_item["Total Harga"]) - (sum(self.data_all_item["Total Harga"]) * 0.08))))
      elif sum(self.data_all_item["Total Harga"]) > 200000:
          print("Sebelum mendapatkan diskon 5%: Rp.{}".format(sum(self.data_all_item["Total Harga"])))
          print("Setelah mendapatkan diskon 5%: Rp.{}".format(
              sum(int(self.data_all_item['Total Harga']) - (sum(self.data_all_item["Total Harga"]) * 0.0
```

## Deskripsi Task
1. Module 'init_variable.py' memuat variabel-variabel yang dibutuhkan untuk membuat koneksi ke server dan database di MySQL.
2. Module 'create_db.py' berfungsi untuk membuat koneksi ke server dan database. Dalam module ini juga terdapat function create_tables() untuk membuat tabel-tabel dalam database dan insert_tables() untuk menambahkan data contoh pada tabel-tabel jika diperlukan.
3. Module 'start.py' berfungsi untuk menjalankan program pada module 'create_db.py', yaitu membuat koneksi ke server dan database, serta membuat tabel dan menambahkan data contohnya jika diperlukan.
4. Module 'main.py' berisi daftar menu LMS sederhana.

## Cara Menggunakan Program
1. Pastikan Anda memiliki Python versi 3.x terpasang di sistem Anda.
2. Unduh semua file modul Python yang diperlukan ke dalam satu direktori lokal.
3. Buka terminal dan arahkan ke direktori lokal di mana file modul Python disimpan.
4. Jalankan perintah python main.py di terminal untuk menjalankan program.
5. Program akan memulai dan menampilkan pesan selamat datang di Sumber Makmur Super General Store.
6. Jawab pertanyaan apakah Anda sudah memiliki akun atau tidak dengan "YA" atau "TIDAK".
7. Jika Anda sudah memiliki akun, Anda akan diminta untuk login dengan memasukkan email atau username Anda.
8. Jika Anda belum memiliki akun dan ingin membuat akun baru, Anda akan diminta untuk memasukkan informasi yang diperlukan.
9. Setelah berhasil login atau membuat akun, Anda dapat memilih kategori produk dan item yang ingin dibeli.
10. Anda dapat memilih item, mengatur jumlah item, atau membatalkan item dari keranjang belanja.
11. Setelah selesai berbelanja, program akan mencetak rincian belanjaan Anda, total harga, diskon yang diberikan, dan total harga setelah diskon.
12. Program akan mengucapkan terima kasih dan mengakhiri eksekusi.

## Modul yang Digunakan
1. main.py: Modul utama yang menjalankan program self cashier. Berisi fungsi main() sebagai fungsi utama program.
2. modul_account.py: Modul ini berisi fungsi-fungsi terkait akun pengguna seperti login() dan create_account(). Di dalamnya, terdapat kelas User yang digunakan untuk merepresentasikan pengguna.
3. modul_discount.py: Modul ini berisi fungsi calculate_discount() yang digunakan untuk menghitung diskon berdasarkan total harga belanja.
4. modul_item.py: Modul ini berisi definisi kelas Category yang merepresentasikan kategori produk. Modul ini juga menyediakan beberapa kategori produk yang dapat dipilih.
5. existing_users.py: Modul ini berisi daftar pengguna yang sudah terdaftar sebelumnya. Setiap pengguna direpresentasikan oleh objek User

## Hasil Test Case
1. Pendaftaran Anggota Baru

    - Penambahan Data Anggota Baru

    ![1 Pendaftaran Anggota Baru](https://user-images.githubusercontent.com/109220639/180597034-aa853286-f291-4ca3-9633-ca7678568647.jpg)

    - Menampilkan Daftar Anggota Setelah Pendaftaran

    ![4 Tampilkan Daftar Anggota](https://user-images.githubusercontent.com/109220639/180597039-0df64db9-625c-44b8-8da7-661a3f932c59.jpg)

2. Pendaftaran Buku

    - Penambahan Data Buku Baru
    
    ![2 Pendaftaran Buku Baru](https://user-images.githubusercontent.com/109220639/180597228-5fc20b1d-7ebf-4e59-87bd-0c4b66c94434.jpeg)
    
    - Menampilkan Daftar Buku 
    
    ![5 Tampilkan Daftar Buku](https://user-images.githubusercontent.com/109220639/180597232-f9d7f8bb-e7b8-46d4-b91c-fad65f0f1854.jpeg)
    
3. Peminjaman Buku

    - Melakukan Peminjaman
    
    ![3 Peminjaman Buku](https://user-images.githubusercontent.com/109220639/180597274-acfcaa86-c65c-4117-b098-6297c6168ee4.jpeg)

    - Menampilkan Daftar Peminjaman
    
    ![6 Tampilkan Daftar Peminjaman](https://user-images.githubusercontent.com/109220639/180597280-6e9efba5-21bf-478a-a628-1074b42eb456.jpeg)

    - Menampilkan Daftar Buku Setelah Peminjaman (stok berkurang 1)
    
    ![Daftar Buku Setelah Peminjaman](https://user-images.githubusercontent.com/109220639/180597288-40e27e4d-d0f4-444e-87fc-2ce4ffff80c9.jpeg)

4. Pengembalian Buku

    - Melakukan Pengembalian 
    
    ![7 Pengembalian Buku](https://user-images.githubusercontent.com/109220639/180597304-0e910549-f768-4b80-a928-9fde3301a662.jpeg)

    - Menampilkan Daftar Peminjaman (data peminjaman terhapus)
    
    ![Daftar Peminjaman Setelah Pengembalian](https://user-images.githubusercontent.com/109220639/180597312-4c24b1e7-5e36-475e-9c15-4d5a992eed73.jpeg)

    - Menampilkan Daftar Buku Setelah Pengembalian (stok terupdate)
    
    ![Daftar Buku Setelah Pengembalian](https://user-images.githubusercontent.com/109220639/180597320-f2c31016-1e1f-4f3c-b352-81b746a481c9.jpeg)

5. Meampilkan Hasil Pencarian Judul Buku

![Pencarian Judul Buku](https://user-images.githubusercontent.com/109220639/180597323-2f7313e6-e67f-4772-9f4c-2a18248625b6.jpeg)

## Saran Perbaikan
1. Mengembangkan program dengan pendekatan berbasis objek, menggunakan class untuk merepresentasikan entitas seperti pengguna, kategori produk, dan item.
2. Menambahkan fitur tambahan, seperti sistem penilaian atau ulasan produk, pilihan pembayaran, atau integrasi dengan sistem inventaris.
3. Melakukan refaktor pada kode untuk meningkatkan kebersihan dan struktur program.
4. Menggunakan mekanisme penyimpanan data yang lebih baik, seperti database atau file untuk menyimpan informasi pengguna, produk, dan transaksi.
5. Mengimplementasikan pengujian otomatis (automated testing) untuk memastikan kestabilan dan kehandalan program.
6. Menerapkan sistem keamanan untuk melindungi data pengguna, seperti enkripsi kata sandi dan validasi input.
