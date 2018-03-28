# Makefile for elastic-cloud-py
#

DOCDIR = docs

all: clean lint test dist docs

help:
	@echo ""
	@echo "  dist       to build python distribution"
	@echo "  docs	    to build html documentation"
	@echo "  test		to run unit tests"
	@echo "  lint       to run flake8"
	@echo "  clean 		to remove generated files"

dist:
	python setup.py sdist
	python setup.py bdist_wheel

.PHONY: docs
docs:
	make -C docs html

test:
	nosetests

lint:
	flake8 --statistics --exit-zero elastic_cloud/**/*.py

clean: clean-pyc clean-docs clean-build

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache' -exec rm -rf {} + 

clean-docs:
	$(MAKE) -C $(DOCDIR) clean

clean-build:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info