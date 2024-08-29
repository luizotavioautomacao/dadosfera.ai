import pandas as pd
from faker import Faker
import random
import os

# Initial Setup
fake = Faker()
output = "output/"
n_client=10000
n_product=500
n_transaction=100000
n_behavior=200000

# Ensure the directory exists
os.makedirs(output, exist_ok=True)


class DataGenerator:
    """Responsible for generating different types of synthetic data."""

    def __init__(self):
        self.fake = Faker()

    def generate_clients(self, num_clients):
        """Generate client data."""
        clients = [{
            'CustomerId': self.fake.uuid4(),
            'Name': self.fake.name(),
            'Age': random.randint(18, 70),
            'Gender': random.choice(['Masculino', 'Feminino']),
            'Location': self.fake.city(),
            'Profession': self.fake.job(),
            'LastVisit': self.fake.date_this_year(),
            'PurchaseHistory': random.choice(['Baixo', 'Médio', 'Alto']),
            'Preferences': random.choice(['Tecnologia', 'Moda', 'Decoração de Casa', 'Livros', 'Esportes']),
        } for _ in range(num_clients)]
        return pd.DataFrame(clients)
    
    def generate_categories(self):
        """Generate category data."""
        categories = ['Ar e Ventilação', 'Artesanato', 'Artigos para Festa', 'Áudio', 'Automotivo', 'Bebê', 
                      'Beleza e Perfumaria', 'Bem-estar Sexual', 'Brinquedos', 'Cama, Mesa e Banho', 'Câmeras e Drones', 
                      'Casa e Construção', 'Casa Inteligente', 'Celulares e Smartphones', 'Colchões', 
                      'Comércio e Indústria', 'Cursos', 'Decoração', 'Eletrodomésticos', 'Eletroportáteis', 
                      'Esporte e Lazer', 'Ferramentas', 'Filmes e Séries', 'Flores e Jardim', 'Games', 
                      'Informática', 'Instrumentos Musicais', 'Livros', 'Mercado', 'Moda', 'Móveis', 'Música e Shows', 
                      'Natal', 'Papelaria', 'Pet Shop', 'Religião e Espiritualidade', 'Relógios', 
                      'Saúde e Cuidados Pessoais', 'Serviços', 'Suplementos Alimentares', 'Tablet, Samsung, Infantil, Ipad e mais', 
                      'Telefonia Fixa', 'TV e Vídeo', 'Utilidades Domésticas']
        
        category_data = [{'CategoryId': f'C{i:03d}', 'CategoryName': category} for i, category in enumerate(categories, start=1)]
        return pd.DataFrame(category_data)
    
    def generate_login_data(self, clients):
        """Generate login data for clients."""
        logins = [{
            'CustomerId': client['CustomerId'],
            'Email': client['Email'],
            'Password': client['Password'],
            'LastLogin': self.fake.date_time_this_year()
        } for client in clients]
        return pd.DataFrame(logins)

    def generate_products(self, num_products):
        """Generate product data."""
        categories = ['Tech', 'Fashion', 'Home Decor', 'Books', 'Sports']
        products = [{
            'ProductId': f'P{i:03d}',
            'Name': self.fake.word().title(),
            'Category': random.choice(categories),
            'Price': round(random.uniform(5, 500), 2),
            'Stock': random.randint(10, 500),
            'Description': self.fake.sentence(),
            'Rating': random.uniform(1, 5),
        } for i in range(1, num_products + 1)]
        return pd.DataFrame(products)

    def generate_transactions(self, clients, products, num_transactions):
        """Generate transaction data."""
        transactions = [{
            'TransactionId': self.fake.uuid4(),
            'CustomerId': random.choice(clients)['CustomerId'],
            'ProductId': random.choice(products)['ProductId'],
            'Date': self.fake.date_between(start_date='-1y', end_date='today'),
            'Quantity': random.randint(1, 3),
            'TotalValue': round(random.uniform(5, 500), 2),
            'PaymentMethod': random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer', 'Pix']),
            'CouponApplied': random.choice([True, False])
        } for _ in range(num_transactions)]
        return pd.DataFrame(transactions)

    def generate_cart(self, clients, products, num_carts):
        """Generate cart data."""
        carts = [{
            'CartId': self.fake.uuid4(),
            'CustomerId': random.choice(clients)['CustomerId'],
            'ProductId': random.choice(products)['ProductId'],
            'AddedDate': self.fake.date_time_this_year(),
            'Quantity': random.randint(1, 5),
            'IsPurchased': random.choice([True, False])
        } for _ in range(num_carts)]
        return pd.DataFrame(carts)

    def generate_delivery(self, transactions):
        """Generate delivery data."""
        deliveries = [{
            'DeliveryId': self.fake.uuid4(),
            'TransactionId': transaction['TransactionId'],
            'CustomerId': transaction['CustomerId'],
            'DeliveryDate': self.fake.date_between(start_date=transaction['Date'], end_date='today'),
            'DeliveryStatus': random.choice(['Pending', 'Shipped', 'Delivered', 'Cancelled']),
            'Carrier': random.choice(['DHL', 'FedEx', 'UPS', 'USPS']),
            'ShippingCost': round(random.uniform(5, 50), 2)
        } for transaction in transactions]
        return pd.DataFrame(deliveries)

    def generate_behavior(self, clients, num_behaviors):
        """Generate behavioral data."""
        behaviors = [{
            'CustomerId': random.choice(clients)['CustomerId'],
            'DateTime': self.fake.date_time_this_year(),
            'PageVisited': random.choice(['Home', 'Product', 'Category', 'Cart']),
            'TimeSpent': round(random.uniform(5, 300), 2),
            'LinkClicked': random.choice([True, False])
        } for _ in range(num_behaviors)]
        return pd.DataFrame(behaviors)


class DataSaver:
    """Responsible for saving data to files."""

    def __init__(self, output_directory):
        self.output_directory = output_directory

    def save_to_csv(self, dataframe, filename):
        """Save DataFrame to CSV file if it doesn't already exist."""
        filepath = os.path.join(self.output_directory, filename)
        if not os.path.exists(filepath):
            dataframe.to_csv(filepath, index=False)
            print(f"File '{filepath}' created successfully.")
        else:
            print(f"File '{filepath}' already exists. Skipping save.")

def main():
    generator = DataGenerator()
    saver = DataSaver(output)

    # Generate data
    clients_df = generator.generate_clients(n_client)
    products_df = generator.generate_products(n_product)
    transactions_df = generator.generate_transactions(clients_df.to_dict('records'), products_df.to_dict('records'), n_transaction)
    cart_df = generator.generate_cart(clients_df.to_dict('records'), products_df.to_dict('records'), n_transaction)
    delivery_df = generator.generate_delivery(transactions_df.to_dict('records'))
    behavior_df = generator.generate_behavior(clients_df.to_dict('records'), n_behavior)

    # Save data
    saver.save_to_csv(clients_df, 'clients.csv')
    saver.save_to_csv(products_df, 'products.csv')
    saver.save_to_csv(transactions_df, 'transactions.csv')
    saver.save_to_csv(cart_df, 'cart.csv')
    saver.save_to_csv(delivery_df, 'delivery.csv')
    saver.save_to_csv(behavior_df, 'behavior.csv')


if __name__ == "__main__":
    main()

