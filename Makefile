.ONESHELL:
.DELETE_ON_ERROR:

SHELL := /bin/bash

.PHONY: activate requirements format


activate:
	@echo "Connecting pyenv & poetry..."
	poetry config virtualenvs.in-project true && \
	poetry env use $$(pyenv which python) && \
	poetry config virtualenvs.prefer-active-python true;

	source ./.venv/bin/activate;
	
	@echo "Done!"

requirements:
	poetry export -f requirements.txt --without-hashes | cut -f1 -d\; > requirements.txt

format:
	poetry run isort . && \
	poetry run black ./ && \
	poetry run flake8 ./ 
	