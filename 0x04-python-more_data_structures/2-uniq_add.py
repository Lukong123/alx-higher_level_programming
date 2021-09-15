#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = set(my_list)
    stack = 0
    for i in my_list:
        stack = stack + i
    return stack
