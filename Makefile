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

docs:
	make -C docs html

test:
	nosetests

lint:
	flake8 --statistics --exit-zero elastic_cloud/**/*.py

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