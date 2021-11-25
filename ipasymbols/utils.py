from .ipasymbols import db
from typing import List
import numpy as np


def phonlist(query: dict) -> List[str]:
    """ Get Phon List """
    query_ = {key: val if isinstance(val, (tuple, list)) else [val]
              for key, val in query.items()}
    return [phon for phon, props in db.items()
            if all([props.get(key) in val for key, val in query_.items()])]


def props(phon, keys) -> dict:
    """ Get certain data fields """
    try:
        return {k: v for k, v in db[phon].items() if k in keys}
    except Exception:
        return {}


def count(ipatext: str, query: dict, phonlen: int = 3) -> int:
    """
    Parameters:
    -----------
    ipatext : str
        A string with IPA characters, e.g. an IPA sentence.
    query : dict
        An JSON object with keys and values to search for,
        e.g. if `type` is `vowel`.
    phonlen : int (default: 3)
        Some phons consist of 2 or 3 unicode characters (e.g.
          affricates, diphthongs). Thus, we need to shingle `ipatext`
          into 2,3,4,.. length shingles.

    Global Parameter:
    -----------------
    db : symbol
        An JSON object with IPA phons as key, and other properties
          als value (also an JSON object).

    Example:
    --------
    ipatext = 'dəʀ koːdeː ɪst fɔl pløːd, ɑːbəʀ aux tɔl.'
    query = {"type": "vowel", "position": "back"}
    pct = ipasymbols.get(ipatext, query)
    """
    phons = phonlist(query)
    hits = 0
    for k in range(1, phonlen + 1):
        hits += sum([ipatext[i:i + k] in phons
                     for i in range(len(ipatext) - k + 1)])
    return hits


def count_clusters(ipatext: str,
                   query: dict = ["pulmonic", "non-pulmonic",
                                  "affricate", "co-articulated"],
                   phonlen: int = 3,
                   min_cluster_len: int = 2) -> dict:
    """Identify and count clusters, e.g. consonant clusters

    Parameters:
    -----------
    ipatext : str
        A string with IPA characters, e.g. an IPA sentence.
    query : dict
        An JSON object with keys and values to search for,
        e.g. if `type` is `vowel`.
    phonlen : int (default: 3)
        Some phons consist of 2 or 3 unicode characters (e.g.
          affricates, diphthongs). Thus, we need to shingle `ipatext`
          into 2,3,4,.. length shingles.

    Returns:
    --------
    results : dict
        An JSON object with the keys as consonant subsequence length
          (or consonant cluster size) and the values how often these
          are found in the IPA text string.
    Example:
    --------
    ipatext = "diː bœʀsən-yːʊpiːs uːmɭ̊˔ ɡɔʀdoːn ɡɛkkoː tʀɑːɡ"
    numclusters = count_clusters(ipatext, phonlen=3, min_cluster_len=2)
    numclusters
    """
    # filter phons from ipasymbols.db list
    phons = phonlist(query)

    # mark string position if an IPA consonant starts there
    matches = np.zeros((len(ipatext), ), dtype=bool)
    for k in range(1, phonlen + 1):
        tmp = [ipatext[i:i + k] in phons for i in range(len(ipatext) - k + 1)]
        tmp += [False for _ in range(k - 1)]  # pad missing elements at the end
        matches = np.logical_or(matches, tmp)

    # identify consecutive subsequences of 1s, and count them by their length
    results = {}
    lengthcounter = 0
    for iscons in matches:
        if iscons:
            # count the subsequence length
            lengthcounter += 1
        else:
            # save if the subsequence is long enough
            if lengthcounter >= min_cluster_len:
                results[lengthcounter] = results.get(lengthcounter, 0) + 1
            # start a new subsequence if it's NOT a consonant
            lengthcounter = 0

    if lengthcounter >= min_cluster_len:
        # store the last subsequence
        results[lengthcounter] = results.get(lengthcounter, 0) + 1

    # done
    return results
