set shell := ["fish", "-c"]

venv:
    uv venv
    source .venv/bin/activate.fish

run:
    python3 main.py -s=2 -n=100

tour:
    python3 main.py -n=10000 -s=0 -c
