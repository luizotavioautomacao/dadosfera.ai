#!/bin/bash

# Check if Python 3 is installed
if command -v python3 &>/dev/null; then
    echo "Python 3 já está instalado."
    python3 --version
else
    echo "Python 3 não está instalado. Instalando Python 3..."
    sudo apt-get update
    sudo apt-get install -y python3
fi

# Check if pip3 is installed
if command -v pip3 &>/dev/null; then
    echo "pip3 já está instalado."
else
    echo "pip3 não está instalado. Instalando pip3..."
    sudo apt-get install -y python3-pip
fi

# Create and activate a virtual environment
echo "Criando e ativando um ambiente virtual..."
python3 -m venv venv
source venv/bin/activate

# Display Python 3 and pip3 versions
python3 --version
pip3 --version

# Install dependencies with pip3
echo "Instalando bibliotecas pandas, faker, orchest-sdk"
pip3 install pandas faker flask #orchest

echo "Instalação concluída!"
echo "Siga para o próximo passo."


