#!/usr/bin/env bash


apt install -y python3-venv
python3 -m venv scraper-venv
source scraper-venv/bin/activate
pip install -r requirements.txt
playwright install-deps
playwright install


