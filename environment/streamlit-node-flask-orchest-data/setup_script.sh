#!/bin/bash

# Conceder permissão executável ao próprio script
#chmod +x $0

# Instalar Mamba se não estiver instalado
if ! command -v mamba &> /dev/null
then
    echo "Mamba não encontrado. Instalando Mamba..."
    conda install mamba -n base -c conda-forge
fi

# Instalar Python 3.8 e dependências
mamba create -y -n py38 python=3.8 future
mamba install -y -n py38 ipykernel jupyter_client ipython_genutils pycryptodomex future "pyarrow<8.0.0"
mamba run -n py38 pip install orchest flask matplotlib
pip install requests openai

# Configuração do ambiente Jupyter e Orchest
echo "export JUPYTER_PATH=/opt/conda/envs/py38/share/jupyter" >> /home/jovyan/.orchestrc
echo "export PATH='/opt/conda/envs/py38/bin/:$PATH'" >> /home/jovyan/.orchestrc
echo "export CONDA_ENV=py38" >> /home/jovyan/.orchestrc

echo 'export PYTHONPATH="${PYTHONPATH}:/data"' >> /home/jovyan/.orchestrc
echo 'export FLASK_ENV="development"' >> /home/jovyan/.orchestrc
#echo 'export OPENAI_API_KEY=""' >> /home/jovyan/.orchestrc

# Instalar pacotes adicionais no ambiente conda
mamba run -n py38 pip install pandas snowflake-snowpark-python streamlit plotly spacy==3.5.0 https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.5.0/en_core_web_sm-3.5.0-py3-none-any.whl

# Atualizar o sistema e instalar pacotes
sudo apt-get update   
pip3 install --upgrade pyOpenSSL boto3 awscli chardet requests anybase32 pandas snowflake-snowpark-python
 
# Autenticação e configuração do CodeArtifact da AWS
if ! aws codeartifact login --tool pip --domain dadosfera --domain-owner 611330257153 --region us-east-1 --repository dadosfera-pip
then
    echo "Falha na autenticação da AWS CodeArtifact. Verifique suas credenciais."
    exit 1
fi

# Instalar pacotes específicos da AWS CodeArtifact
pip3 install dadosfera==1.5.0 dadosfera_logs==1.0.3

# Define o diretório do ambiente virtual
VENV_DIR="$HOME/venv"

# Atualiza o sistema
sudo apt update

# Instala o Node.js e npm se não estiverem instalados
if ! command -v node &> /dev/null || ! command -v npm &> /dev/null
then
    echo "Node.js e/ou npm não encontrados. Instalando Node.js e npm..."
    sudo apt install -y curl
    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    sudo apt install -y nodejs
    if command -v node &> /dev/null && command -v npm &> /dev/null
    then
        echo "Node.js e npm instalados com sucesso."
    else
        echo "Falha ao instalar Node.js e npm."
        exit 1
    fi
else
    echo "Node.js e npm já estão instalados."
fi
