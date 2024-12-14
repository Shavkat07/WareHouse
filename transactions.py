# from datetime import datetime
# from products import add_product
# from logs import save_log, get_logs
# from data import load_data_from_file, save_data_to_file, update_data, delete_data
#
# # Проверка наличия товара на складе для экспорта и уменьшение количества
# def check_product_availability(warehouse_id, product_id, quantity, transaction_type):
#     product = load_data_from_file(file_name='products', param_key='id', param_value=product_id)
#     warehouse = load_data_from_file(file_name="warehouses", param_key='id', param_value=warehouse_id)
#     if transaction_type == 'export':
#
#         if product["quantity"] >= quantity:
#             # Уменьшаем количество товара на складе при экспорте
#             new_product_quantity = product["quantity"] - quantity
#             new_warehouse_capacity = warehouse['current_capacity'] - quantity
#
#             update_data(file_name='warehouses', obj_id=warehouse_id, param_key='current_capacity',
#                         new_param_value=new_warehouse_capacity)
#             update_data(file_name='products', obj_id=product_id, param_key='quantity',
#                         new_param_value=new_product_quantity)  # Сохраняем обновленные данные о товарах
#             return True  # Товар есть и его достаточно
#         else:
#             print(
#                 f"Ошибка: недостаточно товара для экспорта. На складе {warehouse_id} доступно только {product['quantity']} единиц.")
#             return False
#     else:
#         new_product_quantity = product["quantity"] + quantity
#         new_warehouse_capacity = warehouse['current_capacity'] + quantity
#         update_data(file_name='warehouses', obj_id=warehouse_id, param_key='current_capacity',
#                     new_param_value=new_warehouse_capacity)
#         update_data(file_name='products', obj_id=product_id, param_key='quantity', new_param_value=new_product_quantity)
#     return True  # Для транзакций типа 'import' не проверяем наличие товара
#
#
# # Функция для создания транзакции
#
# def create_transaction():
#     transaction = {
#         'id': 1,
#         'user': '',
#         'product_id': '',
#         'transaction_type': '',
#         'quantity': '',
#         'date': '',
#         'warehouse_id': '',
#     }
#
#     product_id = int(input("Productning id kiriting: "))
#
#     if product_id != 0 and load_data_from_file('products', param_key='id', param_value=product_id) is not None:
#
#         transaction['product_id'] = product_id
#
#         quantity = int(''.join(input("Nechta tovar ekanligini kiriting: ").split()))
#         transaction['quantity'] = quantity
#
#         warehouse_id = int(input("Введите ID склада: "))
#         if load_data_from_file('warehouses', 'id', warehouse_id) is not None:
#             transaction['warehouse_id'] = warehouse_id
#         else:
#             print("Omborxona mavjud emas")
#             return
#
#         # Ввод типа транзакции
#         while True:
#             transaction_type = input("Введите тип транзакции (import/export): ").strip().lower()
#             if transaction_type in {"import", "export"}:
#                 transaction['transaction_type'] = transaction_type
#                 break
#             else:
#                 print("Ошибка: тип транзакции может быть только 'import' или 'export'. Попробуйте снова.")
#
#         # Проверка наличия товара на складе для транзакции типа 'export'
#         if not check_product_availability(warehouse_id, product_id, quantity, transaction_type):
#             print("Tovar skladda yetarlicha emas")
#             return  # Если товара нет или недостаточно для экспорта, прекращаем выполнение
#
#
#     else:
#         while True:
#             question = input("Bunaqa product hali mavjud emas. Yangi qushishni istaysizmi('yes' or 'no'): ")
#             if question == 'yes':
#                 new_product = add_product()
#                 transaction['product_id'] = new_product['id']
#                 transaction['quantity'] = new_product['quantity']
#                 transaction['warehouse_id'] = new_product['warehouse_id']
#                 transaction['transaction_type'] = 'import'
#
#                 break
#             elif question == 'no':
#                 print("Function failed.")
#                 return
#             else:
#                 pass
#
#     username = input("Username kiriting: ")
#
#     if load_data_from_file('users', param_key='username', param_value=username):
#         transaction['user'] = username
#     else:
#         return "Username does not exists"
#
#     last_transaction_id = load_data_from_file('transactions', param_key='id', )
#
#     if last_transaction_id is not None:
#         transaction["id"] = last_transaction_id + 1
#     else:
#         transaction["id"] = 1
#
#     transaction['date'] = datetime.now().isoformat()
#
#     log = (
#         f"Transaction ID: {transaction['id']}"
#         f"User who created this transaction: {transaction['user']}"
#         f"Product ID: {transaction['product_id']}"
#         f"Transaction type: {transaction['transaction_type']}"
#         f"Quantity: {transaction['quantity']}"
#         f"Date of transaction: {transaction['date']}"
#         f"Warehouse ID: {transaction['warehouse_id']}"
#     )
#     save_data_to_file(file_name='transactions', data=transaction)
#     print(f"Транзакция добавлена: {transaction}")
#     save_log(log=log)
#     return
#
#
# # Функция для просмотра всех транзакций
# def view_transactions():
#     transactions = load_data_from_file('transactions', param_key='all')
#     if transactions is None:
#         print("Список транзакций пуст.")
#     else:
#         print("\nВсе транзакции:")
#         for transaction in transactions:
#             print(f"Id Transaction: {transaction['id']} \n"
#                   f"User Who created this transaction: {transaction['user']} \n"
#                   f"Product id: {transaction['product_id']} \n"
#                   f"Transaction type: {transaction['transaction_type']} \n"
#                   f"Quantity: {transaction['quantity']} \n"
#                   f"Date: {transaction['date']} \n"
#                   f"Warehouse id: {transaction['warehouse_id']} \n")
#
#
# # Функция для удаления транзакции по ID
# def delete_transaction():
#     transaction_id = int(input("Id raqamini kiriting: "))
#     delete_data(file_name='transactions', param_key='id', param_value=transaction_id)
#     return

