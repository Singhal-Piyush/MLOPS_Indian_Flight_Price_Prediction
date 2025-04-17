from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e.'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of packages from requirements.txt
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements ]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    
name = "indian_flight_price_prediction",
version = "0.0.1",
author = "Piyush Singhal",
author_email = "singhalpiyush3610@gmail.com",
packages = find_packages(),
install_packages = get_requirements('requirements.txt'),
)

