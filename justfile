set shell := ["fish", "-c"]

venv:
    uv venv
    source .venv/bin/activate.fish

tour:
    python3 tournament.py

run:
    python3 main.py
