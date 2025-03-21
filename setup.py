from setuptools import setup, find_packages
# from pathlib import Path
from typing import List

HYPEN_E_DOT = '-e .'
# This is a workaround to get the README file content
# Function to read the requirements from a file
def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of requirements.
    """
    requirements = []
    # Check if the file exists
    with open(file_path, 'r') as file_obj:
        # Read the lines from the file
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
    
    
    # Remove any '-e .' from the requirements list
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    # Remove any leading/trailing whitespace characters
    #requirements = [req.strip() for req in requirements if req.strip()]
    
    return requirements


# This is a workaround to get the README file content
setup(
    name='mlproject',
    version='0.0.1',
    author='Nitish', # Replace with your name    
    author_email='nitishkumarsharma58804@gmail.com',  # Replace with your email
    # description='A small example package',
    # long_description=open('README.md').read(),
    # long_description_content_type='text/markdown',
    # install_requires=[
        # 'pandas','numpy','seaborn'], # Add other dependencies here
    install_requires=get_requirements('requirements.txt'), # Function to read requirements from a file
    packages=find_packages()
)