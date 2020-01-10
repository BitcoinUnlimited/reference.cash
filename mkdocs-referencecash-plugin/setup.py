import os
from setuptools import setup, find_packages

long_description = (
    "This is a mkdocs plugin used to customize reference.cash."
    "For some reason mkdocs requires this to be an installable package."
)

setup(
    name='mkdocs-referencecash-plugin',
    version='0.1.0',
    description='Plugin used to customize refrence.cash',
    long_description=long_description,
    keywords='mkdocs python markdown',
    url='https://github.com/dagurval/mkdocs-referencecash-plugin',
    author='dagurval',
    author_email='dagurval@pvv.ntnu.no',
    license='MIT',
    python_requires='>=3.0',
    install_requires=[
        'setuptools>=18.5',
        'beautifulsoup4>=4.6.3',
        'mkdocs>=1.0.4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(exclude=['*.tests']),
    entry_points={
        'mkdocs.plugins': [
            'referencecash = referencecash.plugin:ReferenceCashPlugin'
        ]
    }
)
