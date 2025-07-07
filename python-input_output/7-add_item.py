#!/usr/bin/python3
"""Task 7. Load, add, save
Add all arguments to a Python list, and then save them to a file
"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


fileName = "add_item.json"

if os.path.isfile(fileName):
    new_list = load_from_json_file(fileName)
else:
    new_list = []

for i in range(1, len(sys.argv)):
    new_list.append(sys.argv[i])

save_to_json_file(new_list, fileName)
