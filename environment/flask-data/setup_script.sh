#!/bin/bash

mamba run -n py38 pip install flask
pip install requests

pip install openai

echo 'export PYTHONPATH="${PYTHONPATH}:/data"' >> /home/jovyan/.orchestrc
echo 'export FLASK_ENV="development"' >> /home/jovyan/.orchestrc
#echo 'export OPENAI_API_KEY=""' >> /home/jovyan/.orchestrc
