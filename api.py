from flask import Flask, jsonify
import openai
import requests
import sys
import os

# Adiciona o diretório desejado ao PYTHONPATH
sys.path.append('/project-dir/src')

# Agora você pode importar o módulo
from get_kpis import KpiHandler, DataLoader

app = Flask(__name__)

# Configure a chave da API da OpenAI
# openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def welcome():
    env = os.getenv('FLASK_ENV', 'production') # isso significa que, se FLASK_ENV não estiver configurada, os.getenv retornará 'production'.
    return f'Flask is running in {env} mode.'
    # return "Welcome to my Flask application!"

@app.route('/test')
def test():
    return "connection_streamlit_flask: True!"

@app.route('/endpoint')
def endpoint():
    response = {
        "connection_streamlit_flask": True
    }
    return jsonify(response)

# @app.route('/catalog', methods=['GET'])
# def get_catalog():
#     """
#     Função para retornar dados da API de catálogo.
#     """

#     # Obtendo o token da URL
#     token = requests.args.get('token')

#     if not token:
#         return jsonify({"error": "Token is required"}), 400

#     catalog_data, status_code = fetch_catalog(token)
#     return jsonify(catalog_data), status_code

def fetch_catalog(token: str):
    """
    Função para buscar dados do catálogo usando o token fornecido.
    """
    try:
        # Substitua pela URL real da API de catálogo
        url = "https://maestro.dadosfera.ai/catalog"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "dadosfera-lang": "pt-BR",
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(url, headers=headers)

        # Levanta uma exceção para códigos de status HTTP de erro
        response.raise_for_status()

        return response.json(), response.status_code
    except requests.exceptions.HTTPError as http_err:
        # Trata erros HTTP
        return {"error": f"HTTP error occurred: {http_err}"}, response.status_code
    except requests.exceptions.RequestException as req_err:
        # Trata erros de solicitação
        return {"error": f"Request error occurred: {req_err}"}, 500
    except Exception as e:
        # Trata outros erros inesperados
        return {"error": f"An unexpected error occurred: {e}"}, 500

@app.route('/kpis', methods=['GET'])
def kpis():
    """
    Função para obter os KPIs.
    """
    try:
        data_loader = DataLoader()  # Instancia DataLoader
        kpi_handler = KpiHandler(data_loader)  # Instancia KpiHandler
        kpis = kpi_handler.load_kpis()  # Obtém KPIs

        return jsonify(kpis), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# @app.route('/openai')
# def get_openai_completion():
#     """
#     Função para obter uma resposta da API da OpenAI.
#     """
#     print('Função para obter uma resposta da API da OpenAI.')
#     response = openai.ChatCompletion.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": "Write a haiku about recursion in programming."}
#         ]
#     )
#     return response.choices[0].message['content']
    
# @app.route('/auth/sign-in', methods=['POST'])
# def sign_in():
#     # URL da API externa
#     url = 'https://maestro.dadosfera.ai/auth/sign-in'
    
#     # Cabeçalhos da requisição
#     headers = {
#         'Accept': 'application/json',
#         'Content-Type': 'application/json',
#         'totp': '45454',
#         'dadosfera-lang': 'pt-BR'
#     }
    
#     # Corpo da requisição POST (o payload que será enviado)
#     # Esse payload pode ser adaptado conforme necessário
#     payload = request.json  # Você pode passar o JSON diretamente no corpo da requisição
    
#     # Fazendo a requisição POST para a API externa
#     try:
#         response = requests.post(url, headers=headers, json=payload)
#         # Retornando a resposta da API externa para o cliente
#         return jsonify(response.json()), response.status_code
#     except requests.exceptions.RequestException as e:
#         # Caso ocorra um erro na requisição
#         return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')