#  for PROFESSIONAL VERSION OF PyCharm
# from datetime import datetime
# import matplotlib.pyplot as plt
# from collections import Counter
# from products import add_product
# from logs import save_log, get_logs
# from data import load_data_from_file, save_data_to_file, update_data, delete_data
#
#
# def check_product_availability(warehouse_id, product_id, quantity, transaction_type):
#     product = load_data_from_file( file_name='products', param_key='id', param_value=product_id )
#     warehouse = load_data_from_file( file_name="warehouses", param_key='id', param_value=warehouse_id )
#     if transaction_type == 'export':
#         if product["quantity"] >= quantity:
#             # Уменьшаем количество товара на складе при экспорте
#             new_product_quantity = product["quantity"] - quantity
#             new_warehouse_capacity = warehouse['current_capacity'] - quantity
#             update_data( file_name='warehouses', obj_id=warehouse_id, param_key='current_capacity',
#                          new_param_value=new_warehouse_capacity )
#             update_data( file_name='products', obj_id=product_id, param_key='quantity',
#                          new_param_value=new_product_quantity )  # Сохраняем обновленные данные о товарах
#             return True  # Товар есть и его достаточно
#         else:
#             print(
#                 f"Ошибка: недостаточно товара для экспорта. На складе {warehouse_id} доступно только {product['quantity']} единиц." )
#             return False
#     else:
#         new_product_quantity = product["quantity"] + quantity
#         new_warehouse_capacity = warehouse['current_capacity'] + quantity
#         update_data( file_name='warehouses', obj_id=warehouse_id, param_key='current_capacity',
#                      new_param_value=new_warehouse_capacity )
#         update_data( file_name='products', obj_id=product_id, param_key='quantity',
#                      new_param_value=new_product_quantity )
#     return True  # Для транзакций типа 'import' не проверяем наличие товара
#
#
# # Функция для создания транзакции
# def create_transaction():
#     transaction = {
#         'id': 1,
#         'user': '',
#         'product_id': '',
#         'transaction_type': '',
#         'quantity': '',
#         'date': '',
#         'warehouse_id': '',
#     }
#
#     product_id = int( input( "Productning id kiriting: " ) )
#
#     if product_id != 0 and load_data_from_file( 'products', param_key='id', param_value=product_id ) is not None:
#         transaction['product_id'] = product_id
#         quantity = int( ''.join( input( "Nechta tovar ekanligini kiriting: " ).split() ) )
#         transaction['quantity'] = quantity
#         warehouse_id = int( input( "Введите ID склада: " ) )
#         if load_data_from_file( 'warehouses', 'id', warehouse_id ) is not None:
#             transaction['warehouse_id'] = warehouse_id
#         else:
#             print( "Omborxona mavjud emas" )
#             return
#
#         # Ввод типа транзакции
#         while True:
#             transaction_type = input( "Введите тип транзакции (import/export): " ).strip().lower()
#             if transaction_type in {"import", "export"}:
#                 transaction['transaction_type'] = transaction_type
#                 break
#             else:
#                 print( "Ошибка: тип транзакции может быть только 'import' или 'export'. Попробуйте снова." )
#
#         # Проверка наличия товара на складе для транзакции типа 'export'
#         if not check_product_availability( warehouse_id, product_id, quantity, transaction_type ):
#             print( "Tovar skladda yetarlicha emas" )
#             return  # Если товара нет или недостаточно для экспорта, прекращаем выполнение
#
#     else:
#         while True:
#             question = input( "Bunaqa product hali mavjud emas. Yangi qushishni istaysizmi('yes' or 'no'): " )
#             if question == 'yes':
#                 new_product = add_product()
#                 transaction['product_id'] = new_product['id']
#                 transaction['quantity'] = new_product['quantity']
#                 transaction['warehouse_id'] = new_product['warehouse_id']
#                 transaction['transaction_type'] = 'import'
#                 break
#             elif question == 'no':
#                 print( "Function failed." )
#                 return
#             else:
#                 pass
#
#     username = input( "Username kiriting: " )
#     if load_data_from_file( 'users', param_key='username', param_value=username ):
#         transaction['user'] = username
#     else:
#         return "Username does not exists"
#
#     last_transaction_id = load_data_from_file( 'transactions', param_key='id', )
#     if last_transaction_id is not None:
#         transaction["id"] = last_transaction_id + 1
#     else:
#         transaction["id"] = 1
#
#     transaction['date'] = datetime.now().isoformat()
#
#     log = (
#         f"Transaction ID: {transaction['id']} "
#         f"User who created this transaction: {transaction['user']} "
#         f"Product ID: {transaction['product_id']} "
#         f"Transaction type: {transaction['transaction_type']} "
#         f"Quantity: {transaction['quantity']} "
#         f"Date of transaction: {transaction['date']} "
#         f"Warehouse ID: {transaction['warehouse_id']} "
#     )
#     save_data_to_file( file_name='transactions', data=transaction )
#     print( f"Транзакция добавлена: {transaction}" )
#     save_log( log=log )
#     return
#
#
# # Функция для просмотра всех транзакций
# def view_transactions():
#     transactions = load_data_from_file( 'transactions', param_key='all' )
#     if transactions is None:
#         print( "Список транзакций пуст." )
#     else:
#         print( "\nВсе транзакции:" )
#         for transaction in transactions:
#             print( f"Id Transaction: {transaction['id']} \n"
#                    f"User Who created this transaction: {transaction['user']} \n"
#                    f"Product id: {transaction['product_id']} \n"
#                    f"Transaction type: {transaction['transaction_type']} \n"
#                    f"Quantity: {transaction['quantity']} \n"
#                    f"Date: {transaction['date']} \n"
#                    f"Warehouse id: {transaction['warehouse_id']} \n" )
#
#
# # Функция для удаления транзакции по ID
# def delete_transaction():
#     transaction_id = int( input( "Id raqamini kiriting: " ) )
#     delete_data( file_name='transactions', param_key='id', param_value=transaction_id )
#     return
#
#
# # Функция для создания диаграммы транзакций
# def get_transaction_data():
#     transactions = load_data_from_file( 'transactions', param_key='all' )
#     if transactions is None:
#         print( "No transactions available." )
#         return None
#     return transactions
#
#
# def generate_transaction_chart(transaction_type='export'):
#
#     transactions = get_transaction_data()
#     if transactions is None:
#         return
#
#     filtered_transactions = [t for t in transactions if t['transaction_type'] == transaction_type]
#
#     if not filtered_transactions:
#         print( f"No {transaction_type} transactions found." )
#         return
#
#     product_quantities = Counter()
#     for transaction in filtered_transactions:
#         product_id = transaction['product_id']
#         quantity = transaction['quantity']
#         product_quantities[product_id] += quantity
#
#     product_names = {product['id']: product['name'] for product in load_data_from_file( 'products', param_key='all' )}
#
#     product_ids = list( product_quantities.keys() )
#     quantities = list( product_quantities.values() )
#     labels = [product_names[product_id] for product_id in product_ids]
#
#     plt.figure( figsize=(10, 6) )
#     plt.bar( labels, quantities, color='skyblue' )
#     plt.xlabel( 'Products' )
#     plt.ylabel( 'Quantity' )
#     plt.title( f'Most {transaction_type.capitalize()}ed Products' )
#     plt.xticks( rotation=45, ha='right' )
#     plt.tight_layout()
#
#     plt.show()
# from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter
from products import add_product
from logs import save_log
from data import load_data_from_file, save_data_to_file, update_data, delete_data


