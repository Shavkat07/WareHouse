from categories import add_category
from data import load_data_from_file, save_data_to_file, update_data, delete_data


def add_product():
    """Yangi mahsulot ma'lumotlarini yaratadi va qaytaradi."""
    print("\nYangi mahsulot ma'lumotlarini kiriting:")
    product = {
        "id": 0,
        "name": '',
        "price": '',
        "description": '',
        "quantity": '',
        "category": '',
        "supplier_id": 0,
        "warehouse_id": 0
    }

    name = input("Mahsulot nomi: ")
    product["name"] = name

    price = input("Narxi: ")
    product["price"] = price

    description = input("Tavsif: ")
    product["description"] = description

    quantity = int(input("Miqdori: "))
    product["quantity"] = quantity

    category = input("Kategoriya nomi: ")

    if load_data_from_file(file_name='categories', param_key='name', param_value=category) is not None:
        product['category'] = category
    else:
        while True:
            question = input("Bunaqa category hali mavjud emas. Yangi qushishni istaysizmi('yes' or 'no'): ")
            if question == 'yes':
                category_name = add_category()
                product['category'] = category_name
                break
            elif question == 'no':
                print("Function failed.")
                return
            else:
                pass

    supplier_id = int(input("Yetkazib beruvchi ID: "))
    if load_data_from_file('suppliers', param_key='id', param_value=supplier_id) is not None:
        product['supplier_id'] = supplier_id
    else:
        print("Supplier doesn't exist.")
        return

    warehouse_id = int(input("Ombor ID: "))

    if load_data_from_file('warehouses', param_key='id', param_value=warehouse_id) is not None:
        product['warehouse_id'] = warehouse_id
    else:
        print("Function failed.")
        return
    last_product_id = load_data_from_file('products', param_key='id')
    if last_product_id is not None:
        product["id"] = last_product_id + 1
    else:
        product["id"] = 1

    print("Product Added Successfully")
    return product

def delete_product(product_id):
    delete_data(file_name='products', param_key='id', param_value=product_id)
    print("Product Deleted Successfully")
    return

def view_products():
    """JSON fayldan barcha mahsulotlarni o'qiydi va qaytaradi."""
    return load_data_from_file(file_name='products', param_key='all')


add_product()