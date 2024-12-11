import json
from data import load_data_from_file, save_data_to_file, update_data


def add_warehouse():
    warehouse={
        "id": 0,
        "name": "",
        "location": "",
        "capacity": "",
        "current_capacity": 0
    }
    last_warehouse_id = load_data_from_file(file_name='warehouses', param_key='id')

    if last_warehouse_id is not None:
        warehouse["id"] = last_warehouse_id + 1
    else:
        warehouse["id"] = 1

    name = input("Name kiriting: ")
    location = input("Locatsiya kiriting: ")
    capacity = int(''.join(input("Capacity ni kiriting: ").split()))

    warehouse['name'] = name
    warehouse['location'] = location
    warehouse['capacity'] = capacity

    save_data_to_file(file_name='warehouses', data=warehouse)

    return "Warehouse Qushildi "



# def view
# def view_warehouse_capacity
# add_warehouse()
