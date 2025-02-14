# Accetra - Multilingual Language Loader

Accetra is a lightweight and efficient **language loader** that supports loading translations from **XML** and **JSON** files. It allows for **automatic fallback**, **variable replacements**, and has an **organized structure** for easy extensibility. This library is ideal for applications that need to support multiple languages.

---

## 🚀 Features

- **Multi-format Support**: Load translations from XML and JSON files.
- **Fallback Mechanism**: Automatically fall back to another language if a key is missing.
- **Variable Replacement**: Replace variables in strings (e.g., `{username}` becomes `Alice`).
- **Metadata Extraction**: Retrieve metadata like language code, authors, and version.
- **Extensibility**: Easily add support for more formats or customization.
- **Clear Structure**: Organize translations into sections (e.g., windows, errors, etc.).

---

## 🧑‍💻 Installation

### 1. **Install via PyPI** (Recommended)
You can install **Accetra** directly from PyPI:

```bash
pip install accetra
```

### 2. **Install from Source**

If you want to contribute or modify the library, you can install it from the source in editable mode:

```bash
git clone https://github.com/yourusername/accetra.git
cd accetra
pip install -e .
```

---

## 🎯 Usage

Accetra supports loading languages from both **XML** and **JSON** formats. Below are examples of how to use both formats.

### **XML Example**

```xml
<language>
    <meta>
        <code>en</code>
        <name>English</name>
        <authors><author>John Doe</author></authors>
        <version>1.0</version>
        <description>English Language Pack</description>
    </meta>
    <general>
        <entry id="app.welcome">
            <text>Welcome, {username}!</text>
        </entry>
    </general>
</language>
```

#### Load and use an XML language file:

```python
from accetra.xml_loader import XmlLanguageLoader

# Initialize loader with primary and fallback languages
lang = XmlLanguageLoader("languages/en.xml", "languages/de.xml")

# Get translated text with variable replacement
text = lang.get_text("general.app.welcome", username="Alice")
print(text)  # Output: "Welcome, Alice!"
```

### **JSON Example**

```json
{
  "meta": {
    "code": "en",
    "name": "English",
    "authors": ["John Doe"],
    "version": "1.0",
    "description": "English Language Pack"
  },
  "general": {
    "app.welcome": {
      "text": "Welcome, {username}!"
    }
  }
}
```

#### Load and use a JSON language file:

```python
from accetra.json_loader import JsonLanguageLoader

# Initialize loader with primary and fallback languages
lang = JsonLanguageLoader("languages/en.json", "languages/de.json")

# Get translated text with variable replacement
text = lang.get_text("general.app.welcome", username="Alice")
print(text)  # Output: "Welcome, Alice!"
```

---

## 🧑‍💼 Functions and Methods

### **Base Class: `BaseLanguageLoader`**  
The base class provides the core functionality for loading translations and handling variable replacement.

- **`__init__(self, primary_lang_file, fallback_lang_file=None)`**:  
  Initialize the loader with primary and optional fallback language files.

- **`get_text(self, entry_id, **variables)`**:  
  Retrieve the translated text for a specific entry, applying any provided variable replacements.

- **`get_tooltip(self, entry_id, **variables)`**:  
  Retrieve the tooltip text for a specific entry, applying any provided variable replacements.

### **XML Loader: `XmlLanguageLoader`**  
Inherits from `BaseLanguageLoader`, designed for loading XML-based translation files.

- **`load_language(self, lang_file, is_fallback=False)`**:  
  Load the specified XML language file.

- **`_load_metadata(self, meta)`**:  
  Extract metadata from the XML file (e.g., code, name, authors).

- **`_load_entries(self, section, prefix="", is_fallback=False)`**:  
  Load translation entries from a specific section in the XML.

### **JSON Loader: `JsonLanguageLoader`**  
Inherits from `BaseLanguageLoader`, designed for loading JSON-based translation files.

- **`load_language(self, lang_file, is_fallback=False)`**:  
  Load the specified JSON language file.

- **`_load_metadata(self, meta)`**:  
  Extract metadata from the JSON file (e.g., code, name, authors).

- **`_load_entries(self, section, prefix="", is_fallback=False)`**:  
  Load translation entries from a specific section in the JSON.

---

## 🤝 Contributing

We welcome contributions to Accetra! If you would like to contribute, please follow these steps:

1. **Fork the repository**:  
   Click the "Fork" button at the top of the page to create your own copy of the repository.

2. **Create a new branch**:  
   In your forked repository, create a new branch for your changes:
   ```bash
   git checkout -b feature/my-new-feature
   ```

3. **Make your changes**:  
   Make your changes to the code. Add tests for new features or bug fixes.

4. **Commit your changes**:  
   Once you're happy with your changes, commit them:
   ```bash
   git commit -am 'Add new feature'
   ```

5. **Push your changes**:  
   Push your changes to your forked repository:
   ```bash
   git push origin feature/my-new-feature
   ```

6. **Create a pull request**:  
   Go to the original repository and create a pull request. We'll review it and merge it into the main branch if everything looks good.

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 📢 Contact

If you have any questions or suggestions, feel free to open an issue or contact the maintainers:

- **AK (TRCLoop)**: [GitHub Profile](https://github.com/TRC-Loop)

---

Happy coding! 😊