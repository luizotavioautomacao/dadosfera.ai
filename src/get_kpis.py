import orchest
import os
import json
import pandas as pd

def convert_to_serializable(obj):
    """
    Converte objetos complexos em formatos serializáveis por JSON.
    
    Args:
        obj: Objeto a ser convertido.
    
    Returns:
        Objeto serializável.
    """
    if isinstance(obj, pd.Period):
        return str(obj)  # Converte pd.Period para string
    elif isinstance(obj, pd.DataFrame):
        return obj.reset_index().to_dict(orient='records')  # Converte DataFrame para lista de dicionários, sem índices
    elif isinstance(obj, float) and (obj != obj):  # Verifica NaN
        return None  # Substitui NaN por None
    return obj  # Retorna o objeto se não for um dos tipos anteriores
    
def save_kpis(kpis, output_directory):
    """
    Salva cada DataFrame em keys.key() como um arquivo .csv no diretório especificado.
    Salva cada Dicionário em keys.key() como um arquivo .json no diretório especificado.
    
    Args:
        kpis (dict): Dicionário contendo os Dicionários com DataFrames.
        output_directory (str): Diretório onde os arquivos .csv e .json serão salvos.
    """
    # Verifique se o diretório de saída existe, caso contrário, crie-o
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # file_path = os.path.join(output_directory, "kpis3.json")
    
    # Variável para armazenar tipos e dados
    kpis_json = {}

    # Itera sobre o dicionário de KPIs
    for key, value in kpis.items():
        # Identifica o tipo de cada valor e salva os dados em um dicionário
        item_type = type(value).__name__  # Obtém o nome do tipo

        if isinstance(value, pd.DataFrame):

            # Salva o DataFrame como CSV
            file_path = os.path.join(output_directory, f"{key}.csv")
            value.to_csv(file_path, index=False)

            # Lê o CSV de volta em um DataFrame
            df = pd.read_csv(file_path)

            # Serializa o DataFrame como JSON
            json_data = convert_to_serializable(df)

            # Adiciona os dados JSON ao dicionário kpis_json
            kpis_json[key] = json_data
            
        else:
            # Adiciona o valor ao dicionário de dados
            kpis_json[key] = value

    # Salva todos os dados como um único arquivo JSON
    json_file_path = os.path.join(output_directory, "kpis.json")
    with open(json_file_path, 'w') as file:
        json.dump(kpis_json, file, indent=4, default=str)

def convert_kpis_to_serializable(kpis):
    """
    Converte todos os DataFrames no dicionário `kpis` para um formato JSON serializável.
    """
    serializable_kpis = {}

    for key, value in kpis.items():
        # Usa a função `convert_to_serializable` para lidar com vários tipos
        serializable_kpis[key] = convert_to_serializable(value)
    
    return serializable_kpis

class DataLoader:
    def __init__(self, source=orchest):
        """
        Construtor da classe DataLoader.

        Args:
            source: A origem dos dados, por padrão 'orchest'.
        """
        self.source = source
        self.load_data_path='/data/luizotavioautomacao_build/kpis.json'

    def load_pipeline(self) -> dict:
        """
        Carrega os dados KPIs que estão no pipeline.

        Returns:
            dict: Dicionário contendo os KPIs.
        """
        data = self.source.get_inputs()  # Obter dados do pipeline
        kpis = data.get('kpis', {})  # Garantir que 'kpis' esteja presente, senão retorna vazio

        return kpis

    def load_data(self: str) -> dict:
        """ 
        Carrega os dados KPIs a partir de um arquivo JSON salvo em self.load_data_path (/data)

        Args:
            self.load_data_path (str): O caminho do arquivo JSON contendo os dados KPIs.

        Returns:
            dict: Dicionário contendo os KPIs.
        """
        # Verifica se o arquivo JSON existe
        if not os.path.exists(self.load_data_path):
            raise FileNotFoundError(f"O arquivo {self.load_data_path} não foi encontrado.")
        
        # Lê o conteúdo do arquivo JSON e carrega os dados
        with open(self.load_data_path, 'r') as file:
            kpis = json.load(file)
        
        return kpis


class KpiHandler:
    def __init__(self, data_loader: DataLoader):
        """
        Construtor da classe KpiHandler.

        Args:
            data_loader (DataLoader): Instância responsável por carregar os dados.
        """
        self.data_loader = data_loader

    def get_kpis(self) -> dict:
        """
        Obtém os KPIs carregados do pipeline.

        Returns:
            dict: Dicionário contendo os KPIs processados.
        """
        kpis = self.data_loader.load_pipeline()
        return kpis

    def load_kpis(self) -> dict:
        """
        Obtém os KPIs carregados de /data.

        Returns:
            dict: Dicionário contendo os KPIs processados.
        """
        kpis = self.data_loader.load_data()
        return kpis

def get_kpis():
    """
    Função para obter os KPIs.

    Returns:
        dict: Dicionário contendo os KPIs processados.
    """
    data_loader = DataLoader() # Instanciar o carregador de dados    
    kpi_handler = KpiHandler(data_loader) # Instanciar o manipulador de KPIs
    return kpi_handler.get_kpis() # Buscar os KPIs

if __name__ == "__main__":

    # Código a ser executado quando o script é executado diretamente
    kpis = get_kpis()
    output_dir = "/data/luizotavioautomacao_build"
    save_kpis(kpis, output_dir)
    print('get_kpis.py success!')