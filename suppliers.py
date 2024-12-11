from data import load_data_from_file, save_data_to_file, delete_data

# Таъминотчи қўшиш
def add_supplier():
    new_supplier = {
        'id': 0,
        "name": '',
        "contact_name": "",
        "phone": '',
        "email": '',
        'address': '',
    }
    name = input("Enter your name: ")
    new_supplier['name'] = name
    contact_name = input("Enter your contact name: ")
    new_supplier['contact_name'] = contact_name
    phone = input("Enter your phone number: ")
    if not (phone.isdigit() and len(phone) == 9):
        raise ValueError("Telefon raqami noto'g'ri. U 9 ta raqamdan iborat bo'lishi kerak.")
    # Takroriy telefon raqami tekshiruvi
    if load_data_from_file(file_name='suppliers', param_key='phone', param_value=phone) is not None:
        raise ValueError("Bu telefon raqami allaqachon mavjud. Iltimos, boshqa raqam kiriting.")

    new_supplier["phone"] = phone

    email = input("Enter your email: ")

    if load_data_from_file(file_name='suppliers', param_key='email', param_value=email) is None:
        if email.islower() and "@" in email:
            new_supplier['email'] = email
        else:
            print('Email format is invalid!!!')
            return
    else:
        print("Email already exists!!!")
        return

    address = input("Enter your address: ")
    new_supplier['address'] = address


    last_supplier_id = load_data_from_file('suppliers', param_key='id')
    if last_supplier_id is not None:
        new_supplier["id"] = last_supplier_id + 1
    else:
        new_supplier["id"] = 1

    save_data_to_file(file_name='suppliers', data=new_supplier)
    print(f"Таъминотчи {name} қўшилди.")

# Таъминотчиларни кўриш
def view_suppliers():
    suppliers = load_data_from_file('suppliers', param_key='all')
    if not suppliers:
        print("Таъминотчилар рўйхати бўш.")
    else:
        for idx, supplier in enumerate(suppliers, start=1):
            print(f"{idx}. Исим: {supplier['name']}, Компания: {supplier['company']}, "
                  f"Миқдори: {supplier['quantity']}, Нархи: ${supplier['price']}")

# Таъминотчини ўчириш
def delete_supplier(supplier_id):

    delete_data(file_name='suppliers', param_key='id', param_value=supplier_id)

    print(f"Таъминотчи ўчирилди.")

