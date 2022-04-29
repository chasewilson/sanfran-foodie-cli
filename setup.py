from importlib.metadata import entry_points
from pkg_resources import require
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name = 'SanFran Foodie CLI',
    version = '0.0.1',
    author = 'Chase Wilson',
    license = 'MIT',
    description = 'Find food trucks near specified location',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/chasewilson/sanfran-foodie-cli',
    py_modules = ['my_tool', 'src'],
    packages = find_packages(),
    install_requires = ['click (>=7.1.2)'],
    python_requires = '>=3.7',
    entry_points = '''
        [console_scripts]
        foodtruck=my_tool:cli
    '''
)