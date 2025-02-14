import os
import pytest
from accetra.xml_loader import XmlLanguageLoader

TEST_XML = "test_lang.xml"
FALLBACK_XML = "fallback_lang.xml"

TEST_CONTENT = """<language>
    <meta>
        <code>en</code>
        <name>English</name>
        <authors><author>John Doe</author></authors>
        <version>1.0</version>
        <description>English Language Pack</description>
    </meta>
    <general>
        <entry id="app.welcome"><text>Welcome, {user}!</text></entry>
        <entry id="app.exit"><text>Goodbye!</text></entry>
    </general>
</language>"""

FALLBACK_CONTENT = """<language>
    <general>
        <entry id="app.missing"><text>This is from fallback.</text></entry>
    </general>
</language>"""

@pytest.fixture
def xml_loader():
    with open(TEST_XML, "w") as f:
        f.write(TEST_CONTENT)
    with open(FALLBACK_XML, "w") as f:
        f.write(FALLBACK_CONTENT)

    yield XmlLanguageLoader(TEST_XML, FALLBACK_XML)

    os.remove(TEST_XML)
    os.remove(FALLBACK_XML)

def test_metadata(xml_loader):
    assert xml_loader.metadata["code"] == "en"
    assert xml_loader.metadata["name"] == "English"
    assert "John Doe" in xml_loader.metadata["authors"]

def test_text_replacement(xml_loader):
    assert xml_loader.get_text("general.app.welcome", user="Alice") == "Welcome, Alice!"

def test_missing_key_fallback(xml_loader):
    assert xml_loader.get_text("general.app.missing") == "This is from fallback."

def test_nonexistent_key(xml_loader):
    assert xml_loader.get_text("general.app.unknown") == "general.app.unknown"
