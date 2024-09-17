import pandas as pd
from faker import Faker
import random
import os
from datetime import datetime
#import orchest

# Initial Setup
fake = Faker()
output = "data/"
n_client = 163495
n_product = 123
n_transaction = 400000
n_behavior = 500000
start_year = 2019
end_year = datetime.now().year
data_in_pipeline=False

# Ensure the directory exists
os.makedirs(output, exist_ok=True)

class DataGenerator:
    """Responsible for generating different types of synthetic data."""

    def __init__(self):
        self.fake = Faker()
        self.n_client = n_client
        self.start_year = start_year
        self.end_year = end_year

    def generate_customer(self, year, states_df, cities_df):
        """Generate client data."""
        # Create a mapping of state code to cities
        state_to_cities = cities_df.groupby('COD UF')['NOME'].apply(list).to_dict()
        state_code = random.choice(states_df['COD'])
        state = states_df[states_df['COD'] == state_code].iloc[0]
        cities = state_to_cities.get(state_code, [])
        city = random.choice(cities)
        return {
                'CustomerId': self.fake.uuid4(),
                'Name': self.fake.name(),
                'Age': random.randint(18, 70),
                'Gender': random.choice(['Masculino', 'Feminino']),
                'City': city,
                'State': state['SIGLA'],
                'Profession': self.fake.job(),
                'RegistrationDate': self.fake.date_between(start_date=datetime(year, 1, 1),end_date=datetime(year, 12, 31)),
                'LastVisit': self.fake.date_this_year(),
                'PurchaseHistory': random.choice(['Baixo', 'Médio', 'Alto']),
                'Preferences': random.choice(['Tecnologia', 'Moda', 'Decoração de Casa', 'Livros', 'Esportes']),
            }

    def generate_clients_over_time(self, states_df, cities_df):
        """Generate client data over time, gradually increasing the number of clients each year."""

        years = list(range(self.start_year, self.end_year + 1))  # Lista dos anos de início ao atual
        clients_per_year = self._calculate_clients_per_year(years)

        clients = []
        for year in years:
            num_clients_this_year = clients_per_year[year]
            for _ in range(num_clients_this_year):
                client = self.generate_customer(year, states_df, cities_df)
                clients.append(client)

        return pd.DataFrame(clients)
    

    def _calculate_clients_per_year(self, years):
        """Distribute the total number of clients over the years, gradually increasing."""
        num_years = len(years)
        # Exemplo de crescimento exponencial suave: cada ano tem mais clientes que o anterior
        growth_rate = 1.5  # Aumenta o número de clientes a cada ano por essa taxa
        base_clients = self.n_client // ((growth_rate ** num_years - 1) / (growth_rate - 1))

        clients_per_year = {}
        for i, year in enumerate(years):
            clients_per_year[year] = int(base_clients * (growth_rate ** i))

        # Ajusta para garantir que a soma final seja igual ao total de clientes
        total_assigned_clients = sum(clients_per_year.values())
        if total_assigned_clients != self.n_client:
            difference = self.n_client - total_assigned_clients
            clients_per_year[years[-1]] += difference  # Ajusta no último ano

        return clients_per_year

    
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
    
    def generate_transactions(self, clients, products, total_transactions):
        """Generate transaction data, scaling the number by year."""
        transactions = []
        year_distribution = {2019: 0.05, 2020: 0.10, 2021: 0.15, 2022: 0.25, 2023: 0.30, 2024: 0.15}
        for year, proportion in year_distribution.items():
            year_transactions = int(total_transactions * proportion)
            for _ in range(year_transactions):
                transactions.append({
                    'TransactionId': self.fake.uuid4(),
                    'CustomerId': random.choice(clients)['CustomerId'],
                    'ProductId': random.choice(products)['ProductId'],
                    'Date':  self.fake.date_between(start_date=datetime(year, 1, 1),end_date=datetime(year, 12, 31)),
                    'Quantity': random.randint(1, 3),
                    'TotalValue': round(random.uniform(5, 500), 2),
                    'PaymentMethod': random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer', 'Pix']),
                    'CouponApplied': random.choice([True, False]),
                    'Latitude': self.generate_latitude(),
                    'Longitude': self.generate_longitude()
                })
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
        deliveries = []
        
        for transaction in transactions:
            # Ensure the transaction date is a date object
            transaction_date = transaction['Date'].date() if isinstance(transaction['Date'], datetime) else transaction['Date']
            
            # Ensure the start_date is not after today's date
            end_date = datetime.today().date()
            start_date = min(transaction_date, end_date)  # Take the earlier of the two

            deliveries.append({
                'DeliveryId': self.fake.uuid4(),
                'TransactionId': transaction['TransactionId'],
                'CustomerId': transaction['CustomerId'],
                'DeliveryDate': self.fake.date_between(start_date=start_date, end_date=end_date),
                'DeliveryStatus': random.choice(['Pending', 'Shipped', 'Delivered', 'Cancelled']),
                'Carrier': random.choice(['DHL', 'FedEx', 'UPS', 'USPS']),
                'ShippingCost': round(random.uniform(5, 50), 2)
            })
        
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
    
    def generate_latitude(self):
        """Generate a random latitude."""
        return round(random.uniform(-33.7500, 5.2718), 6)

    def generate_longitude(self):
        """Generate a random longitude."""
        return round(random.uniform(-73.9922, -34.7931), 6)
    
    def add_lat_long_to_cities(self, cities_df):
        """Adiciona latitude e longitude sintéticas aos municípios."""
        cities_df['Latitude'] = cities_df.apply(lambda _: self.generate_latitude(), axis=1)
        cities_df['Longitude'] = cities_df.apply(lambda _: self.generate_longitude(), axis=1)
        return cities_df

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

    def save_pipeline(self, data_dict: dict):
        """Save all tables to files and as Orchest output."""

        # Output the entire data dictionary to Orchest
        #orchest.output(data_dict, name="all_tables")

def main():
    generator = DataGenerator()
    saver = DataSaver(output)

    # Generate data
    states_df = pd.read_csv("brasil/estados.csv")
    cities_df = generator.add_lat_long_to_cities(pd.read_csv("brasil/municipios.csv"))
    clients_df = generator.generate_clients_over_time(states_df, cities_df)
    products_df = generator.generate_products(n_product)
    cart_df = generator.generate_cart(clients_df.to_dict('records'), products_df.to_dict('records'), n_transaction)
    transactions_df = generator.generate_transactions(clients_df.to_dict('records'), products_df.to_dict('records'), n_transaction)
    delivery_df = generator.generate_delivery(transactions_df.to_dict('records'))
    behavior_df = generator.generate_behavior(clients_df.to_dict('records'), n_behavior)

    if(data_in_pipeline):
        data_dict = {
            'clients': clients_df,
            'products': products_df,
            'transactions': transactions_df,
            'carts': cart_df,
            'deliveries': delivery_df,
            'behaviors': behavior_df,
            'states': states_df,
            'cities': cities_df
        }
        saver.save_pipeline(data_dict)

    else: # .cvs
        save_csv = [
            (clients_df, 'clients.csv'),
            (products_df, 'products.csv'),
            (transactions_df, 'transactions.csv'),
            (cart_df, 'carts.csv'),
            (delivery_df, 'deliveries.csv'),
            (behavior_df, 'behaviors.csv'),
            (states_df, 'states.csv'),
            (cities_df, 'cities.csv')
            ]

        # Itera sobre os dataframes e arquivos e salva cada um
        for df, filename in save_csv:
            saver.save_to_csv(df, filename)

if __name__ == "__main__":
    main()
