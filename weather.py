"""Query wunderground.com for city weather conditions.

Interfaces with Weather Underground API.  Default city is Philadelphia, PA.

Resources:
- https://www.wunderground.com/weather/api
- https://www.wunderground.com/weather/api/d/docs

Logo: https://icons.wxug.com/logos/JPG/wundergroundLogo_4c.jpg
"""

# My key is fec1d891d64ec80a; Project name: Philly Weather

__author__ = 'Brad Solomon <brad.solomon.1124@gmail.com>'
__all__ = ['get_current', 'CityWeather', 'get_json']

import requests

from tabulate import tabulate


UN = {
    'IMPERIAL' : ('F', 'MPH', 'MI', 'IN', ),
    'METRIC' : ('C', 'KPH', 'KM', 'METRIC')
    }


def _check_units(units):
    units = units.upper()
    if units in UN:
        units = UN[units]
        return units
    else:
        raise ValueError("`units` must one in ('imperial', 'metric'),"
                         " case-insensitive.")       


class CityWeather(object):
    """Class-based implementation designed for repeated requests."""
    def __init__(self, key, state='PA', city='Philadelphia'):
        self.key = key
        self.state = state
        self.city = city
        self.data = get_json(self.key, self.state, self.city)

    @property
    def observation_location(self):
        return self.data['observation_location']

    @property
    def all_weather_stats(self):
        """Excludes location data."""
        return {k: v for k, v in self.data.items() if not k.endswith('_location')}

    def filter_units(self, units='imperial'):
        """Filter *out* the specified unit measurements from statistics."""
        units = tuple('_{}'.format(i.lower()) for i in _check_units(units))
        return {k: v for k, v in self.data.items() 
                if not k.endswith(units)}


def get_json(key, state='PA', city='Philadelphia'):
    """Helper function to get json via http request and return dictionary."""
    url = 'http://api.wunderground.com/api/{0}/conditions/q/{1}/{2}.json'\
        .format(key, state, city)
    # We really arent' interested in the 'response' key; it's just metadata
    data = requests.get(url).json()['current_observation']
    return data


def get_current(key, units='imperial', state='PA', city='Philadelphia'):
    """Query city/state and print a selected set of current measurements.""" 
    units = _check_units(units)
    data = get_json(key=key, state=state, city=city)
    stats = [
        ['Temperature ({})'.format(units[0]), 
            data['temp_{}'.format(units[0].lower())]],
        ['Weather', data['weather']],
        ['Dew point ({})'.format(units[0]), 
            data['dewpoint_{}'.format(units[0].lower())]],
        ['Wind chill ({})'.format(units[0]), 
            data['windchill_{}'.format(units[0].lower())]],
        ['Feels like ({})'.format(units[0]), 
            float(data['feelslike_{}'.format(units[0].lower())])],
        ['Wind ({})'.format(units[1]), 
            float(data['wind_{}'.format(units[1].lower())])],
        ['Visibility ({})'.format(units[2]), 
            float(data['visibility_{}'.format(units[2].lower())])],
        ['Time', data['observation_time_rfc822']]
        ]
    print(tabulate(stats, headers=['Measurement', 'Value']))