from setuptools import setup, find_packages

setup(
    name="accetra",
    version="0.2.2",
    author="AK (GMRZE/Gamorize)",
    author_email="info@gamorize.com",
    description="A flexible XML/JSON language loader",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Gamorize/accetra",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "accetra=accetra.cli:main",
        ],
    },
)
