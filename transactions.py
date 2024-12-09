import json
from datetime import datetime

# Путь к JSON-файлу
file_path = 'Database/transactions.json'
products_file = 'Database/products.json'  # JSON-файл с товарами на складе


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
def check_product_availability(warehouse_id, product_id, quantity, products, transaction_type):
    if transaction_type == 'export':
        for product in products:
            if product["warehouse_id"] == warehouse_id and product["product_id"] == product_id:
                if product["quantity"] >= quantity:
                    # Уменьшаем количество товара на складе при экспорте
                    product["quantity"] -= quantity
                    save_data(products, products_file)  # Сохраняем обновленные данные о товарах
                    return True  # Товар есть и его достаточно
                else:
                    print(
                        f"Ошибка: недостаточно товара для экспорта. На складе {warehouse_id} доступно только {product['quantity']} единиц.")
                    return False
        print(f"Ошибка: товара с ID {product_id} нет на складе {warehouse_id}.")
        return False
    return True  # Для транзакций типа 'import' не проверяем наличие товара


# Функция для создания транзакции

def create_transaction(user, product_id, transaction_type, quantity, warehouse_id):
    transactions = load_data(file_path)
    user = input("Username kiriting")
    product_id = int(input("Productning id kiriting"))
    transaction_type = input("Import or Export kiling")
    quantity = int(input("Nechta tovar ekanligini kirgizing"))
    warehouse_id = int(input("Skadlning id sini kiriting"))

    # products = load_data(products_file)  # Загружаем список товаров на складе

    transaction = {
        'id': 1,
        'user': '',
        'product_id': '',
        'transaction_type':'',
        'quantity': '',
        'date':'',
        'warehouse_id':'',
    }

    if transaction['id'] < transactions[-1]['id']:
        transaction['id'] += transactions[-1]['id'] + 1

    if load_data('users', param_key='username', param_value=user):
        transaction['user'] = user
    else:
        return "Username does not exists"

    if load_data('products', param_key='id', param_value=product_id):
        transaction['product_id'] = product_id
    else:
        return




    # Ввод типа транзакции
    while True:
        transaction_type = input("Введите тип транзакции (import/export): ").strip().lower()
        if transaction_type in {"import", "export"}:
            break
        else:
            print("Ошибка: тип транзакции может быть только 'import' или 'export'. Попробуйте снова.")

    warehouse_id = int(input("Введите ID склада: "))
    user_id = int(input("Введите ID пользователя: "))

    # Проверка наличия товара на складе для транзакции типа 'export'
    if not check_product_availability(warehouse_id, product_id, quantity, products, transaction_type):
        return  # Если товара нет или недостаточно для экспорта, прекращаем выполнение

    # Создание новой транзакции
    new_transaction = {
        "id": len(transactions) + 1,
        "product_id": product_id,
        "quantity": quantity,
        "transaction_type": transaction_type,
        "date": datetime.now().isoformat(),
        "warehouse_id": warehouse_id,
        "user_id": user_id
    }

    transactions.append(new_transaction)
    save_data(transactions, file_path)
    print(f"Транзакция добавлена: {new_transaction}")


# Функция для просмотра всех транзакций
def view_transactions(file_path, product):
    transactions = load_data(file_path, )
    if not transactions:
        print("Список транзакций пуст.")
    else:
        print("\nВсе транзакции:")
        for transaction in transactions:
            print(transaction)


# Функция для удаления транзакции по ID
def delete_transaction(file_path):
    transactions = load_data(file_path)
    if not transactions:
        print("Список транзакций пуст. Нечего удалять.")
        return

    try:
        transaction_id = int(input("Введите ID транзакции для удаления: "))
        # Поиск и удаление транзакции
        updated_transactions = [t for t in transactions if t["id"] != transaction_id]
        if len(updated_transactions) == len(transactions):
            print(f"Транзакция с ID {transaction_id} не найдена.")
        else:
            save_data(updated_transactions, file_path)
            print(f"Транзакция с ID {transaction_id} удалена.")
    except ValueError:
        print("Ошибка: введите корректный ID.")


# Пример использования функций без меню

# Создание новой транзакции
create_transaction('transactions.json', 'products.json')

# Просмотр всех транзакций
view_transactions('transactions.json')

# Удаление транзакции
delete_transaction('transactions.json')



