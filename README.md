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

## Penjelasan Keteknisan
Program Self Automated Cashier Toko Sumber Makmur menggunakan beberapa modul sekaligus seperti yang dijelaskan pada penjelasan sebelumnya. Maka dari itu kita akan merunutkan penjelasan keteknisan pada project ini.
###  Main.py

```python
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
```

Kode di atas mengimpor fungsi `login` dan `create_account` dari modul `modul_account`, fungsi `calculate_discount` dari modul `modul_discount`, serta kelas `Category` dan kategori-kategori item dari modul `modul_item`. Selain itu, juga mengimpor variabel `existing_users` dari modul `existing_users`.

```python
def main():
    print("Selamat datang di Sumber Makmur Super General Store!")
    print("===============================================")
    
    # Bagian lain dari program

if __name__ == "__main__":
    main()
```

Kode di atas mendefinisikan fungsi `main()` sebagai fungsi utama yang akan dijalankan ketika file ini dieksekusi. Di dalam fungsi `main()`, pesan selamat datang dicetak, dan kemudian bagian lain dari program dijalankan. Juga terdapat pengecekan apakah file ini dieksekusi langsung dengan `__name__ == "__main__"`, yang berarti kode di dalam blok tersebut hanya akan dijalankan jika file ini dieksekusi langsung, bukan diimpor oleh file lain.

### modul_account.py
Tentu, berikut adalah penjelasan per segmen untuk modul `modul_account`:

**Import Daftar Pengguna yang Ada:**
```python
from existing_users import existing_users
```
Pada bagian ini, modul `existing_users` diimpor untuk mendapatkan akses ke daftar pengguna yang sudah ada.

**Deklarasi Class `User`:**
```python
class User:
    def __init__(self, name, username, account_duration, email, has_account, referral_code=None):
        self.name = name
        self.username = username
        self.account_duration = account_duration
        self.email = email
        self.has_account = has_account
        self.referral_code = referral_code
```
Segmen ini mendefinisikan class `User` yang memiliki atribut sebagai berikut:
- `name`: Nama lengkap pengguna.
- `username`: Nama pengguna (username) pengguna.
- `account_duration`: Durasi akun pengguna.
- `email`: Email pengguna.
- `has_account`: Menandakan apakah pengguna memiliki akun.
- `referral_code`: Kode referral pengguna (opsional).

**Fungsi `login()`:**
```python
def login():
    username_email = input("Silahkan masukkan email atau username Anda: ")
    while True:
        existing_user = next(
            (user for user in existing_users if user.username == username_email or user.email == username_email), None
        )
        if existing_user is not None:
            print("Selamat datang, " + existing_user.name + "!")
            return existing_user
        create_account = input("Akun tidak ditemukan. Apakah Anda sudah memiliki akun Sumber Makmur? (YA/TIDAK) ")
        if create_account.upper() != "YA":
            print("Login gagal. Silakan ulangi proses dari awal.")
            return None
        username_email = input("Silahkan masukkan email atau username Anda: ")
    return None
```
Fungsi `login()` digunakan untuk melakukan proses login pengguna. Pada bagian ini, langkah-langkah yang dilakukan adalah sebagai berikut:
1. Pengguna diminta untuk memasukkan email atau username mereka.
2. Fungsi mencari pengguna yang memiliki email atau username yang sesuai dengan yang dimasukkan oleh pengguna.
3. Jika pengguna ditemukan, pesan selamat datang akan dicetak dengan mencantumkan nama pengguna yang sesuai. Fungsi akan mengembalikan objek pengguna yang sesuai.
4. Jika pengguna tidak ditemukan, pengguna akan diminta apakah mereka sudah memiliki akun di Sumber Makmur.
5. Jika pengguna tidak memiliki akun, fungsi akan mencetak pesan login gagal dan mengembalikan `None`.
6. Jika pengguna ingin membuat akun, fungsi akan meminta pengguna untuk memasukkan email atau username mereka lagi.
7. Fungsi akan terus meminta masukan hingga pengguna berhasil login atau memilih untuk membuat akun.
8. Fungsi akan mengembalikan `None` jika login gagal.

