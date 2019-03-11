#!/usr/bin/env bash
# Instalar local
pip install -e .

# Distribuir
python setup.py bdist_wheel
python -m twine upload dist/