#!/usr/bin/env bash


export NEEDRESTART_MODE=a # This supporesses various prompts during apt package installation

apt install -y python3-venv
python3 -m venv scraper-venv
source scraper-venv/bin/activate
pip install -r requirements.txt
playwright install-deps
playwright install


