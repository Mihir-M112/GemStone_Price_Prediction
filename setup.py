from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will check and return list of requirements
    from file_path i.e. requirements.txt file
    '''
    # Initializing blank requirements list
    requirements = []

    # Opening and reading the file
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        # Remove hyphen_e_dot if present in requirements
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name = 'mlproject_regression',
    version= '0.0.1',
    author='Mihir Mishra',
    author_email='mihirmishra892@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)