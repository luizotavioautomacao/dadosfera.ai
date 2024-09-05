SHELL = /bin/bash
venv: 
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt
g: venv
	source venv/bin/activate && python3 generate-synthetic-data.py
i:
	chmod +x scripts/install.sh && scripts/install.sh && git submodule update --init --recursive
expec: venv
	source venv/bin/activate && python -m great_expectations.cli init




