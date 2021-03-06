# Food Truck finding command line tool

As someone who spends a lot of time in a terminal and enjoys the easy access to information I chose to create a command line tool to meet the requirements.

SanFran foodie cli is a command line tool that allows you to find food trucks near a location specified in your command.

## Long Description

Currently, you can use the `nearme` command to list the 5 closest food trucks to the specified latitude and longitude:

```bash
foodtruck nearme --latitude 37.7749295  --longitude -122.4194155
```

## Data information

All food truck data is extracted from the [San Fransisco DataSf Mobile Food Facility permit site](https://data.sfgov.org/Economy-and-Community/Mobile-Food-Facility-Permit/rqzj-sfat/data) and can be updated by downloading the latest CSV file and placed in the `sanfran-foodie-cli/data` folder replacing the old one by naming it: `ft_data.csv`

## Getting started

### Prerequisites

Must have Python 3.7 or greater installed to run this project.
See [Python installation instructions](https://www.python.org/downloads/)

### Setup

The setup and operation of this tool can be completed entirely in a terminal

1. Open your terminal of choice.
1. Change your directory to the root directory of sanfran-foodie-cli. e.g. `cd C:\source\sanfran-foodie-cli`
1. Create a virtual environment:

    - Windows: `python -m venv venv`
    - macOS/Linux: `python3 -m venv venv`
1. Activate virtual environment - For more information about virtual environments, see [this documentation](https://docs.python.org/3/tutorial/venv.html).

    - Windows: `. .\venv\Scripts\Activate.ps1`
    - macOS/Linux: `source venv/bin/activate`

1. Run `setup.py`: This will also install the `click` python module which allows for extra features for python CLI tools rather than just using `sys.argv`.

    - Windows: `python setup.py install`
    - macOS/Linux: `python3 setup.py install`

## Running the tool

You should now be ready to run the tool.

> **NOTE:** The food trucks used are only ones in an approved state. There won't ben any listed with expired or in review applications.

You will call the tool by typing `foodtruck` into your terminal. This by itself won't do anything currently but in the future could list all options available. For now, the tool only has one command and functionality.

### `foodtruck nearme`

You can use `foodtruck nearme` to list the **5** closest food trucks based on a latitude and longitude you provide using the `--latitude` and `--longitude` parameters.

```bash
foodtruck nearme --latitude 37.7749295  --longitude -122.4194155

# output is abbreviated for brevity
Company: Bay Area Mobile Catering, Inc. dba. Taqueria Angelica's
Food: Tacos: burritos: soda & juice
Distance: 0.10845063959495266

....
```

**NOTE:** To deactivate the virtual environment, regardless of OS, enter `deactivate` in your terminal.

### output

The output is a list of the 5 closest food trucks and provides the company name(`Company`), the type of food(`Food`), and the distance to truck in miles(`Distance`).

## Known issues

### Dirty data

The data used has multiples of different food trucks due to it being a list of food truck applicants and SF requires an application for any location a food truck will be located.

**TODO:** Clean data to resolve unique food trucks.

## Future ideas

### Filter by food type

User could specify the type of food they want and receive a filtered list of closest food trucks by food type.

### Choose how many trucks to return

A parameter can be added to allow the user to return as many trucks they would like to see.

### Reach out for automatic updates to data

According to the site, the data is updated weekly. Functionality could be added to see if there should be updated data and then update it's data automatically for accuracy.

### Adjust for multiple possible locations

Currently the data includes multiple entries for possible locations of a given food truck. The data could be adjusted to provide all possible locations of a foodtruck to ensure the customer could search more for current location or try multiple locations to get their delicious food.

## Final Notes

There is a lot of work left to do to make this tool production ready including:

- fixing warnings in `setup.py`
- distribution tasks
- verifying input
- error handling
- improving ease of use (lat and long is difficult for a user to use for example)
- command and feature discovery in-tool
- in-tool help
- unit testing
- and the list goes on.

## Development thought process and trade offs

I started with focusing on delivering something functional in the allotted time and then improving over time. This comes with benefits and tradeoffs as I'll explain below.

### Python

Choosing Python was in part made by familiarity as well as attempting something new. I could have easily written a PowerShell module to work well in a PowerShell sessions and gained benefits like tab completion. However, I wanted to be able to attempt to build my own working CLI and explore the process a bit more.

Python is much more performant than PowerShell but still not near as performant as other option. For example, Go, could have brought many benefits like speed and better deliverable packaging. I.e. a single executable after compilation rather than an entire python package. If I were to hand this off to another team afterwards, my choice would have likely been driven by what the receiving team felt comfortable with. If i made the app in any choice that the customer would not want to use, it would be better to ensure supportability after I'm gone than a minor performance increase.

### Data

I chose to use local CSV data for two reasons. The amount of data is relatively small and is easy to store locally. This removes reliability of an online connection and isi very fast. The second reason is due to the refresh rate of the data. According to the data source, data is only refreshed once a week meaning there is little risk of the information being outdated especially if there was a refresh check to import updated data.

This doesn't discount the fact that the customer has the potential to receive out of date information or other benefits if the customer wanted to expand the scope of the app. If I were to continue the project, depending on the need of the customer and what they would want to use the tool for, I would build out a data refresh mechanism as well as build out a database to use some of the reliable functionality for geo-location features in something like SQL or Kusto.
