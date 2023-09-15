# Py Passphrase Generator

Generate secure, random passphrase from a word list.

    ```
    python app.py --help
    ```

    ```
    usage: app.py [-h] [--wordlist {bip39,eff-large,eff-short,eff-short-2}]
              count separator

    positional arguments:
      count                 number of random words to generate
      separator             string to insert between words. Use ' ' for empty
                            space

    options:
      -h, --help            show this help message and exit
      --wordlist {bip39,eff-large,eff-short,eff-short-2}, -l {bip39,eff-large,eff-short,eff-short-2}
                            source word list from bitcoin or eff.org
    ```


## Running with Docker

- build the docker image!
   ```commandline
   sh docker-build.sh
   ```
- run the app from docker!
   ```commandline
   docker run pass-gen 8 '-'
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
