import click
from src import application

@click.group()
def cli():
    """Calls the cli tool as 'foodtruck'. See 'setup.py'"""
    pass

@cli.command
def nearMe():
    """Returns a list of the top 5 closest food trucks"""


