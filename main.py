
items = [
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


def menu():
    while True:
        user_input = input("What would you like to do?: ")

        if user_input == 'exit':
            break
        elif user_input == 'show':
            get_items()
        elif user_input == 'add':
            add_item()
        elif user_input == 'sell':
            sell_item()
        elif user_input == 'show_revenue':
            show_revenue()


def get_items():
    table_header = f"{'l.p.':<5} {'Name':<10} {'Quantity':<10} {'Unit':<8} {'Unit Price (PLN)':<10}\n" \
                   f"{'-'*5} {'-'*10} {'-'*10} {'-'*8} {'-'*10}"

    print(table_header)

    for i, item in enumerate(items, start=1):
        print(f"{i:<5} {item['Name']:<10} {item['Quantity']:<10} {item['Unit']:<8} {item['Unit Price']:<10.2f}")


# def add_item(name: str, quantity: float, unit_name: str, unit_price: float):
def add_item():
    print("Adding an item to the warehouse...")
    item_name = input("Item name: ")
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


def sell_item():
    print("Selling an item...")
    item_name = input("Item name: ")
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
    Add note to sold_items list about selling an item.

    :param name:
    :param quantity:
    :param unit_name:
    :param unit_price:
    :return:
    """
    sold_item = {
        'Name': name,
        'Quantity': quantity,
        'Unit': unit_name,
        'Unit Price': unit_price,
    }
    sold_items.append(sold_item)


def get_costs():
    """
    Będzie zliczać wartość przedmiotów aktualnie znajdujących się w magazynie (na liście items).

    :return:
    """
    cost = sum(item['Quantity'] * item['Unit Price'] for item in items)
    return cost


def get_income():
    """
    będzie w analogiczny sposób zliczać wartość sprzedanych przedmiotów z listy sold_items.

    :return:
    """
    income = sum(item['Quantity'] * item['Unit Price'] for item in sold_items)
    return income


def show_revenue():
    """
    wyświetli przychody (policzone przez get_income), koszty (policzone przez get_costs) i zarobek,
    czyli różnicę między przychodem a kosztami.

    :return:
    """
    print("Revenue breakdown (PLN):")
    print(f"{'Income':<10}: {get_income():>10.2f}")
    print(f"{'Cost':<10}: {get_costs():>10.2f}")
    print("-" * 22)
    print(f"{'Revenue':<10}: {get_income() - get_costs():>10.2f}")



if __name__ == "__main__":
    menu()

