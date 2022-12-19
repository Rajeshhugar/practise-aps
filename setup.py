from setuptools import  find_packages,setup


from typing import List

REQUIREMENTS_FILE_NAME = 'requirements.txt'
HYPEN_E_DOT = '-e .'

def get_requirements()->List[str]:...
   with open(REQUIREMENTS_FILE_NAME) as requireemnt_file:
       requirement_list =requireemnt_file.readlines()
       requirement_list =[requirement_name.replace ("\n","") for requirement_name in 
        requirement_list]
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPEN_E_DOT)
    return requirement_list


# If we have __init__ then this find packages will consider it as a packages

setup(
    name="sensor",
    version="0.0.1",
    author="Rajesh_hugar",
    author_email ="hugarrajesh@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)

# If we want to install our source code as Library so we use -e .
# . means it is pointing to the current directory 
# e means editable install 