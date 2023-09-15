# Py Passphrase Generator

Generate random passphrases from a word list.

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


## Why?

For use in generating the few passwords in life you _have_ to remember.
Like your password for logging into your physical laptop or a master password
for a password vault.
Many websites exists that do this already.
But I want a tool I can read the source in 5 mintues and run on my own machine.

![xkcd password strength comit](https://imgs.xkcd.com/comics/password_strength.png)

Websites that do the same thing:
- <https://diceware.dmuth.org/>
- <https://1password.com/password-generator/>


## Word lists

You can choose from any of these word lists when you run the program.

| word list     | size          | bits of entropy / word |
| ------------- | ------------- | ---------------------- |
| bitcoin bip39 | 2048          | 11                     |
| eff large     | 7776          | 12.9248125             |
| eff short 1   | 1296          | 10.33985               |
| eff short 2.0 | 1296          | 10.33985               |

Multiply the `bits of entropy / word` by your passphrase word count to
get the total passphrase entropy.


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
