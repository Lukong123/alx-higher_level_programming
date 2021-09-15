#!/usr/bin/python3
def search_replace(my_list, search, replace):
    search_list = [i for i, x in enumerate(my_list) if x == search]
    for i in search_list:
        my_list[i] = replace
        return my_list
