import io
import os

from setuptools import setup

# Load the version number
about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'amadeus', '__version__.py')) as f:
    exec(f.read(), about)

# Import the README and use it as the long-description.
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
    name='amadeus',
    version=about['__version__'],
    description='Python module for the Amadeus travel APIs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Amadeus',
    author_email='developer@amadeus.com',
    python_requires='>=2.7.0',
    url='https://github.com/amadeusdev/amadeus-python',
    py_modules=['amadeus'],
    install_requires=[],
    package=['amadeus'],
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
