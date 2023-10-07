import csv
import sys
from typing import List, Dict, Union

WAREHOUSE_CSV: str = 'warehouse.csv'
SALES_CSV: str = 'sales.csv'

items: List[Dict[str, Union[str, int, float]]] = [
    {
        'Name': 'Milk',
        'Quantity': 120,
        'Unit': 'l',
        'Unit Price': 2.3,
    },
    {
        'Name': 'Sugar',
        'Quantity': 1000,
        'Unit': 'kg',
        'Unit Price': 3,
    },
    {
        'Name': 'Flour',
        'Quantity': 12000,
        'Unit': 'kg',
        'Unit Price': 1.2,
    }
]

sold_items = []


def menu() -> None:
    """
    Allows the user to input commands for warehouse management.

    :return: None
    """
    print("For help, enter 'help'.")

    while True:
        user_input = input("What would you like to do?: ")
        user_input = user_input.lower()

        if user_input == 'exit':
            break
        elif user_input == 'help':
            menu_help()
        elif user_input == 'show':
            get_items()
        elif user_input == 'add':
            add_item()
        elif user_input == 'sell':
            sell_item()
        elif user_input == 'revenue':
            show_revenue()
        elif user_input == 'save':
            export_items_to_csv()
            export_sales_to_csv()
        elif user_input == 'load':
            load_items_from_csv()
            load_sales_from_csv()
        else:
            print("Wrong command.")


def menu_help() -> None:
    """
    Prints the available commands in alphabetical order.

    :return: None
    """
    commands = ['exit', 'help', 'show', 'add', 'sell', 'revenue', 'save', 'load']
    print(f"Command list: {sorted(commands)}")


def get_items() -> None:
    """
    Prints table for the user containing information about items in stock.

    :return: None
    """
    table_header = f"{'l.p.':<5} {'Name':<10} {'Quantity':>10} {'Unit':>8} {'Unit Price (PLN)':>10}\n" \
                   f"{'-'*5} {'-'*10} {'-'*10} {'-'*8} {'-'*16}"

    print(table_header)

    for i, item in enumerate(items, start=1):
        print(f"{i:<5} {item['Name']:<10} {item['Quantity']:>10} {item['Unit']:>8} {item['Unit Price']:>10.2f}")


def add_item() -> None:
    """
    Takes input about the new item and adds it to the warehouse.

    :return: None
    """
    print("Adding an item to the warehouse...")
    item_name = input("Item name: ").capitalize()
    item_quantity = int(input("Item quantity: "))
    item_unit = input("Item unit of measure: ")
    item_price = float(input("Item price in PLN: "))
    new_item = {
        'Name': item_name,
        'Quantity': item_quantity,
        'Unit': item_unit,
        'Unit Price': item_price,
    }
    items.append(new_item)
    print("New item added!")


def sell_item() -> None:
    """
    Takes input about the item being sold and adds it to the list of sold items.

    :return: None
    """
    print("Selling an item...")
    item_name = input("Item name: ").capitalize()
    item_quantity = int(input("Quantity to sell: "))
    flag = True  # if item was not found inform the user
    for item in items:
        if item['Name'] == item_name:
            item['Quantity'] -= item_quantity
            print(f"Successfully sold {item_quantity} {item['Unit']} of {item_name}.")
            print("Displaying the current warehouse status...")
            get_items()
            flag = False
            update_sold_items(name=item_name, quantity=item_quantity, unit_name=item['Unit'],
                              unit_price=item['Unit Price'])
    if flag:
        print(f"{item_name} was not found. Aborting...")


def update_sold_items(name: str, quantity: float, unit_name: str, unit_price: float) -> None:
    """
    Adds the sold item to the list of sold items.

    :param name: item name
    :param quantity: item quantity
    :param unit_name: item measurement unit
    :param unit_price: item price per one unit of measurement
    :return: None
    """
    sold_item = {
        'Name': name,
        'Quantity': quantity,
        'Unit': unit_name,
        'Unit Price': unit_price,
    }
    sold_items.append(sold_item)


