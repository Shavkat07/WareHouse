
import getpass
import hashlib
from data import *

# JSON fayl nomi
DATA_FILE = "users.json"
ADMIN_PASSWORD = "admin12345"
MANAGER_PASSWORD = "meneger12345"
DIRECTOR_PASSWORD = "director12345"

session = {"logged_in": False}

def is_logged_in():
    """Проверяет, вошел ли пользователь."""
    return session["logged_in"]


# Parolni xeshlash funksiyasi
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Ro'yxatdan o'tish funksiyasi
def register():
    while True:  # Noto'g'ri ma'lumotlar uchun qaytadan urinib ko'rish
        try:
            # Foydalanuvchi ma'lumotlarini yuklash
            users = load_data_from_file('users', param_key='all')

            # Foydalanuvchi1dan ma'lumotlarni kiritish
            username = input("Username kiriting: ").strip()

            if not username:
                raise ValueError("Username kiritilishi shart.")
            # Takroriy username tekshiruvi
            for user in users:
                if user['username'] == username:
                    a = input("Bu username allaqachon mavjud. Login qilishni istaysizmi ('yes' or 'no'): ")
                    if a == "yes":
                        if login() == "Login Successfully":
                            return "Logining"

                        return "Login Failed"

                    else:
                        return
            # Parolni ko'rinmas holatda kiritish

            password = getpass.getpass("Password kiriting: ").strip()
            if not password:
                raise ValueError("Password kiritilishi shart.")
            hashed_password = hash_password(password)  # Parolni xeshlash

            first_name = input("Ismingizni kiriting: ").strip()
            if len(first_name) > 50 or not first_name:
                raise ValueError("Ism uzunligi 50 ta belgidan oshmasligi va bo'sh bo'lmasligi kerak.")

            last_name = input("Familiyangizni kiriting: ").strip()
            if len(last_name) > 50 or not last_name:
                raise ValueError("Familiya uzunligi 50 ta belgidan oshmasligi va bo'sh bo'lmasligi kerak.")

            phone = int(''.join(input("Telefon raqamingizni kiriting (9 ta raqam): ").strip().split()))
            if not (phone and len(str(phone)) == 9):
                raise ValueError("Telefon raqami noto'g'ri. U 9 ta raqamdan iborat bo'lishi kerak.")
            # Takroriy telefon raqami tekshiruvi
            for user in users:
                if user["phone"] == phone:
                    raise ValueError("Bu telefon raqami allaqachon mavjud. Iltimos, boshqa raqam kiriting.")

            role = input("Rolingizni kiriting (admin/manager/director/worker): ").strip().lower()
            if role not in ["admin", "manager", "director", "worker"]:
                raise ValueError("Rol noto'g'ri. Rol admin, manager, director yoki worker bo'lishi kerak.")

            # Admin uchun parol tekshiruvi
            if role == "admin":
                admin_password = getpass.getpass("Admin parolini kiriting: ").strip()
                if admin_password != ADMIN_PASSWORD:
                    raise ValueError("Admin paroli noto'g'ri. Ro'yxatdan o'tish bekor qilindi.")

            if role == "manager":
                manager_password = getpass.getpass("Manager parolini kiriting").strip()
                if manager_password != MANAGER_PASSWORD:
                    raise ValueError("Menegir paroli notogri kiritildi")

            if role == "director":
                director_password = getpass.getpass("director parolini kiriting").strip()
                if director_password != DIRECTOR_PASSWORD:
                    raise ValueError("Director paroli notogri kiritildi")

            # Yangi foydalanuvchi identifikatori
            new_user_id = load_data_from_file(file_name="users", param_key="id",) + 1

            # Yangi foydalanuvchini qo'shish
            new_user = {
                "id": new_user_id,
                "username": username,
                "password": hashed_password,  # Parol xeshlangan holda saqlanadi
                "first_name": first_name,
                "last_name": last_name,
                "phone": phone,
                "role": role
            }


            # JSON faylga yozish
            save_data_to_file(new_user, file_name='users')
            print("Ro'yxatdan muvaffaqiyatli o'tdingiz!")
            break  # Ro'yxatdan o'tish muvaffaqiyatli bo'lsa, siklni tugatish
        except ValueError as e:
            print(f"Xatolik: {e}")
            print("Iltimos, ma'lumotlarni qaytadan kiriting.\n")

# Login funksiyasi
def login():
    try:
        users = load_data_from_file(file_name='users', param_key='all')  # JSON fayldan foydalanuvchilarni yuklash

        username = input("Username kiriting: ").strip()
        password = getpass.getpass("Password kiriting: ").strip()

        hashed_password = hash_password(password)  # Kiritilgan parolni xeshlash

        # Foydalanuvchini qidirish
        for user in users:
            if user["username"] == username and user["password"] == hashed_password:
                print(f"Xush kelibsiz, {user['first_name']} {user['last_name']}! Sizning rolingiz: {user['role']}.")
                session['logged_in'] = True
                return "Login Successfully" # Login muvaffaqiyatli bo'lsa, funksiyani tugatish

        # Agar foydalanuvchi topilmasa
        print("Username yoki password noto'g'ri.")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

def logout():
    """Логаут пользователя."""
    if not is_logged_in():
        print("Siz royhatdan otmagansiz.")
        return
    session["logged_in"] = False
    print("Siz sistemadan chiqdingiz.")



# Foydalanuvchilarni ko'rish funksiyasi
def view_users():
    try:
        users = load_data_from_file("users", param_key="all",)  # JSON fayldan foydalanuvchilarni yuklash
        if users:  # Agar foydalanuvchilar mavjud bo'lsa
            print("\nFoydalanuvchilar ro'yxati:")
            for user in users:
                print(
                    f"- ID: {user.get('id', 'Noma’lum')}, "
                    f"Username: {user.get('username', 'Noma’lum')}, "
                    f"First Name: {user.get('first_name', 'Noma’lum')}, "
                    f"Last Name: {user.get('last_name', 'Noma’lum')}, "
                    f"Phone: {user.get('phone', 'Noma’lum')}, "
                    f"Role: {user.get('role', 'Noma’lum')}"
                )
        else:
            print("\nHozircha foydalanuvchilar mavjud emas.")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

