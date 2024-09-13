SHELL = /bin/bash
i:
	chmod +x scripts/install.sh && scripts/install.sh && git submodule update --init --recursive 
venv: 
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt
g: venv
	source venv/bin/activate && python3 generate-synthetic-data.py
app:
	python3 api.py