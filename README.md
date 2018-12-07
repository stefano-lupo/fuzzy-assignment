# Fuzzy Logic Group Assignment
- Stefano Lupo - 14334933
- Rowan Sutton - 13330793
- Yash Mundra - 16338461

## File Descriptions
- `fuzzy.py` contains the entry point to the program
- `membership_funcs.py` contains the definitions of each of the membership functions used
- `rule_gen.py` contains functions which aided in reading / parsing the rulebase found in `rulebase.txt`
- `rulebase.txt` contains the rules for the fuzzy controller


## Running The Program
- Need to `pip install pipenv` if you don't already have it
- Then just `pipenv install` to grab deps
- Then `pipenv run python <script>` or `pipenv shell`
- For some reason I had to install `tkinter` specifically for 3.6
  - Add PPA: `sudo add-apt-repository ppa:deadsnakes/ppa`
  - Install tkinter for 3.6.1: `sudo apt install python3.6-tk`
  - Then you have to reinstall python 3.6 with pyenv
    - `pyenv uninstall 3.6.7`
    - `pyenv install 3.6.7`
