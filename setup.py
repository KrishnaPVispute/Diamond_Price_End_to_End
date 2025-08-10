from setuptools import find_packages,setup
from typing import List

# hypen_dot_e = "-e."
def get_req(file_path:str)->list[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        # if hypen_dot_e in requirements:
        #     requirements.remove(hypen_dot_e)

        return requirements


setup(
    name='DiamondPriceML',
    version="0.0.1",
    author='Krishna vispute',
    author_email = "Krishnavispute2004@gmail.com",
    install_requirements = get_req("requirements.txt"),
    packages=find_packages()

)