import json
from datetime import datetime
from operator import ifloordiv

from data import load_data_from_file, save_data_to_file, update_data, delete_data


# Путь к JSON-файлу
# file_path = 'Database/transactions.json'
# products_file = 'Database/products.json'  # JSON-файл с товарами на складе


# Загрузка существующих данных (транзакции и товары)
# def load_data(path, ):
#     try:
#         with open(file_path, 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return []  # Если файл отсутствует, возвращаем пустой список
#
#
# # Сохранение данных в файл
# def save_data(data, file_path):
#     with open(file_path, 'w') as file:
#         json.dump(data, file, indent=4)


# Проверка наличия товара на складе для экспорта и уменьшение количества
def check_product_availability(warehouse_id, product_id, quantity, transaction_type):
    product = load_data_from_file(file_name='products', param_key='id', param_value=product_id)

    if transaction_type == 'export':

        if product["quantity"] >= quantity:
            # Уменьшаем количество товара на складе при экспорте
            new_product_quantity = product["quantity"] - quantity
            update_data(file_name='products', obj_id=product_id, param_key='quantity', new_param_value=new_product_quantity)  # Сохраняем обновленные данные о товарах
            return True  # Товар есть и его достаточно
        else:
            print(
                f"Ошибка: недостаточно товара для экспорта. На складе {warehouse_id} доступно только {product['quantity']} единиц.")
            return False
    else:
        new_product_quantity = product["quantity"] + quantity
        update_data(file_name='products', obj_id=product_id, param_key='quantity', new_param_value=new_product_quantity)
    return True  # Для транзакций типа 'import' не проверяем наличие товара


# Функция для создания транзакции

def create_transaction():
    transaction = {
        'id': 1,
        'user': '',
        'product_id': '',
        'transaction_type': '',
        'quantity': '',
        'date': '',
        'warehouse_id': '',
    }



    product_id = int(input("Productning id kiriting"))

    if load_data_from_file('products', param_key='id', param_value=product_id):
        transaction['product_id'] = product_id
    else:
        # add_product()
        pass

    username = input("Username kiriting")

    if load_data_from_file('users', param_key='username', param_value=username):
        transaction['user'] = username
    else:
        return "Username does not exists"

    quantity = int(input("Nechta tovar ekanligini kirgizing"))

    # Ввод типа транзакции
    while True:
        transaction_type = input("Введите тип транзакции (import/export): ").strip().lower()
        if transaction_type in {"import", "export"}:
            transaction['transaction_type'] = transaction_type
            break
        else:
            print("Ошибка: тип транзакции может быть только 'import' или 'export'. Попробуйте снова.")

    warehouse_id = int(input("Введите ID склада: "))

    if load_data_from_file('warehouses', 'id', warehouse_id) is not None:
        transaction['warehouse_id'] = warehouse_id
    else:
        print("Omborxona mavjud emas")
        return

    # Проверка наличия товара на складе для транзакции типа 'export'
    if not check_product_availability(warehouse_id, product_id, quantity, transaction_type):
        print("Tovar skladda yetarlicha emas")
        return  # Если товара нет или недостаточно для экспорта, прекращаем выполнение

    transaction['quantity'] = quantity

    last_transaction_id = load_data_from_file('transactions', param_key='id', )

    if last_transaction_id is not None:
        transaction["id"] = last_transaction_id + 1
    else:
        transaction["id"] = 1

    transaction['date'] = datetime.now().isoformat()
    log = f"""
                  f"Id Transaction: {transaction['id']} \n"
                  f"User Who created this transaction: {transaction['user']} \n"
                  f"Product id: {transaction['product_id']} \n"
                  f"Transaction type: {transaction['transaction_type']} \n"
                  f"Quantity: {transaction['quantity']} \n"
                  f"Date: {transaction['date']} \n"
                  f"Warehouse id: {transaction['warehouse_id']} \n"
                  

    """

    save_data_to_file(file_name='transactions', data=transaction)
    print(f"Транзакция добавлена: {transaction}")


# Функция для просмотра всех транзакций
def view_transactions():
    transactions = load_data_from_file('transactions', param_key='all')
    if transactions is None:
        print("Список транзакций пуст.")
    else:
        print("\nВсе транзакции:")
        for transaction in transactions:
            print(f"Id Transaction: {transaction['id']} \n"
                  f"User Who created this transaction: {transaction['user']} \n"
                  f"Product id: {transaction['product_id']} \n"
                  f"Transaction type: {transaction['transaction_type']} \n"
                  f"Quantity: {transaction['quantity']} \n"
                  f"Date: {transaction['date']} \n"
                  f"Warehouse id: {transaction['warehouse_id']} \n")


# Функция для удаления транзакции по ID
def delete_transaction():
    transaction_id = int(input("Id raqamini kiriting: "))
    delete_data(file_name='transactions', param_key='id', param_value=transaction_id)
    return



# Пример использования функций без меню

# Создание новой транзакции
# create_transaction()

# Просмотр всех транзакций

# Удаление транзакции
# delete_transaction('transactions.json')



