from setuptools import setup, find_packages


setup(
    name='cv_tool',
    version='0.1',
    description='A tool using opencv for preprocessing images',
    author='Henry Ho',
    author_email='ellipsclamation@gmail.com',
    url='https://github.com/ellipsclamation/opencv_preprocessing_tool',
    packages=find_packages(exclude=('tests', 'docs'))
)
