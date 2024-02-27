import json
import sys

def read_file(filename):
    with open(filename,'r') as file:
        orders = json.load(file)
    return orders

def process_orders(orders):
    customers = {}
    items = {}

    for order in orders:
        phone_no = order['phone']
        name = order['name']
        
        if phone_no not in customers:
            customers[phone_no] = name

        for item in order['items']:
            item_name = item['name']
            item_price = item['price']

            if item_name not in items:
                items[item_name] = {'price': item_price, 'orders':1}

            else:
                items[item_name]['orders'] += 1


    return customers, items 


def customer_write(customers):
    customer_list = {phone: name for phone, name in customers.items()}
    with open('customers.json', 'w') as file:
        json.dump(customer_list, file, indent=4)






orders_file = sys.argv[1]
orders = read_file(orders_file)
customers, items = process_orders(orders)
customer_write(customers)
print("Processing complete.")

