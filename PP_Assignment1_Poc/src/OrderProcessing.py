import concurrent.futures
import time
from pathlib import Path

# Define a global constant for the delay
DELAY = 0.01

class Inventory:
    def __init__(self):
        self.items = {
            'item1': {'price': 100, 'stock': 500000},
            'item2': {'price': 200, 'stock': 500000},
            'item3': {'price': 150, 'stock': 500000},
        }

    def check_stock(self, item, quantity):
        time.sleep(DELAY)  # Using global delay
        if item in self.items and self.items[item]['stock'] >= quantity:
            return True
        return False

    def update_stock(self, item, quantity):
        time.sleep(DELAY)  # Using global delay
        if self.check_stock(item, quantity):
            self.items[item]['stock'] -= quantity
            return True
        return False

class Order:
    def __init__(self, inventory):
        self.inventory = inventory
        self.orders = []

    def validate_order(self, order):
        time.sleep(DELAY)  # Using global delay
        for item, quantity in order.items():
            if not self.inventory.check_stock(item, quantity):
                return False
        return True

    def process_order(self, order):
        time.sleep(DELAY)  # Using global delay
        if self.validate_order(order):
            total_price = 0
            for item, quantity in order.items():
                if self.inventory.update_stock(item, quantity):
                    total_price += self.inventory.items[item]['price'] * quantity
            self.orders.append(order)
            return f"Order# {item} processed successfully. Total price: ${total_price}"
        return "Order validation failed. One or more items are out of stock."

def process_orders_in_parallel(order_system, orders):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(order_system.process_order, order) for order in orders]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

def process_orders_sequentially(order_system, orders):
    for order in orders:
        print(order_system.process_order(order))

def read_orders_from_file(file_path):
    orders = []
    with open(file_path, 'r') as file:
        for line in file:
            order = {}
            items = line.strip().split(', ')
            for item in items:
                name, quantity = item.split(':')
                order[name] = int(quantity)
            orders.append(order)
    return orders

# Example usage
inventory = Inventory()
order_system = Order(inventory)

# Read orders from file
orders = read_orders_from_file(Path(__file__).parent.parent / 'input' / 'orders.txt')

# Process orders sequentially and measure time
start_time = time.time()
process_orders_sequentially(order_system, orders)
sequential_time = time.time() - start_time

# Process orders in parallel and measure time
start_time = time.time()
process_orders_in_parallel(order_system, orders)
parallel_time = time.time() - start_time

print(f"Total time taken for sequential execution: {sequential_time:.2f} seconds")

print(f"Total time taken for parallel execution: {parallel_time:.2f} seconds")
