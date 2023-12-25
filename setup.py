# SimpleDES - the simplest wrapper for pyDES library - package setup
# Homepage: https://github.com/greentracery/SimpleDES

from setuptools import setup, find_packages
import simpledes as sd


setup(
    name='SimpleDES',
    description='SimpleDES - the simplest wrapper wrapper for pyDES library',
    url="https://github.com/greentracery/SimpleDES",
    version=sd.__version__,
    packages=find_packages(),
    install_requires=['pyDes']
)
