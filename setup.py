from setuptools import setup, find_packages


setup(
    name='optic.py',
    version='0.1',
    description='opencv preprocessing tool',
    author='Henry Ho',
    author_email='ellipsclamation@gmail.com',
    url='https://github.com/ellipsclamation/opencv_preprocessing_tool',
    packages=find_packages(exclude=('tests', 'docs'))
)
