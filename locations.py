from .cards import *
from .format import *


def transform_location(x):
    location = LocationStruct()
    location.localized_name = x['localizedName']
    location.id = x['id']
    location.name = x['name']
    location.is_country = x['isCountry']
    location.country_code = x['countryCode']
    return location


def transform_location_list(x):
    location_list = LocationListStruct()
    location_list.items = []
    for location in x['items']:
        location_list.items.append(transform_location(location))
    return location_list

