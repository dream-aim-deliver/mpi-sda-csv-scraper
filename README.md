# MPI CSV Scraper





## Development

### Setup

1. Install the required packages, preferably in a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


2. Setup kernel-planckster locally:
    1. Clone the [kernel-planckster](https://github.com/dream-aim-deliver/kernel-planckster) repo elsewhere
    2. Install the required packages, preferable in its own virtual environment, following the instructions in the README
    3. Run it in dev mode with a object store following the README (e.g., `poetry run dev:storage`), where you'll find the host, port, auth key and schema
    4. Kernel Planckster's host, port, auth key and schema will be used as command line arguments when running the main scraper script, so take note of them


