#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """Replaces all occurences of an element by another"""
    nlist = my_list.copy()
    count = my_list.count(search)
    for i in range(count):
        index = nlist.index(search)
        nlist[index] = replace
    return nlist
