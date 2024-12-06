import json
import os

# JSON fayl nomi
DATA_FILE = "users.json"
ADMIN_PASSWORD = "amdin12345"

# JSON faylni yaratish yoki o'qish
def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            json.dump([], file)  # Bo'sh ro'yxat saqlash
    with open(DATA_FILE, "r") as file:
        return json.load(file)

# JSON faylga yangi ma'lumot yozish
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Ro'yxatdan o'tish funksiyasi
def register():
    # Foydalanuvchi ma'lumotlarini yuklash
    users = load_data()

    # Foydalanuvchidan ma'lumotlarni kiritish
    username = input("Username kiriting: ").strip()
    password = input("Password kiriting: ").strip()
    first_name = input("Ismingizni kiriting: ").strip()
    last_name = input("Familiyangizni kiriting: ").strip()
    phone = input("Telefon raqamingizni kiriting: ").strip()
    role = input("Rolingizni kiriting (masalan, user yoki admin): ").strip().lower()

    # Tekshiruv: Username takrorlanmasligi kerak
    for user in users:
        if user["username"] == username:
            print("❌ Bu username allaqachon mavjud. Iltimos, boshqa username tanlang.")
            return

    if role == "admin":
        admin_password = input("Admin parolni kiriting: ").strip()
        if admin_password != ADMIN_PASSWORD:
            print("Admin parol noto'g'ri royhatdan otish bekor qilindi.")


    # Yangi foydalanuvchi identifikatori
    user_id = len(users) + 1

    # Yangi foydalanuvchini qo'shish
    new_user = {
        "id": user_id,
        "username": username,
        "password": password,  # Parol xeshlanishi mumkin
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "role": role
    }
    users.append(new_user)

    # JSON faylga yozish
    save_data(users)
    print("Ro'yxatdan muvaffaqiyatli o'tdingiz!")

# Foydalanuvchilarni ko'rish funksiyasi
def view_users():
    try:
        users = load_data()  # JSON fayldan foydalanuvchilarni yuklash
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
        print(f"❌ Xatolik yuz berdi: {e}")


# Bosh menyu
if __name__ == "__main__":
    while True:
        print("\n=== Ro'yxatdan o'tish ===")

        print("1. Ro'yxatdan o'tish")
        print("2. Foydalanuvchilarni ko'rish")
        print("3. Chiqish")
        choice = input("Tanlovingizni kiriting: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            view_users()
        elif choice == "3":
            print("Tizimdan chiqildi.")
            break
        else:
            print("Noto'g'ri tanlov. Qaytadan urinib ko'ring.")
