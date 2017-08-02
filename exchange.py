#!/usr/bin/env python

""""A commandline application built using python to see currency exchange rates."""

import urllib.parse
import requests
import click

__author__ = "Anshul Chauhan"
__copyright__ = "Copyright 2017, Anshul Chauhan"
__license__ = "MIT"
__version__ = "0.1"
__email__ = "anshulchauhan@outlook.com"

@click.command()
@click.option('--curr_from', '-f', default = 'USD', type = str, help = 'This the currency you are trying to convert from.')
@click.option('--curr_to', '-t', default = 'INR', type = str, help = 'This is the currency you\'re converting to.')
@click.option('--value', '-v', default = 1, type = float, help = 'The amount you want to convert.')

def cli(curr_from, curr_to, value):

    if curr_from == curr_to:
        click.echo("1.00")

    main_api = 'http://api.fixer.io/latest?'

    url = main_api + urllib.parse.urlencode({'base':curr_from})

    json_data = requests.get(url).json()
    click.echo(json_data['rates'][curr_to] * value)