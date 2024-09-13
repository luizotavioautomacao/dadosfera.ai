import snowflake.connector
import pandas as pd
from typing import Dict, Union, Literal, List
import numpy as np
import orchest
import os
import sys
import json
import logging
#from dadosfera import *
from sklearn import datasets
#from dadosfera import Dadosfera#from utils.dadosfera import Dadosfera
#from dadosfera.services.maestro import get_data_assets, get_token

class DataLoader:
    def __init__(self, data_path: str):
        """
        Inicializa o DataLoader com o caminho dos dados.
        """
        self.data_path = data_path

    def load_data(self, table_names: List[str]) -> dict:
        """
        Carrega os dados dos arquivos CSV da pasta data e retorna um dicionário
        com os nomes das tabelas como chave e os DataFrames como valor.
        """
        data_tables = {}
        for table in table_names:
            csv_path = os.path.join(self.data_path, f"{table}.csv")
            if os.path.exists(csv_path):
                logging.info(f"Carregando dados do arquivo: {csv_path}")
                data_tables[table] = pd.read_csv(csv_path)
            else:
                logging.warning(f"Arquivo {csv_path} não encontrado.")
        return data_tables
    # def __init__(self, dadosfera):
    #     self.dadosfera = dadosfera

    # def load_data(self, table_names: List[str]) -> dict:
    #     """
    #     Carrega os dados do catálogo de tabelas fornecidas e retorna um dicionário
    #     com os nomes das tabelas como chave e os DataFrames como valor.
    #     """
    #     data_tables = {}
    #     for table in table_names:
    #         logging.info(f"Carregando dados da tabela: {table}")
    #         data_tables[table] = self.dadosfera.get_data_from_catalog(table)
    #     return data_tables

class DataFormatter:
    #def __init__(self):
        #pass

    @staticmethod
    def format_table(df: pd.DataFrame, date_columns: List[str] = None) -> pd.DataFrame:
        """
        Aplica o processamento padrão para uma tabela, incluindo:
        - Transformar a primeira linha em cabeçalho
        - Remover a linha que virou cabeçalho
        - Resetar o índice
        - Converter colunas de data, se aplicável
        """
        # df.columns = df.iloc[0] # transforma a primeira linha em cabeçalho
        # df = df[1:] # remove a linha que virou cabeçalho
        # df.reset_index(drop=True, inplace=True)
        
        if date_columns:
            for col in date_columns:
                if col in df.columns:
                    df[col] = pd.to_datetime(df[col])
        return df

class DataPipeline:
    #def __init__(self, dadosfera):
        #self.data_loader = DataLoader(dadosfera)
        #self.data_formatter = DataFormatter()
    def __init__(self, data_path: str):
        self.data_loader = DataLoader(data_path)
        self.data_formatter = DataFormatter()

    def execute_pipeline(self):
        
        # Listar os arquivos .cvs
        table_names = [
            'clients',
            'cities',
            'states',
            'products',
            'carts',
            'transactions',
            'deliveries',
            'behaviors'
        ]

        # Listar as tabelas catalogadas
        # table_names = [
        #     'TB__W18CHA__CLIENTS',
        #     'TB__A9JUQD__CITIES',
        #     'TB__YNWS4O__STATES',
        #     'TB__4H3FQM__PRODUCTS',
        #     'TB__B8S3J1__CARTS',
        #     'TB__4ZCFGN__TRANSACTIONS',
        #     'TB__7Z8Y33__DELIVERY',
        #     'TB__RGGHTP__BEHAVIORS'
        # ]

        # Carregar os dados
        data_tables = self.data_loader.load_data(table_names)

        # Formatando os dados .cvs
        data_tables['clients'] = self.data_formatter.format_table(data_tables['clients'], ['LastVisit'])
        data_tables['carts'] = self.data_formatter.format_table(data_tables['carts'], ['AddedDate'])
        data_tables['transactions'] = self.data_formatter.format_table(data_tables['transactions'], ['Date'])
        data_tables['deliveries'] = self.data_formatter.format_table(data_tables['deliveries'], ['DeliveryDate'])

        # Formatando os dados catalogados
        # data_tables['TB__W18CHA__CLIENTS'] = self.data_formatter.format_table(data_tables['TB__W18CHA__CLIENTS'], ['LastVisit'])
        # data_tables['TB__B8S3J1__CARTS'] = self.data_formatter.format_table(data_tables['TB__B8S3J1__CARTS'], ['AddedDate'])
        # data_tables['TB__4ZCFGN__TRANSACTIONS'] = self.data_formatter.format_table(data_tables['TB__4ZCFGN__TRANSACTIONS'], ['Date'])
        # data_tables['TB__7Z8Y33__DELIVERY'] = self.data_formatter.format_table(data_tables['TB__7Z8Y33__DELIVERY'], ['DeliveryDate'])

        # Retornar os dados processados ou salvá-los
        return data_tables

class DataSaver:
    def save(self, data_dict: dict):
        logging.info("Salvando todas as tabelas em um único output.")
        orchest.output(data_dict, name="all_tables")

# #Problema ao salvar as tabelas dentro do for!
# class DataSaver:
#     def save(self, data_dict: dict):
#         for name, df in data_dict.items():
#             if df is not None and not df.empty:
#                 print(f"Salvando tabela: {name}")
#                 orchest.output(df, name=name)
#                 #dadosfera_utils.output(df, name=name)
#             else:
#                 print(f"Tabela {name} está vazia ou None.")

if __name__ == "__main__":

    # Inicializando a pipeline com o caminho dos dados CSV
    data_path = "../get-data-csv" 
    pipeline = DataPipeline(data_path=data_path)
    
    # Inicializando a pipeline
    # pipeline = DataPipeline(dadosfera=Dadosfera())
    
    # Executando o pipeline
    processed_data = pipeline.execute_pipeline()
    print(processed_data.keys())
    
    # Salvando os dados processados
    data_saver = DataSaver()
    data_saver.save(processed_data)
    
    print(processed_data["clients"].head())
    processed_data["deliveries"].head()
