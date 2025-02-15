import argparse
import os
from accetra.json_loader import JsonLanguageLoader
from accetra.xml_loader import XmlLanguageLoader
from rich.console import Console
from rich.traceback import install

install()
console: Console = Console()


def validate_file(file_path)-> None:
    try:
        if file_path.endswith(".json"):
            loader = JsonLanguageLoader(file_path)
        elif file_path.endswith(".xml"):
            loader = XmlLanguageLoader(file_path)
        else:
            console.print(f"[bold red]Unsupported file type:[/bold red] {file_path}")
            return
        console.print(f"[bold green]Validated successfully:[/bold green] {file_path}")
    except Exception as e:
        console.print(f"[bold red]Validation failed for {file_path}:[/bold red] {e}")


def create_template(output_dir: str, file_type: str):
    template = {
        "meta": {
            "code": "en",
            "name": "English",
            "authors": ["Author Name"],
            "version": "1.0",
            "description": "Language file template"
        },
        "windows": {},
        "general": {},
        "errors": {}
    }
    if file_type == "json":
        import json
        with open(os.path.join(output_dir, "language_template.json"), "w") as f:
            json.dump(template, f, indent=4)
    elif file_type == "xml":
        template_xml = """<?xml version="1.0"?>
<language>
    <meta>
        <code>en</code>
        <name>English</name>
        <authors><author>Author Name</author></authors>
        <version>1.0</version>
        <description>Language file template</description>
    </meta>
    <windows></windows>
    <general></general>
    <errors></errors>
</language>
"""
        with open(os.path.join(output_dir, "language_template.xml"), "w") as f:
            f.write(template_xml)
    else:
        console.print(f"Filetype: {file_type} is invalid. Choose either 'xml' or 'json'")
    console.print(f"[bold cyan]Template created in {output_dir}[/bold cyan]")


def main():
    parser = argparse.ArgumentParser(description="Language Loader CLI")
    subparsers = parser.add_subparsers(dest="command")

    validate_parser = subparsers.add_parser("validate", help="Validate a language file")
    validate_parser.add_argument("file", type=str, help="Path to language file")

    template_parser = subparsers.add_parser("template", help="Create a language file template")
    template_parser.add_argument("output_dir", type=str, help="Output directory for the template")
    template_parser.add_argument("type", choices=["json", "xml"], help="File type for the template")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        console.print("\n[bold yellow]Run with a subcommand (validate or template) for usage details.[/bold yellow]")
    elif args.command == "validate":
        validate_file(args.file)
    elif args.command == "template":
        create_template(args.output_dir, args.type)


if __name__ == "__main__":
    main()
