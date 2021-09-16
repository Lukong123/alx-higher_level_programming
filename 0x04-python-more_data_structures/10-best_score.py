#!/usr/bin/python3
def best_score(a_dictionary):
    """ returns a key with the biggest integer value """
    maxvalue = 0
    maxkey = None
    if a_dictionary:
        for key in a_dictionary:
            if a_dictionary[key] > maxvalue:
                maxvalue = a_dictionary[key]
                maxkey = key
    return maxkey