# Проверка наличия товара на складе для экспорта и уменьшение количества
def check_product_availability(warehouse_id, product_id, quantity, transaction_type):
    product = load_data_from_file(file_name='products', param_key='id', param_value=product_id)
    warehouse = load_data_from_file(file_name="warehouses", param_key='id', param_value=warehouse_id)

    if transaction_type == 'export':
        if product["quantity"] >= quantity:
            # Уменьшаем количество товара на складе при экспорте
            new_product_quantity = product["quantity"] - quantity
            new_warehouse_capacity = warehouse['current_capacity'] - quantity
            update_data(file_name='warehouses', obj_id=warehouse_id, param_key='current_capacity',
                        new_param_value=new_warehouse_capacity)
            update_data(file_name='products', obj_id=product_id, param_key='quantity',
                        new_param_value=new_product_quantity)
            return True  # Товар есть и его достаточно
        else:
            print(f"Ошибка: недостаточно товара для экспорта. На складе {warehouse_id} доступно только {product['quantity']} единиц.")
            return False
    else:
        # For 'import' transaction, increase the product quantity and warehouse capacity
        new_product_quantity = product["quantity"] + quantity
        new_warehouse_capacity = warehouse['current_capacity'] + quantity
        update_data(file_name='warehouses', obj_id=warehouse_id, param_key='current_capacity',
                    new_param_value=new_warehouse_capacity)
        update_data(file_name='products', obj_id=product_id, param_key='quantity',
                    new_param_value=new_product_quantity)
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

    product_id = int(input("Product ID kiriting: "))

    if product_id != 0 and load_data_from_file('products', param_key='id', param_value=product_id) is not None:
        transaction['product_id'] = product_id
        quantity = int(input("Nechta tovar ekanligini kiriting: ").strip())
        transaction['quantity'] = quantity
        warehouse_id = int(input("Введите ID склада: "))
        if load_data_from_file('warehouses', 'id', warehouse_id) is not None:
            transaction['warehouse_id'] = warehouse_id
        else:
            print("Omborxona mavjud emas")
            return

        # Ввод типа транзакции
        while True:
            transaction_type = input("Введите тип транзакции (import/export): ").strip().lower()
            if transaction_type in {"import", "export"}:
                transaction['transaction_type'] = transaction_type
                break
            else:
                print("Ошибка: тип транзакции может быть только 'import' или 'export'. Попробуйте снова.")

        # Проверка наличия товара на складе для транзакции типа 'export'
        if not check_product_availability(warehouse_id, product_id, quantity, transaction_type):
            print("Tovar skladda yetarlicha emas")
            return  # Если товара нет или недостаточно для экспорта, прекращаем выполнение

    else:
        while True:
            question = input("Bunaqa product hali mavjud emas. Yangi qushishni istaysizmi('yes' or 'no'): ").strip().lower()
            if question == 'yes':
                new_product = add_product()
                transaction['product_id'] = new_product['id']
                transaction['quantity'] = new_product['quantity']
                transaction['warehouse_id'] = new_product['warehouse_id']
                transaction['transaction_type'] = 'import'
                break
            elif question == 'no':
                print("Function failed.")
                return
            else:
                print("Invalid input. Please answer 'yes' or 'no'.")

    username = input("Username kiriting: ").strip()
    if load_data_from_file('users', param_key='username', param_value=username):
        transaction['user'] = username
    else:
        return "Username does not exist"

    last_transaction_id = load_data_from_file('transactions', param_key='id')
    if last_transaction_id is not None:
        transaction["id"] = last_transaction_id + 1
    else:
        transaction["id"] = 1

    transaction['date'] = datetime.now().isoformat()

    log = (
        f"Transaction ID: {transaction['id']} "
        f"User who created this transaction: {transaction['user']} "
        f"Product ID: {transaction['product_id']} "
        f"Transaction type: {transaction['transaction_type']} "
        f"Quantity: {transaction['quantity']} "
        f"Date of transaction: {transaction['date']} "
        f"Warehouse ID: {transaction['warehouse_id']} "
    )
    save_data_to_file(file_name='transactions', data=transaction)
    print(f"Транзакция добавлена: {transaction}")
    save_log(log=log)
    return


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