def get_costs() -> float:
    """
    Sums up the price of all available items in stock.

    :return: the price of all available items in stock
    """
    cost = sum(item['Quantity'] * item['Unit Price'] for item in items)
    return cost


def get_income() -> float:
    """
    Sums up the price of all sold items.

    :return: the price of all sold items
    """
    income = sum(item['Quantity'] * item['Unit Price'] for item in sold_items)
    return income


def show_revenue() -> None:
    """
    Prints the income, cost and revenue.

    :return: None
    """
    print("Revenue breakdown (PLN):")
    print(f"{'Income':<10}: {get_income():>10.2f}")
    print(f"{'Cost':<10}: {get_costs():>10.2f}")
    print("-" * 22)
    print(f"{'Revenue':<10}: {get_income() - get_costs():>10.2f}")


def export_items_to_csv(warehouse_csv: str = WAREHOUSE_CSV) -> None:
    """
    Export warehouse data to a CSV file.

    :param warehouse_csv: The path to the CSV file where the items will be exported. Defaults to 'warehouse.csv'.
    :return: None
    """
    print(f"Saving warehouse data to {warehouse_csv}")
    with open(warehouse_csv, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Quantity', 'Unit', 'Unit Price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel')

        writer.writeheader()
        for item in items:
            writer.writerow({
                'Name': item['Name'],
                'Quantity': item['Quantity'],
                'Unit': item['Unit'],
                'Unit Price': item['Unit Price'],
            })
    print("Done!")


def export_sales_to_csv(sales_csv: str = SALES_CSV) -> None:
    """
    Export sold items data to a CSV file.

    :param sales_csv: The path to the CSV file where the items will be exported. Defaults to 'sales.csv'.
    :return: None
    """
    print(f"Saving sales data to {sales_csv}")

    with open(sales_csv, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Quantity', 'Unit', 'Unit Price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel')

        writer.writeheader()
        for item in sold_items:
            writer.writerow({
                'Name': item['Name'],
                'Quantity': item['Quantity'],
                'Unit': item['Unit'],
                'Unit Price': item['Unit Price'],
            })
    print("Done!")


def load_items_from_csv(warehouse_csv: str = WAREHOUSE_CSV) -> None:
    """
    Import warehouse data from a CSV file.

    :param warehouse_csv: The path to the CSV file from which the items will be imported. Defaults to 'warehouse.csv'.
    :return: None
    """
    items.clear()
    print(f"Loading warehouse data from {warehouse_csv}.")

    with open(warehouse_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            items.append({
                'Name': row['Name'],
                'Quantity': int(row['Quantity']),
                'Unit': row['Unit'],
                'Unit Price': float(row['Unit Price']),
                })
    print("Done!")


def load_sales_from_csv(sales_csv: str = SALES_CSV) -> None:
    """
    Import sold items data from a CSV file.

    :param sales_csv: The path to the CSV from which the items will be imported. Defaults to 'sales.csv'.
    :return: None
    """
    sold_items.clear()
    print(f"Loading sales data from {sales_csv}.")

    with open(sales_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sold_items.append({
                'Name': row['Name'],
                'Quantity': int(row['Quantity']),
                'Unit': row['Unit'],
                'Unit Price': float(row['Unit Price']),
                })
    print("Done!")


def startup() -> None:
    """
    Initialize the application by loading warehouse and sold items data from their CSV files.

    This function can accept command-line arguments to specify custom CSV file paths for warehouse
    and sales data.

    :return: None
    """
    global WAREHOUSE_CSV, SALES_CSV
    if len(sys.argv) > 1:  # at startup allow loading from user files
        print("Command-line arguments detected. Loading custom CSV file paths...")
        WAREHOUSE_CSV = sys.argv[1]
        SALES_CSV = sys.argv[2]
    load_items_from_csv()
    load_sales_from_csv()


if __name__ == "__main__":
    startup()
    menu()


