import pytest 

def extract_uppercase(value):
    if value is None:
        raise TypeError("extract_uppercase expects a string, not a None")
    words = value.split()
    uppercase_words = []
    for word in words:
        cleaned_words = clean_word(word)
        if cleaned_words != "" and cleaned_words.isupper():
            uppercase_words.append(cleaned_words)
    return uppercase_words

def clean_word(value):
    cleaning = ""
    for symbol in value:
        if symbol.isalpha():
            cleaning += symbol
    return cleaning

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""

def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

"""
Given two uppercase words
It returns a list with both words
"""
#extract_uppercase("HELLO WORLD") => ["HELLO", "WORLD"]

def test_extract_two_uppercase():
    result = extract_uppercase("HELLO WORLD")
    assert result == ["HELLO", "WORLD"]

"""
Given two lowercase words
It returns an empty list
"""
#extract_uppercase("hello world") => []

def test_extract_two_lowercase():
    result = extract_uppercase("hello world")
    assert result == []


"""
Given a lower and a mixed case word
It returns an empty list
"""
#extract_uppercase("hello WoRLD") => []

def test_mixed_cases():
    result = extract_uppercase("hello WoRLD")
    assert result == []

"""
Given a lowercase word and an uppercase word with an exclamation mark
It returns a list with the uppercase word, no exclamation mark
"""
#extract_uppercase("hello WORLD!") => ["WORLD"]

def test_isalpha():
    result = extract_uppercase("hello WORLD!")
    assert result == ["WORLD"]
"""
Given an empty string
It returns an empty list
"""
#extract_uppercase("") => []

def test_isempty():
    result = extract_uppercase("")
    assert result == []
"""
Given a None value
It throws an error
"""

#extract_uppercase(None) throws an error
def test_error():
    with pytest.raises(TypeError):
        extract_uppercase(None) 
