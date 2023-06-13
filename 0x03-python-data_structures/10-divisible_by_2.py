#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    new_list = []
    for i in range(len(my_list)):
        temp = my_list[i]
        if temp % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
