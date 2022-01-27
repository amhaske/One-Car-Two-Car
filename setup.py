from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='brain_corp_assessment',
   version='1.0',
   description='Brain Corp Assessment',
   license="MIT",
   python_requires=">3.9",
   long_description=long_description,
   author='Ashish Sanjay Mhaske',
   author_email='amhaske32@gmail.com',
   install_requires=['pytest']
)
