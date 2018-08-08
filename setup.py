from setuptools import setup

setup(
    name='optx-cv',
    version='0.1',
    description='opencv preprocessing tool',
    author='Henry Ho',
    author_email='ellipsclamation@gmail.com',
    url='https://github.com/ellipsclamation/opencv_preprocessing_tool',
    packages=['controller', 'view', 'modules', 'images'],
    install_requires=['opencv-python', 'PyQt5', 'numpy']
)
