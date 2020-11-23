import sys
from setuptools import setup

if sys.version_info < (3, 6):
    sys.exit('Sorry, zgtf requires Python >= 3.6')

requirements = [
    "pandas>=0.25",
    "scikit-learn>=0.22",
    "matplotlib>=3.1.3",
    "numpy>=1.16"
]

setup(
    name='zpca',
    version='0.8.2',
    description="PCA analysis for genes or transcripts.",
    author="Foivos Gypas",
    author_email='fgypas@gmail.com',
    url='',
    packages=['zpca'],
    package_dir={'zpca': 'zpca'},
    include_package_data=True,
    scripts=['scripts/zpca-counts', 'scripts/zpca-tpm'],
    install_requires=requirements,
    keywords='zpca',
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ]
)
