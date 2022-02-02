#!/usr/bin/python3
"""Load, add, save"""
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    json_list = load_from_json_file('add_item.json')
except:
    json_list = []

for i in argv[1:]:
    json_list.append(i)

save_to_json_file(json_list, 'add_item.json')
