import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="validate_docbr",
    version="1.11.1",
    author="Álvaro Ferreira Pires de Paiva",
    author_email="alvarofepipa@gmail.com",
    description="Validate brazilian documents.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alvarofpp/validate-docbr",
    packages=setuptools.find_packages(exclude=['tests']),
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
)
