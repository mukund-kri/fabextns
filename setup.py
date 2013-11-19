import os
from setuptools import setup, find_packages


# copied from the setuptools documentation
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

description = """A collection of common fabric tasks for dbs, webservers,
scm's etc.""" 

classifiers = [
    "Topic :: Deployment",
    ]

requires = [
    'fabric',
    'pyyaml',
    'voluptuous==0.8.4',
]

setup(
    name='fabextns',
    version='0.0.1',
    author='Mukund Krishnamurthy',
    author_email='mukund.kri@gmail.com',
    description=description,

    license='Unknown',
    keywords='fabric-extensions deploy',
    long_description=read('README'),
    
    classifiers=classifiers,
    install_requires=requires,
    packages=find_packages(),
    zip_safe=True
    
)
