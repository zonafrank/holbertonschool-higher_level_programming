#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return [(lambda x: x if x != search else replace)(item)
            for item in my_list]
