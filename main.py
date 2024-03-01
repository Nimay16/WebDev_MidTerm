"""Code for mid term project"""
import json
import sys

def read_file(filename):
    """Function for reading the Json file"""
    with open(filename,'r', encoding='utf-8') as file:
        orders = json.load(file)
    return orders

def process_orders(orders):
    """Function for processing the orders"""
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
    """Function for macking customer list Json file"""
    customer_dict = {phone: name for phone, name in customers.items()}
    with open('customers.json', 'w', encoding='utf-8') as file:
        json.dump(customer_dict, file, indent = 4)

def item_write(items):
    """Function for macking item list Json file"""
    with open('item.json', 'w', encoding='utf-8' ) as file:
        json.dump(items, file, indent = 4)

if __name__ == "__main__":
    orders_file = sys.argv[1]
    order_read = read_file(orders_file)
    customers_list, items_list = process_orders(order_read)
    customer_write(customers_list)
    item_write(items_list)
    print("Processing complete.")
