from setuptools import setup

setup(
   name='binarytool',
   version='1.0',
   description='A useful module',
   author='Jiaxin He',
   author_email='jih063@ucsd.edu',
   packages=['binarytool'],  
   install_requires=['jupyter','pandas==0.23.3','numpy>=1.14.5',]
)