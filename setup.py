<<<<<<< HEAD
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
=======
from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-r .'

def get_requirements(file_path:str)->List[str]:
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
>>>>>>> 36f7984 (Initial commit: Redesigned UI, fixed scikit-learn mismatch, added README)
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
<<<<<<< HEAD

=======
        
>>>>>>> 36f7984 (Initial commit: Redesigned UI, fixed scikit-learn mismatch, added README)
        return requirements


setup(
<<<<<<< HEAD
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Karan',
    author_email='karanjadhav1771@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()

=======
    name="Diamond_Price_Prediction",
    version="0.0.1",
    author="Karan Jadhav",
    author_email="karanjadhav1771@gmail.com",
    install_required=get_requirements('requirements.txt'),
    packages=find_packages()
    
>>>>>>> 36f7984 (Initial commit: Redesigned UI, fixed scikit-learn mismatch, added README)
)