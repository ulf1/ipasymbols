import ipasymbols
import html


def test1():
    for key, val in ipasymbols.db.items():
        # if key not in ['\u027F', '\u0285']:
        assert key == val['glyph']


def test2():
    for key, val in ipasymbols.db.items():
        if val.get("html"):
            assert key == html.unescape(val.get("html"))


def test_vowels1():
    for key, val in ipasymbols.db.items():
        if val.get('type') == "vowel":
            desc = val.get('ipa-description')
            if desc:
                desc = desc.lower()
                assert val.get("type") in desc
                assert val.get("backness") in desc
                assert val.get("height") in desc
                if val.get("roundedness"):
                    assert val.get("roundedness") in desc


def test_height1():
    vowels = ['\u0069', '\u0079', '\u0268', '\u0289', '\u026F', '\u0075']
    for key, val in ipasymbols.db.items():
        if val.get('type') == "vowel" and val.get('height') == "close":
            if key in vowels:
                vowels.remove(key)
            else:
                raise Exception(f"Phon '{key}' is misclassified.")
    assert len(vowels) == 0


def test_height2():
    vowels = ['\u026A', '\u028F', '\u026A\u0308', '\u028A\u0308', '\u028A']
    for key, val in ipasymbols.db.items():
        if val.get('type') == "vowel" and val.get('height') == "near-close":
            if key in vowels:
                vowels.remove(key)
            else:
                raise Exception(f"Phon '{key}' is misclassified.")
    assert len(vowels) == 0


def test_height3():
    vowels = ['\u0065', '\u00F8', '\u0258', '\u0275', '\u0264', '\u006F']
    for key, val in ipasymbols.db.items():
        if val.get('type') == "vowel" and val.get('height') == "close-mid":
            if key in vowels:
                vowels.remove(key)
            else:
                raise Exception(f"Phon '{key}' is misclassified.")
    assert len(vowels) == 0


def test_height4():
    vowels = ['\u0065\u031E', '\u00F8\u031E', '\u0259', '\u0264\u031E',
              '\u006F\u031E']
    for key, val in ipasymbols.db.items():
        if val.get('type') == "vowel" and val.get('height') == "mid":
            if key in vowels:
                vowels.remove(key)
            else:
                raise Exception(f"Phon '{key}' is misclassified.")
    assert len(vowels) == 0


def test_height5():
    vowels = ['\u025B', '\u0153', '\u025C', '\u025E', '\u028C', '\u0254']
    for key, val in ipasymbols.db.items():
        if val.get('type') == "vowel" and val.get('height') == "open-mid":
            if key in vowels:
                vowels.remove(key)
            else:
                raise Exception(f"Phon '{key}' is misclassified.")
    assert len(vowels) == 0


def test_height6():
    vowels = ['\u00E6', '\u0250']
    for key, val in ipasymbols.db.items():
        if val.get('type') == "vowel" and val.get('height') == "near-open":
            if key in vowels:
                vowels.remove(key)
            else:
                raise Exception(f"Phon '{key}' is misclassified.")
    assert len(vowels) == 0


def test_height7():
    vowels = ['\u0061', '\u0276', '\u0061\u0308', '\u0251', '\u0252']
    for key, val in ipasymbols.db.items():
        if val.get('type') == "vowel" and val.get('height') == "open":
            if key in vowels:
                vowels.remove(key)
            else:
                raise Exception(f"Phon '{key}' is misclassified.")
    assert len(vowels) == 0


# backness: front, central, back
