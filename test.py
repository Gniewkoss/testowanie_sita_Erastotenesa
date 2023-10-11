import pytest
from main import sito


from main import sito

def test_sito_with_10():
    result = sito(10)
    assert result == [2, 3, 5, 7]

def test_sito_with_20():
    result = sito(20)
    assert result ==[2, 3, 5, 7, 11, 13, 17, 19]
