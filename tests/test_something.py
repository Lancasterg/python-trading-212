import pytest
from t212.config import T212_API_KEY, T212_ENVIRONMENT


def test_something():
    assert T212_API_KEY == "abcdefg12345"
    assert T212_ENVIRONMENT == "demo"
    # Placeholder test for now
    assert True is True
