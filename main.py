
items = [
    {
        'Name': 'Milk',
        'Quantity': 120,
        'Unit': 'l',
        'Unit Price': 2.3
    },
{
        'Name': 'Sugar',
        'Quantity': 1000,
        'Unit': 'kg',
        'Unit Price': 3
    },
{
        'Name': 'Flour',
        'Quantity': 12000,
        'Unit': 'kg',
        'Unit Price': 1.2
    }
]


def menu():
    while True:
        user_input = input("What would you like to do?: ")

        if user_input == 'exit':
            break
        elif user_input == 'show':
            get_items()


def get_items():
    table_header = f"{'l.p.':<5} {'Name':<10} {'Quantity':<10} {'Unit':<5} {'Unit Price':<10}\n" \
                   f"{'-'*5} {'-'*10} {'-'*10} {'-'*5} {'-'*10}"

    print(table_header)

    for i, item in enumerate(items, start=1):
        print(f"{i:<5} {item['Name']:<10} {item['Quantity']:<10} {item['Unit']:<5} {item['Unit Price']:<10.2f}")


if __name__ == "__main__":
    menu()

