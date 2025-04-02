import random

# Define the items and their quantities
items = ['item1', 'item2', 'item3']
orders = []

# Generate 1000 orders
for _ in range(1000):
    order = {}
    for item in items:
        quantity = random.randint(1, 100)  # Random quantity between 1 and 100
        order[item] = quantity
    orders.append(order)

# Write the orders to a text file
with open('orders.txt', 'w') as file:
    for order in orders:
        order_str = ', '.join([f"{item}:{quantity}" for item, quantity in order.items()])
        file.write(order_str + '\n')

print("Orders have been generated and written to orders.txt")