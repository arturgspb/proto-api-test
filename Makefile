CWD=$(shell pwd)

esp:
	python3 -m metasdk.tools.esp_deploy --service=hello --lang=python --workdir=$(CWD)

dev:
	python3 -m metasdk.tools.esp_dev --service=hello