**Fungsi `create_account()`:**
```python
def create_account():
    full_name = input("Masukkan Nama Lengkap Anda: ")
    valid_email = False
    while not valid_email:
        email = input("Masukkan email Anda: ")
        if "@" in email and "." in email:
            valid_email = True
        else:
            print("Tolong masukkan email yang benar!")
    valid_username = False
    while not valid_username:
        username = input("Masukkan nama akun Anda! Gunakan 6-10 karakter yang mengandung angka dan huruf: ")
        if len(username) >= 6 and len(username) <= 10 and username.isalnum():
            username_exists = False
            for user in existing_users:
                if user.username == username:
                    username_exists = True
                    break
            if username_exists:
                print("Username sudah ada! Mohon buat username lainnya!")
            else:
                valid_username = True
        else:
            print("Mohon gunakan 6-10 karakter yang mengandung angka dan huruf saja untuk username Anda!")
    print("Akun Anda berhasil dibuat! Selamat berbelanja, " + full_name + "!")
    new_user = User(full_name, username, None, email, True)
    existing_users.append(new_user)
    return new_user
```
Fungsi `create_account()` digunakan untuk membuat akun baru. Langkah-langkah yang dilakukan adalah sebagai berikut:
1. Pengguna diminta untuk memasukkan nama lengkap dan email.
2. Fungsi memvalidasi email yang dimasukkan oleh pengguna. Jika email tidak valid (tidak mengandung "@" dan "."), pesan error akan dicetak dan pengguna diminta memasukkan email kembali.
3. Pengguna juga diminta untuk memasukkan nama pengguna (username). Fungsi akan memvalidasi nama pengguna dengan memastikan bahwa nama pengguna memiliki panjang antara 6 hingga 10 karakter dan hanya terdiri dari huruf dan angka.
4. Fungsi akan memeriksa keberadaan nama pengguna dalam daftar `existing_users`. Jika nama pengguna sudah ada, pesan error akan dicetak dan pengguna diminta untuk memilih nama pengguna lainnya.
5. Jika nama pengguna valid dan unik, fungsi akan mencetak pesan sukses pembuatan akun dan mengembalikan objek `User` yang baru dibuat.
6. Objek `User` baru akan ditambahkan ke daftar `existing_users`.

 ### modul_discount.py

1. Import Modul

```python
from modul_discount import calculate_discount
```

Pada bagian ini, modul `modul_discount` diimpor ke dalam file yang sedang digunakan agar fungsi `calculate_discount` dapat digunakan.

2. Fungsi `calculate_discount`

```python
def calculate_discount(total_price, cashback=0):
    """
    Fungsi ini digunakan untuk menghitung diskon dan harga setelah diskon dari total harga pembelian.

    Parameters:
        - total_price (float): Total harga pembelian sebelum diskon.
        - cashback (float, optional): Jumlah cashback yang diberikan. Default: 0.

    Returns:
        - discounted_price (float): Total harga setelah diskon.
        - discount_amount (float): Jumlah diskon yang diberikan.

    """
    if total_price > 500000:
        discount = 0.1
    elif total_price > 300000:
        discount = 0.08
    elif total_price > 200000:
        discount = 0.05
    else:
        discount = 0

    discount_amount = total_price * discount
    discounted_price = total_price - discount_amount - cashback

    return discounted_price, discount_amount
```

Fungsi `calculate_discount` digunakan untuk menghitung diskon dan harga setelah diskon dari total harga pembelian. Fungsi ini memiliki dua parameter: `total_price` dan `cashback`.

- `total_price` adalah total harga pembelian sebelum diskon. Parameter ini bertipe data float.
- `cashback` adalah jumlah cashback yang diberikan. Parameter ini bersifat opsional dan memiliki nilai default 0. Parameter ini juga bertipe data float.

Fungsi ini mengembalikan dua nilai:
- `discounted_price` adalah total harga setelah diskon. Nilai ini bertipe data float.
- `discount_amount` adalah jumlah diskon yang diberikan. Nilai ini bertipe data float.

Fungsi ini menggunakan beberapa kondisi untuk menentukan jumlah diskon yang diberikan. Jika `total_price` melebihi 500.000, diskon sebesar 10% diberikan. Jika `total_price` melebihi 300.000, diskon sebesar 8% diberikan. Jika `total_price` melebihi 200.000, diskon sebesar 5% diberikan. Jika `total_price` tidak memenuhi kondisi-kondisi tersebut, maka tidak ada diskon yang diberikan.

Setelah menghitung jumlah diskon, fungsi ini menghitung harga setelah diskon dengan mengurangi jumlah diskon dan cashback dari total harga pembelian.

Kembali ke [main.py](./main.py).

## Deskripsi Task
1. Module 'init_variable.py' memuat variabel-variabel yang dibutuhkan untuk membuat koneksi ke server dan database di MySQL.
2. Module 'create_db.py' berfungsi untuk membuat koneksi ke server dan database. Dalam module ini juga terdapat function create_tables() untuk membuat tabel-tabel dalam database dan insert_tables() untuk menambahkan data contoh pada tabel-tabel jika diperlukan.
3. Module 'start.py' berfungsi untuk menjalankan program pada module 'create_db.py', yaitu membuat koneksi ke server dan database, serta membuat tabel dan menambahkan data contohnya jika diperlukan.
4. Module 'main.py' berisi daftar menu LMS sederhana.

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
