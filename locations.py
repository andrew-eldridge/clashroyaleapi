from format import *


def transform_location(l):
    location = LocationStruct()
    location.localized_name = c["location"]["localizedName"]
    location.id = c["location"]["id"]
    location.name = c["location"]["name"]
    location.is_country = c["location"]["isCountry"]
    location.country_code = c["location"]["countryCode"]
    return location

