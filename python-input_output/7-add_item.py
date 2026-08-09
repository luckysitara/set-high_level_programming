
#!/usr/bin/python3
"""
Write a script that adds all
arguments to a Python list, and then
save them to a file
"""
from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = 'add_item.json'
my_list = []

try:
    my_list = load_from_json_file(filename)
except Exception:
    pass

for items in range(1, len(argv)):
    my_list.append(argv[items])

save_to_json_file(my_list, filename)
