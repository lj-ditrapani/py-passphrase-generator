# Py Passphrase Generator

Generate secure, random passphrase from a word list.
Read the help.

    python app.py --help


## Running with Docker

- build the docker image!
   ```commandline
   sh docker-build.sh
   ```
- run the app from docker!
   ```commandline
   sh docker-run.sh
   ```


# Develop

## Dev setup

- Make sure pyenv is initialized.  You may already have this is your bashrc.
    ```commandline
    eval "$(pyenv init -)"
    ```
- install the python version defined in `.python-version` (one time only)
    ```commandline
    pyenv install
    ```
- create a new python virtual environment (one time only)
    ```commandline
    python -m venv ppg
    ```
- activate the virtual environment
    ```commandline
    source ppg/bin/activate
    ```
- install pip requirements
    ```commandline
    pip install -r requirements.txt
    ```


### Dev

- run the tool
    ```commandline
    python app.py
    ```
- run the tests
    ```commandline
    python -m unittest
    ```
- run unit tests with code coverage & report results
    ```commandline
    coverage run -m unittest
    coverage report
    ```
- typecheck with MyPy
    ```commandline
    mypy --strict app.py
    ```
- format src with black
    ```commandline
    black app.py
    ```
