import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Inventory Manager",
    version="ALPHA 0.1",
    author="Ben Saltz",
    author_email="ben@squizit.net",
    description="A solution for rental shops to keep track of checked out equipment through barcodes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/b2550/Inventory-Manager",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Filter Framework :: Flask",
        "Natural Language :: English",

    ),
)
