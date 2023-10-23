from setuptools import setup, find_packages
from pkg_resources import parse_requirements

with open('requirements.txt') as f:
    requirements = [str(req) for req in parse_requirements(f)]


setup(
    name='p2p_correspondence',
    version='0.1.0',
    include_package_data=True,
    packages=find_packages(),
    install_requires=requirements,
    author='Shahar Zuler',
    author_email='shahar.zuler@gmail.com',
    description='Surface point-to-point correspondence using zoomout',
    url='https://github.com/shaharzuler/p2p_correspondence',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)