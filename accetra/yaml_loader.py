import yaml
from .base_loader import BaseLanguageLoader

class YamlLanguageLoader(BaseLanguageLoader):
    def load_language(self, lang_file, is_fallback=False):
        with open(lang_file, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        if not is_fallback:
            self._load_metadata(data.get("meta", {}))

        for section in ["windows", "general", "errors"]:
            if section in data:
                self._load_entries(data[section], section, is_fallback)

    def _load_metadata(self, meta):
        self.metadata = {
            "code": meta.get("code", "unknown"),
            "name": meta.get("name", "Unknown"),
            "authors": meta.get("authors", []),
            "version": meta.get("version", "1.0"),
            "description": meta.get("description", ""),
        }

    def _load_entries(self, section, prefix="", is_fallback=False):
        for key, value in section.items():
            entry_id = f"{prefix}.{key}"
            self._add_entry(value, entry_id, is_fallback)

    def _add_entry(self, entry, entry_id, is_fallback):
        if entry_id not in self.translations or is_fallback:
            self.translations.setdefault(entry_id, {
                "text": entry.get("text", entry_id),
                "tooltip": entry.get("tooltip", "")
            })
