from clans import *
from format import *


def transform_item(x):
    item = ItemStruct()
    item.icon_urls = x["iconUrls"]
    item.name = x["name"]
    item.id = x["id"]
    item.max_level = x["maxLevel"]
    return item


def transform_item_list(x):
    item_list = ItemListStruct()
    item_list.items = []
    for item in x["items"]:
        item_list.items.append(transform_item(item))
    return item_list

