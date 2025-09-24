from setuptools import setup, find_packages

HYPEN_E_DOT='-e .'
def get_requirements(file_name):
    requirements=[]
    with open(file_name,'r') as file_obj:
        requirements = file_obj.readlines()
        requirements=[i.replace("\n","")for i in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements


setup(
    name="MLproject",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)