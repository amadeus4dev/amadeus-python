import io
import os

from setuptools import setup, find_packages

# Load the version number
about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'amadeus', 'version.py')) as f:
    exec(f.read(), about)

# Import the README and use it as the long-description.
with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
    name='amadeus',
    version=about['version'],
    description='Python module for the Amadeus travel APIs',
    long_description=long_description,
    author='Amadeus',
    author_email='developers@amadeus.com',
    python_requires='>=2.7.0',
    url='https://github.com/amadeus4dev/amadeus-python',
    install_requires=[],
    packages=find_packages(),
    data_files=[('docs', ['README.rst', 'CHANGELOG.rst'])],
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
