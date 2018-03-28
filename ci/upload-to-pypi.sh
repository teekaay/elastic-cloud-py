#!/usr/bin/env bash

PYPI_USER="${PYPI_USER}"
PYPI_PASSWORD="${PYPI_PASSWORD}"

if [ -z "$PYPI_USER" ]; then
    echo "ERROR: PYPI_USER must be set"
    exit 1
fi

if [ -z "$PYPI_PASSWORD" ]; then
    echo "ERROR: PYPI_PASSWORD must be set"
    exit 1
fi

make dist
twine upload -u $PYPI_USER -p $PYPI_PASSWORD --skip-existing dist/*
