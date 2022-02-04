import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="msa-server",
    version="0.0.1",
    author_email="lfmainwaring@gmail.com",
    description="Flask backend for music sample assistant.",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    install_requires=["flask"],
)