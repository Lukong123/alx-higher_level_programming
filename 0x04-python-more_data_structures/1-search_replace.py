#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    search_list = [i for i, x in enumerate(new) if x == search]
    for i in search_list:
        new[i] = replace
        return new
