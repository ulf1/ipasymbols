[![PyPI version](https://badge.fury.io/py/ipasymbols.svg)](https://badge.fury.io/py/ipasymbols)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/linguistik/ipasymbols.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/linguistik/ipasymbols/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/linguistik/ipasymbols.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/linguistik/ipasymbols/context:python)


# ipasymbols
A simple JSON database to lookup the properties of IPA symbols.

## Warning: Under Development! (25.Nov.2021)
Version `0.0.*` is **not** ready to use. Non-Pulmonic consonants, affricates, co-articulated consonants, and dipthongs are **not** implemented yet. This kind of software is very prone to human errors, and required unit tests are not implemented so far.

## Usage

### Get lists of IPA phons
```py
import ipasymbols

# all vowels
all_vowels = ipasymbols.phonlist(query={'type': 'vowel'})

# front vowels
front_vowels = ipasymbols.phonlist(query={'type': 'vowel', 'backness': 'front'})

# diphthongs (2 char vowels)
diphthongs = ipasymbols.phonlist(query={'type': 'diphthong'})

# different types of consonants
consonants = ipasymbols.phonlist(query={'type': ["pulmonic", "non-pulmonic"]})
# consonants = ['m̥', 'm', 'ɱ', 'n̼', ...]
```


### Get properties of an IPA phon
```py
import ipasymbols
phon = 'ɪ'
props = ipasymbols.props(phon=phon, keys=["height"])
# props = {'height': 'near-close'}
```


### Count certain kinds of IPA symbols
```py
import ipasymbols
ipatext = "de:ɐ̯ kɔʊd ɪst fɔl blø:t abɐ aʊ̯x tɔl"
# vowels
all_vowels = ipasymbols.count(ipatext, query={'type': 'vowel'})
# front vowels
front_vowels = ipasymbols.count(ipatext, query={'type': 'vowel', 'backness': 'front'})
# diphthongs (2 char vowels)
diphthongs = ipasymbols.count(ipatext, query={'type': 'diphthong'})
# different types of consonants
consonants = ipasymbols.count(ipatext, query={'type': ["pulmonic", "non-pulmonic"]})
```


### Count consonant clusters
```py
import ipasymbols
ipatext = "de:ɐ̯ kɔʊd ɪst fɔl blø:t abɐ aʊ̯x tɔl"
types = ["pulmonic", "non-pulmonic", "affricate", "co-articulated"]
clusters = ipasymbols.count_clusters(
    ipatext, query={"type": types}, phonlen=3, min_cluster_len=2)
# clusters = {2: 789, 3: 654, 4: 123, ...}
```


### Read the whole IPA symbols database

```py
import ipasymbols
mydict = ipasymbols.db
```


## Appendix

### Installation
The `ipasymbols` [git repo](http://github.com/linguistik/ipasymbols) is available as [PyPi package](https://pypi.org/project/ipasymbols)

```sh
pip install ipasymbols
pip install git+ssh://git@github.com/linguistik/ipasymbols.git
```

### Install a virtual environment

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
pip install -r requirements-dev.txt --no-cache-dir
pip install -r requirements-demo.txt --no-cache-dir
```

(If your git repo is stored in a folder with whitespaces, then don't use the subfolder `.venv`. Use an absolute path without whitespaces.)

### Python commands

* Jupyter for the examples: `jupyter lab`
* Check syntax: `flake8 --ignore=F401 --exclude=$(grep -v '^#' .gitignore | xargs | sed -e 's/ /,/g'),./ipasymbols/ipasymbols.py`
* Run Unit Tests: `PYTHONPATH=. pytest`

Publish

```sh
pandoc README.md --from markdown --to rst -s -o README.rst
python setup.py sdist 
twine upload -r pypi dist/*
```

### Clean up 

```sh
find . -type f -name "*.pyc" | xargs rm
find . -type d -name "__pycache__" | xargs rm -r
rm -r .pytest_cache
rm -r .venv
```


### Support
Please [open an issue](https://github.com/linguistik/ipasymbols/issues/new) for support.


### Contributing
Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/linguistik/ipasymbols/compare/).