# Функция для создания диаграммы транзакций
def get_transaction_data():
    transactions = load_data_from_file('transactions', param_key='all')
    if transactions is None:
        print("No transactions available.")
        return None
    return transactions


def generate_transaction_chart(transaction_type='export', file_name='transaction_chart.png'):
    diagram_dir = "C:/Users/Asus/PycharmProjects/AwareHOUSE/diagrams"
    os.makedirs(diagram_dir, exist_ok=True)  # Ensure the directory exists before saving

    transactions = get_transaction_data()
    if transactions is None:
        return

    filtered_transactions = [t for t in transactions if t['transaction_type'] == transaction_type]

    if not filtered_transactions:
        print(f"No {transaction_type} transactions found.")
        return

    product_quantities = Counter()
    for transaction in filtered_transactions:
        product_id = transaction['product_id']
        quantity = transaction['quantity']
        product_quantities[product_id] += quantity

    product_names = {product['id']: product['name'] for product in load_data_from_file('products', param_key='all')}

    product_ids = list(product_quantities.keys())
    quantities = list(product_quantities.values())
    labels = [product_names[product_id] for product_id in product_ids]

    plt.figure(figsize=(10, 6))
    plt.bar(labels, quantities, color='skyblue')
    plt.xlabel('Products')
    plt.ylabel('Quantity')
    plt.title(f'Most {transaction_type.capitalize()}ed Products')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Save the chart to the diagram directory
    chart_path = os.path.join(diagram_dir, file_name)
    plt.savefig(chart_path)
    print(f"Chart saved as {chart_path}")


# Example usage
# generate_transaction_chart(transaction_type='export', file_name='export_chart.png')  # For export transactions
# generate_transaction_chart(transaction_type='import', file_name='import_chart.png')  # For import transactions