import os

from setuptools import find_packages, setup


# Thanks Frankkkkk for inspiring.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="barry-energy-api",
    version="1.0.0",
    author="Emil Elkjær Nielsen",
    author_email="emil@evsn.dk",
    description=(
        "Connecting to and getting data from Barry Energy's API (http://barry.energy)"
    ),
    license="LICENS",
    keywords="python barry energy api electricity prices barry.energy",
    url="https://github.com/eelkjaer/BarryAPIClient",
    packages=find_packages(),
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
