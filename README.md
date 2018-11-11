# Fuzzy Logic Group Assignment
- ~Using Python 3.7~ Scikit fuzzy was giving me issues on 3.7, so using 3.6.7


## Running Stuff
- Need to `pip install pipenv` if you don't already have it
- Then just `pipenv install` to grab deps
- Then `pipenv run python <script>` or `pipenv shell`
- For some reason I had to install `tkinter` specifically for 3.6
  - Add PPA: `sudo add-apt-repository ppa:deadsnakes/ppa`
  - Install tkinter for 3.6.1: `sudo apt install python3.6-tk`
  - Then you have to reinstall python 3.6 with pyenv
    - `pyenv uninstall 3.6.7`
    - `pyenv install 3.6.7`