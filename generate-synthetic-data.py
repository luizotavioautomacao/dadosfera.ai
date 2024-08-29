import pandas as Pandas
from faker import Faker
import random
import os

# Initial Setup
fake = Faker()
num_clients = 10000
num_transactions = 100000
output = "output/"

# Ensure the directory exists
os.makedirs(output, exist_ok=True)

# Function to save DataFrame to CSV if it does not already exist
def save_to_csv(dataframe, filename):
    filepath = os.path.join(output, filename)  # Combina o diretório de saída com o nome do arquivo
    if not os.path.exists(filepath):  # Verifica se o arquivo existe
        dataframe.to_csv(filepath, index=False)
        print(f"File '{filepath}' created successfully.")
    else:
        print(f"File '{filepath}' already exists. Skipping save.")

# Customer Generation
clients = []
for _ in range(num_clients):
    clients.append({
        'CustomerId': fake.uuid4(),
        'Name': fake.name(),
        'Age': random.randint(18, 70),
        'Gender': random.choice(['Male', 'Female']),
        'Location': fake.city(),
        'Profession': fake.job(),
        'LastVisit': fake.date_this_year(),
        'PurchaseHistory': random.choice(['Low', 'Medium', 'High']),
        'Preferences': random.choice(['Tech', 'Fashion', 'Home Decor', 'Books', 'Sports']),
    })

clients_df = Pandas.DataFrame(clients)

# Product Generation
products = []
categories = ['Tech', 'Fashion', 'Home Decor', 'Books', 'Sports']
for i in range(1, 501):  # 500 products
    products.append({
        'ProductId': f'P{i:03d}',
        'Name': fake.word().title(),
        'Category': random.choice(categories),
        'Price': round(random.uniform(5, 500), 2),
        'Stock': random.randint(10, 500),
        'Description': fake.sentence(),
        'Rating': random.uniform(1, 5),
    })

products_df = Pandas.DataFrame(products)

# Transaction Generation
transactions = []
for _ in range(num_transactions):
    customer = random.choice(clients)
    product = random.choice(products)
    transactions.append({
        'TransactionId': fake.uuid4(),
        'CustomerId': customer['CustomerId'],
        'ProductId': product['ProductId'],
        'Date': fake.date_between(start_date='-1y', end_date='today'),
        'Quantity': random.randint(1, 3),
        'TotalValue': round(product['Price'] * random.randint(1, 3), 2),
        'PaymentMethod': random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer']),
        'CouponApplied': random.choice([True, False])
    })

transactions_df = Pandas.DataFrame(transactions)

# Cart (Shopping Bag) Generation
cart_data = []
for _ in range(num_transactions):  # Simulating cart data
    customer = random.choice(clients)
    product = random.choice(products)
    cart_data.append({
        'CartId': fake.uuid4(),
        'CustomerId': customer['CustomerId'],
        'ProductId': product['ProductId'],
        'AddedDate': fake.date_time_this_year(),
        'Quantity': random.randint(1, 5),
        'IsPurchased': random.choice([True, False])
    })

cart_df = Pandas.DataFrame(cart_data)

# Delivery Generation
delivery_data = []
for transaction in transactions:
    delivery_data.append({
        'DeliveryId': fake.uuid4(),
        'TransactionId': transaction['TransactionId'],
        'CustomerId': transaction['CustomerId'],
        'DeliveryDate': fake.date_between(start_date=transaction['Date'], end_date='today'),
        'DeliveryStatus': random.choice(['Pending', 'Shipped', 'Delivered', 'Cancelled']),
        'Carrier': random.choice(['DHL', 'FedEx', 'UPS', 'USPS']),
        'ShippingCost': round(random.uniform(5, 50), 2)
    })

delivery_df = Pandas.DataFrame(delivery_data)

# Behavioral Data Generation
behavior_data = []
for _ in range(num_transactions * 2):  # Navigation data
    customer = random.choice(clients)
    behavior_data.append({
        'CustomerId': customer['CustomerId'],
        'DateTime': fake.date_time_this_year(),
        'PageVisited': random.choice(['Home', 'Product', 'Category', 'Cart']),
        'TimeSpent': round(random.uniform(5, 300), 2),
        'LinkClicked': random.choice([True, False])
    })

behavior_df = Pandas.DataFrame(behavior_data)

# Save to CSV files
save_to_csv(clients_df, 'clients.csv')
save_to_csv(products_df, 'products.csv')
save_to_csv(transactions_df, 'transactions.csv')
save_to_csv(cart_df, 'cart.csv')
save_to_csv(delivery_df, 'delivery.csv')
save_to_csv(behavior_df, 'behavior.csv')
