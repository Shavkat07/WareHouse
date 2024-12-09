

# Таъминотчи қўшиш
def add_supplier(name, company, quantity, price):
    suppliers = load_data()
    new_supplier = {
        "name": name,
        "company": company,
        "quantity": quantity,
        "price": price
    }
    suppliers.append(new_supplier)
    save_data(suppliers)
    print(f"Таъминотчи {name} қўшилди.")

# Таъминотчиларни кўриш
def view_suppliers():
    suppliers = load_data()
    if not suppliers:
        print("Таъминотчилар рўйхати бўш.")
    else:
        for idx, supplier in enumerate(suppliers, start=1):
            print(f"{idx}. Исим: {supplier['name']}, Компания: {supplier['company']}, "
                  f"Миқдори: {supplier['quantity']}, Нархи: ${supplier['price']}")

# Таъминотчини ўчириш
def delete_supplier(name):
    suppliers = load_data()
    updated_suppliers = [supplier for supplier in suppliers if supplier["name"] != name]
    if len(suppliers) == len(updated_suppliers):
        print(f"Таъминотчи {name} топилмади.")
    else:
        save_data(updated_suppliers)
        print(f"Таъминотчи {name} ўчирилди.")
