.ONESHELL:
.DELETE_ON_ERROR:

SHELL := /bin/bash

.PHONY: activate install_pyenv install_poetry requirements format

activate:
	@echo "Connecting pyenv & poetry..."
	poetry config virtualenvs.in-project true && \
	poetry env use $$(pyenv which python) && \
	poetry config virtualenvs.prefer-active-python true;
	source ./.venv/bin/activate;
	@echo "Done!"

install_pyenv:
	if command -v pyenv 1>/dev/null 2>&1; then \
		echo "pyenv already installed"; \
	else \
		sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
		libsqlite3-dev wget curl libncurses5-dev libncursesw5-dev libreadline-dev\
		xz-utils libffi-dev liblzma-dev git; \
		if [ ! -d "$$HOME/.pyenv" ] ; then \
			git clone https://github.com/pyenv/pyenv.git ~/.pyenv; \
		fi; \
		echo 'export PYENV_ROOT="$$HOME/.pyenv"' >> ~/.bashrc; \
		echo 'export PYENV_ROOT="$$HOME/.pyenv"' >> ~/.bash_profile; \
		echo 'export PATH="$$PYENV_ROOT/bin:$$PATH"' >> ~/.bashrc; \
		echo 'export PATH="$$PYENV_ROOT/bin:$$PATH"' >> ~/.bash_profile; \
		echo 'if command -v pyenv 1>/dev/null 2>&1; then eval "$$(pyenv init -)"; fi' >> ~/.bashrc; \
		echo 'if command -v pyenv 1>/dev/null 2>&1; then eval "$$(pyenv init -)"; fi' >> ~/.bash_profile; \
	fi

install_poetry:
	if command -v poetry 1>/dev/null 2>&1; then \
		echo "poetry already installed"; \
	else \
		curl -sSL https://install.python-poetry.org | python3 - ; \
		echo 'export PATH="$$HOME/.local/bin:$$PATH"' >> ~/.bashrc; \
		echo 'export PATH="$$HOME/.local/bin:$$PATH"' >> ~/.bash_profile; \
	fi

requirements:
	poetry export -f requirements.txt --without-hashes | cut -f1 -d\; > requirements.txt

format:
	poetry run isort . && \
	poetry run black ./ && \
	poetry run flake8 ./
