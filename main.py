#!/usr/bin/env python
# coding: utf-8

# In[39]:


from existing_users import existing_users
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


class User:
    def __init__(self, name, username, account_duration, email, has_account, referral_code=None):
        self.name = name
        self.username = username
        self.account_duration = account_duration
        self.email = email
        self.has_account = has_account
        self.referral_code = referral_code


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


def main():
    print("Selamat datang di Sumber Makmur Super General Store!")
    print("===============================================")

    answer = input("Apakah Anda sudah memiliki akun Sumber Makmur? (YA/TIDAK) ")

    existing_user = None

    if answer.upper() == "YA":
        existing_user = login()

    if existing_user is None:
        create_account_choice = input("Apa Anda ingin membuat akun Sumber Makmur? (YA/TIDAK) ")
        if create_account_choice.upper() == "YA":
            new_user = create_account()
            existing_user = new_user
            print("Selamat datang, " + existing_user.name + "!")

    if existing_user:
        # Shopping Cart
        shopping_cart = []

        while True:
            display_categories()

            category_choice = int(input("Silahkan pilih kategori yang Anda inginkan (1-6) atau 0 untuk selesai: "))

            if category_choice == 0:
                break

            selected_category = None

            if category_choice == 1:
                selected_category = food_category
            elif category_choice == 2:
                selected_category = toys_category
            elif category_choice == 3:
                selected_category = toiletries_category
            elif category_choice == 4:
                selected_category = beverages_category
            elif category_choice == 5:
                selected_category = electricals_category
            elif category_choice == 6:
                selected_category = clothing_category
            else:
                print("Pilihan kategori tidak valid. Silakan pilih kembali.")
                continue

            print("Anda telah memilih kategori " + selected_category.name + ". Berikut adalah daftar item yang tersedia:")

            for i, item in enumerate(selected_category.get_items(), 1):
                print(str(i) + ". " + item[0] + " - Rp" + str(item[1]))

            while True:
                item_choice = int(input("Silahkan pilih item yang ingin Anda beli (1-" + str(len(selected_category.items)) + ") atau 0 untuk selesai: "))

                if item_choice == 0:
                    break

                if item_choice < 1 or item_choice > len(selected_category.items):
                    print("Pilihan item tidak valid. Silakan pilih kembali.")
                    continue

                selected_item = selected_category.items[item_choice - 1]
                item_name = selected_item[0]
                item_price = selected_item[1]
                while True:
                    try:
                        item_quantity = int(input("Masukkan jumlah " + item_name + " yang ingin Anda beli: "))
                        if item_quantity <= 0:
                            print("Jumlah harus lebih besar dari 0. Silakan masukkan kembali.")
                            continue
                        break
                    except ValueError:
                        print("Jumlah harus berupa bilangan bulat. Silakan masukkan kembali.")

                shopping_cart.append((item_name, item_price, item_quantity))

                print("Item " + item_name + " sebanyak " + str(item_quantity) + " buah dengan harga Rp" + str(item_price * item_quantity) + " ditambahkan ke keranjang belanja.")

                while True:
                    action_choice = input("Apakah Anda ingin mengkoreksi jumlah atau membatalkan item ini? (1. Koreksi Jumlah / 2. Batal / 0. Selesai): ")
                    if action_choice == "1":
                        while True:
                            try:
                                new_quantity = int(input("Masukkan jumlah yang benar untuk " + item_name + ": "))
                                if new_quantity < 0:
                                    print("Jumlah harus lebih besar dari atau sama dengan 0. Silakan masukkan kembali.")
                                    continue
                                break
                            except ValueError:
                                print("Jumlah harus berupa bilangan bulat. Silakan masukkan kembali.")
                        shopping_cart[-1] = (item_name, item_price, new_quantity)
                        print("Jumlah " + item_name + " diperbarui menjadi " + str(new_quantity))
                        break
                    elif action_choice == "2":
                        shopping_cart.pop()
                        print("Item " + item_name + " telah dibatalkan")
                        break
                    elif action_choice == "0":
                        break
                    else:
                        print("Pilihan tidak valid. Silakan pilih kembali.")

                continue_shopping = input("Apakah Anda ingin membeli barang lain dalam kategori ini? (YA/TIDAK) ")

                if continue_shopping.upper() != "YA":
                    break

        print("Barang yang ada di keranjang belanja Anda:")

        total_price = 0

        for i, cart_item in enumerate(shopping_cart, 1):
            item_name, item_price, item_quantity = cart_item
            subtotal = item_price * item_quantity
            total_price += subtotal
            print(str(i) + ". " + item_name + " - Rp" + str(item_price) + " x " + str(item_quantity) + " = Rp" + str(subtotal))

        print("Total harga: Rp" + str(total_price))

        # Menghitung diskon
        discounted_price, discount_amount = calculate_discount(total_price)

        print("Diskon: Rp" + str(discount_amount))
        print("Total harga setelah diskon: Rp" + str(discounted_price))

    print("Terima kasih telah berbelanja di Sumber Makmur Super General Store!")
    print("===============================================")


def display_categories():
    print("Kami menawarkan berbagai kategori produk untuk Anda:")
    print("1. Food")
    print("2. Toys")
    print("3. Toiletries")
    print("4. Beverages")
    print("5. Electricals")
    print("6. Clothing")


if __name__ == "__main__":
    main()


# In[ ]:




