#!/usr/bin/python3
'''Module for saving argv info via json to file.'''


from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
MyList = argv[1:]
try:
    my_obj = load_from_json_file(filename)
    my_obj += MyList
    save_to_json_file(my_obj, filename)
except:
    my_obj = MyList
    save_to_json_file(my_obj, filename)
