from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRI = "A sample test package"
HP = "https://github.com/faveline/exemple"
LIC = "MIT"

setup(
    name="ft_package",
    version=VERSION,
    description=DESCRI,
    url=HP,
    author="faveline",
    author_email="<faveline@42mulhouse.com>",
    license=LIC,
    Requires="",
    Required_by="",
    Metadata_Version="2.1",
    Installer="pip",
    Classifiers="",
    Entry_points="",
    packages=find_packages()
)
