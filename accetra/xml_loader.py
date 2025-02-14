import xml.etree.ElementTree as ET
from .base_loader import BaseLanguageLoader

class XmlLanguageLoader(BaseLanguageLoader):
    def load_language(self, lang_file, is_fallback=False):
        tree = ET.parse(lang_file)
        root = tree.getroot()

        if not is_fallback:
            self._load_metadata(root.find("meta"))

        for section in ["windows", "general", "errors"]:
            sec = root.find(section)
            if sec is not None:
                self._load_entries(sec, section, is_fallback)

    def _load_metadata(self, meta):
        self.metadata = {
            "code": meta.findtext("code", "unknown"),
            "name": meta.findtext("name", "Unknown"),
            "authors": [author.text for author in meta.find("authors", [])],
            "version": meta.findtext("version", "1.0"),
            "description": meta.findtext("description", ""),
        }

    def _load_entries(self, section, prefix="", is_fallback=False):
        for elem in section:
            entry_id = f"{prefix}.{elem.get('id')}"
            self._add_entry(elem, entry_id, is_fallback)

    def _add_entry(self, entry, entry_id, is_fallback):
        if entry_id not in self.translations or is_fallback:
            self.translations.setdefault(entry_id, {
                "text": entry.findtext("text", entry_id),
                "tooltip": entry.findtext("tooltip", "")
            })
