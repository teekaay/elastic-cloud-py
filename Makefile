# Makefile for elastic-cloud-py
#

DOCDIR = docs

all: clean lint test docs-html

help:
	@echo ""
	@echo "  test		to run unit tests"
	@echo "  docs-html	to build html documentation"

test:
	nosetests

lint:
	flake8 --statistics --exit-zero

docs-html:
	make -C docs html

clean: clean-pyc clean-docs clean-build

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '__pycache' -exec rm -r --force {} + 

clean-docs:
	$(MAKE) -C $(DOCDIR) clean

clean-build:
	rm --force --recursive build
	rm --force --recursive dist
	rm --force --recursive *.egg-info