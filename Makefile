CALL_CMD=PYTHONPATH=. python
ACTIVATE_VENV=source .venv/bin/activate
SERVICE_NAME=pallet_classifier

SHELL:=/bin/bash

.PHONY: deploy destroy
.ONESHELL:

setup:
	python3 -m venv .venv
	$(ACTIVATE_VENV) && \

	pip install -r requirements.txt

check_linter:
	$(ACTIVATE_VENV)
	flake8 src

run_server:
	$(ACTIVATE_VENV)
	$(CALL_CMD) app.py

logs:
	docker logs -f $(SERVICE_NAME)

run_docker:
	docker build -t $(SERVICE_NAME)_image .
	docker run -p $(API_PORT):$(API_PORT) -d --name $(SERVICE_NAME) $(SERVICE_NAME)_image

stop_docker:
	docker stop $(SERVICE_NAME)
	docker container rm $(SERVICE_NAME)
