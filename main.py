import json
import sys

def read_file(filename):
    with open(filename,'r') as file:
        orders = json.load(file)
    return orders

orders_file = sys.argv[1]
orders = read_file(orders_file)

