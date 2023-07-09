# Self Cashier Python
Self Cashier Python adalah program simulasi toko online yang memungkinkan pengguna untuk melakukan pembelian produk dalam berbagai kategori. Program ini juga menghitung total harga belanja dan memberikan potensi diskon. Program ini ditulis dalam bahasa pemrograman Python dan terdiri dari beberapa modul yang bekerja bersama untuk menjalankan fungsionalitasnya.

# Tujuan Pengerjaan Project
1.  Membuat program self cashier sederhana dengan menggunakan bahasa pemrograman Python.
2.  Menerapkan konsep pembuatan modul dan fungsi dalam Python.
3.  Menggunakan objek untuk merepresentasikan pengguna dan kategori produk.
4.  Menghitung total harga belanja dengan potensi diskon berdasarkan total harga belanjaan.
5.  Menggunakan daftar pengguna yang sudah terdaftar sebelumnya untuk login atau membuat akun baru.
6.  Memberikan penggunaan contoh dan penjelasan pada setiap modul.

# Deskripsi Task
1. Module 'init_variable.py' memuat variabel-variabel yang dibutuhkan untuk membuat koneksi ke server dan database di MySQL.
2. Module 'create_db.py' berfungsi untuk membuat koneksi ke server dan database. Dalam module ini juga terdapat function create_tables() untuk membuat tabel-tabel dalam database dan insert_tables() untuk menambahkan data contoh pada tabel-tabel jika diperlukan.
3. Module 'start.py' berfungsi untuk menjalankan program pada module 'create_db.py', yaitu membuat koneksi ke server dan database, serta membuat tabel dan menambahkan data contohnya jika diperlukan.
4. Module 'main.py' berisi daftar menu LMS sederhana.

# Cara Menggunakan Program
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

# Modul yang Digunakan
1. main.py: Modul utama yang menjalankan program self cashier. Berisi fungsi main() sebagai fungsi utama program.
2. modul_account.py: Modul ini berisi fungsi-fungsi terkait akun pengguna seperti login() dan create_account(). Di dalamnya, terdapat kelas User yang digunakan untuk merepresentasikan pengguna.
3. modul_discount.py: Modul ini berisi fungsi calculate_discount() yang digunakan untuk menghitung diskon berdasarkan total harga belanja.
4. modul_item.py: Modul ini berisi definisi kelas Category yang merepresentasikan kategori produk. Modul ini juga menyediakan beberapa kategori produk yang dapat dipilih.
5. existing_users.py: Modul ini berisi daftar pengguna yang sudah terdaftar sebelumnya. Setiap pengguna direpresentasikan oleh objek User

# Hasil Test Case
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

# Saran Perbaikan
1. Mengembangkan program dengan pendekatan berbasis objek, menggunakan class untuk merepresentasikan entitas seperti pengguna, kategori produk, dan item.
2. Menambahkan fitur tambahan, seperti sistem penilaian atau ulasan produk, pilihan pembayaran, atau integrasi dengan sistem inventaris.
3. Melakukan refaktor pada kode untuk meningkatkan kebersihan dan struktur program.
4. Menggunakan mekanisme penyimpanan data yang lebih baik, seperti database atau file untuk menyimpan informasi pengguna, produk, dan transaksi.
5. Mengimplementasikan pengujian otomatis (automated testing) untuk memastikan kestabilan dan kehandalan program.
6. Menerapkan sistem keamanan untuk melindungi data pengguna, seperti enkripsi kata sandi dan validasi input.
