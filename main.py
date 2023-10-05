
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
    if flag:
        print(f"{item_name} was not found. Aborting...")



if __name__ == "__main__":
    menu()

