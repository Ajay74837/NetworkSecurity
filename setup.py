from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    Returns a list of requirements, excluding editable installs.
    """
    requirement_lst: List[str] = []

    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and not requirement.startswith('-e'):
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found')

    return requirement_lst

setup(
    name="networkSecurity",
    version="0.0.1",
    author="Ajay",
    author_email="ajaydanki74@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
