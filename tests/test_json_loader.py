import os
import json
import pytest
from accetra.json_loader import JsonLanguageLoader

TEST_JSON = "test_lang.json"
FALLBACK_JSON = "fallback_lang.json"

TEST_CONTENT = {
    "meta": {
        "code": "en",
        "name": "English",
        "authors": ["John Doe"],
        "version": "1.0",
        "description": "English Language Pack"
    },
    "general": {
        "app.welcome": { "text": "Welcome, {user}!" },
        "app.exit": { "text": "Goodbye!" }
    }
}

FALLBACK_CONTENT = {
    "general": {
        "app.missing": { "text": "This is from fallback." }
    }
}

@pytest.fixture
def json_loader():
    with open(TEST_JSON, "w") as f:
        json.dump(TEST_CONTENT, f)
    with open(FALLBACK_JSON, "w") as f:
        json.dump(FALLBACK_CONTENT, f)

    yield JsonLanguageLoader(TEST_JSON, FALLBACK_JSON)

    os.remove(TEST_JSON)
    os.remove(FALLBACK_JSON)

def test_metadata(json_loader):
    assert json_loader.metadata["code"] == "en"
    assert json_loader.metadata["name"] == "English"
    assert "John Doe" in json_loader.metadata["authors"]

def test_text_replacement(json_loader):
    assert json_loader.get_text("general.app.welcome", user="Alice") == "Welcome, Alice!"

def test_missing_key_fallback(json_loader):
    assert json_loader.get_text("general.app.missing") == "This is from fallback."

def test_nonexistent_key(json_loader):
    assert json_loader.get_text("general.app.unknown") == "general.app.unknown"
