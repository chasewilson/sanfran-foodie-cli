import click
from src import application

@click.group()
def cli():
    """Calls the cli tool as 'foodtruck'. See 'setup.py'"""
    pass

@cli.command
@click.option('--latitude', type=float, help='latitude of the location to find food trucks from.')
@click.option('--longitude', type=float, help='longitude of the location to find food trucks from.')
def nearMe(latitude, longitude):
    """Returns a list of the top 5 closest food trucks"""
    trucks = application.get_foodtrucks(latitude, longitude)
    for truck in trucks:
        print(f"\nCompany: {truck['Applicant']}\nFood: {truck['FoodItems']}\nDistance: {truck['distance']}\n\n")

