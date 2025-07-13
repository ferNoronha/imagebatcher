from setuptools import setup, find_packages

setup(
    name="imagebatcher",
    version="0.1.2",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pillow",
        "pytesseract",
        "typer[all]",
        "pyyaml",
        "tqdm"
    ],
    entry_points={
        "console_scripts": [
            "imagebatcher=cli:app"
        ]
    },
    author="Fernando de Almeida Noronha",
    description="Framework leve para processamento e análise de imagens em lote",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",
)