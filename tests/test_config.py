import pytest

from t212.config import T212_API_KEY, T212_ENVIRONMENT


def test_config():
    assert T212_API_KEY == "abcdefg12345"
    assert T212_ENVIRONMENT == "demo"

# def test_api_key_unset():
#     with pytest.raises(EnvironmentError):

