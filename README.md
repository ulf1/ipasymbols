[![PyPI version](https://badge.fury.io/py/ipasymbols.svg)](https://badge.fury.io/py/ipasymbols)
[![PyPi downloads](https://img.shields.io/pypi/dm/ipasymbols)](https://img.shields.io/pypi/dm/ipasymbols)
[![DOI](https://zenodo.org/badge/431771809.svg)](https://zenodo.org/badge/latestdoi/431771809)


# ipasymbols: Properties of IPA symbols for data analysis
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
The `ipasymbols` [git repo](http://github.com/ulf1/ipasymbols) is available as [PyPi package](https://pypi.org/project/ipasymbols)

```sh
pip install ipasymbols
pip install git+ssh://git@github.com/ulf1/ipasymbols.git
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
Please [open an issue](https://github.com/ulf1/ipasymbols/issues/new) for support.


### Contributing
Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/ulf1/ipasymbols/compare/).

### Acknowledgements
The "Evidence" project was funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) - [433249742](https://gepris.dfg.de/gepris/projekt/433249742) (GU 798/27-1; GE 1119/11-1).

### Maintenance
- till 31.Aug.2023 (v0.0.1) the code repository was maintained within the DFG project [433249742](https://gepris.dfg.de/gepris/projekt/433249742)
- since 01.Sep.2023 (v0.1.0) the code repository is maintained by Ulf Hamster.

### Citation
You can cite the following paper if you want to use this repository in your research work.

```
@inproceedings{hamster-2022-everybody,
    title = "Everybody likes short sentences - A Data Analysis for the Text Complexity {DE} Challenge 2022",
    author = "Hamster, Ulf A.",
    booktitle = "Proceedings of the GermEval 2022 Workshop on Text Complexity Assessment of German Text",
    month = sep,
    year = "2022",
    address = "Potsdam, Germany",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.germeval-1.2",
    pages = "10--14",
}
```