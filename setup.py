from typing import List
from setuptools import setup


def read_lines(fname: str) -> List[str]:
    with open(fname) as f:
        return f.readlines()


def read_requirements() -> List[str]:
    read_lines("requirements_source.txt")


setup(
    name="ptry-lib",
    version="0.1.0",
    install_requires=read_requirements(),
    python_requires=">=3.8",
)
