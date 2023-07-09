existing_users = [
    User("Andi Subandi", "andi12", 13, "andi12@example.com", True),
    User("Budi Setiawan", "budi321", 7, "budi321@example.com", True),
    User("Candra Lee", "chann66", 3, "chann66@example.com", False),
    User("Denis Raharjo", "denz212", 2, "denz212@example.com", True),
    User("Eka Jauhari", "ekawwa11", 5, "ekaazzz@example.com", True)

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
    print("Input: " + username_email)
    for user in existing_users:
        print("Existing User: " + user.username + " / " + user.email)
    existing_user = next(
        (user for user in existing_users if user.username == username_email or user.email == username_email), None
    )
    if existing_user is not None:
        print("Selamat datang, " + existing_user.name + "!")
        return existing_user
    else:
        create_account_choice = input("Akun tidak ditemukan. Apakah Anda sudah memiliki akun Sumber Makmur? (YA/TIDAK) ")
        if create_account_choice.upper() == "YA":
            return create_account()
        else:
            print("Login gagal. Silakan ulangi proses dari awal.")
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