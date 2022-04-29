from importlib.metadata import entry_points
from pkg_resources import require
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'SanFran Foodie CLI',
    version = '0.0.1',
    author = 'Chase Wilson',
    license = 'MIT'
    description = 'Find food trucks near specified location',
    long_description = long_description
    long_description_content_type = "text/markdown"
    url = 'https://github.com/chasewilson/sanfran-foodie-cli',
    py_modules = ['my_tool', 'src'],
    packages = find_packages()
    requires = [requirements],
    python_requires = '>=3.7',
    entry_points = '''
        [console_scripts]
        foodtruck=my_tool:cli
    '''
)