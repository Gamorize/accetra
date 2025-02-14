import os

class BaseLanguageLoader:
    def __init__(self, primary_lang_file, fallback_lang_file=None):
        self.translations = {}
        self.metadata = {}

        self.primary_lang_file = primary_lang_file
        self.fallback_lang_file = fallback_lang_file

        if os.path.exists(primary_lang_file):
            self.load_language(primary_lang_file)
        else:
            raise FileNotFoundError(f"Language file '{primary_lang_file}' not found!")

        if fallback_lang_file and os.path.exists(fallback_lang_file):
            self.load_language(fallback_lang_file, is_fallback=True)
        elif fallback_lang_file:
            raise FileNotFoundError(f"Fallback file: '{fallback_lang_file}' not found!")

    def load_language(self, lang_file, is_fallback=False):
        raise NotImplementedError

    def get_text(self, entry_id, **variables):
        text = self.translations.get(entry_id, {}).get("text", entry_id)
        return text.format(**variables) if variables else text

    def get_tooltip(self, entry_id, **variables):
        tooltip = self.translations.get(entry_id, {}).get("tooltip", "")
        return tooltip.format(**variables) if variables else tooltip
