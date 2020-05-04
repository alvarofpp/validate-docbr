import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="validate_docbr",
    version="1.7.0",
    author="Álvaro Ferreira Pires de Paiva",
    author_email="alvarofepipa@gmail.com",
    description="Validate brazilian documents.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alvarofpp/validate-docbr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
