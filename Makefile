.PHONY: default init install test

default:
	@echo 'available targets: init, install, test'

install:
	python setup.py install

init:
	pip install -r requirements.txt

test:
	python -m pytest
