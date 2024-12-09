from data import load_data_from_file, save_data_to_file

def add_category():
    """Yangi kategoriya yaratadi va qaytaradi."""
    print("\nYangi kategoriya ma'lumotlarini kiriting:")
    category = {
        "id": 0,
        "name": "",
        "description": ""
    }

    while True:
        name = input("Kategoriya nomi: ")

        if load_data_from_file('categories', param_key='name', param_value=name) is not None:
            print("Bunday nomlik category mavjud. Iltimos boshqasini kiriting.")
        else:
            category["name"] = name
            break

    description = input("Kategoriya tavsifi: ")
    category["description"] = description

    last_category_id = load_data_from_file("categories", param_key='id')
    if last_category_id is not None:
        category["id"] = last_category_id + 1
    else:
        category["id"] = 1

    save_data_to_file(data=category, file_name='categories')
    print("Category added succesfully")
    return category["name"]


def view_categories(file_path="categories.json"):
    """Barcha kategoriyalarni JSON fayldan o'qiydi va qaytaradi."""
    return load_data_from_file('categories', param_key='all')

