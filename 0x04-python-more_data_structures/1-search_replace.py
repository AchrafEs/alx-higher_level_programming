#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replaced_list = []
    for row in my_list:
        row_list =[]
        for element in row:
            if element == search:
                row_list.append(replace)
            else:
                row_list.append(element)
        replaced_list.append(row_list)
    return (replaced_list)
