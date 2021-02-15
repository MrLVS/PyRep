# Написать функцию которая возвращает N-мерный массив с ширинами заданными в аргументе списком из N элементов:
# n_arr([2,2])
# > [[“”,“”],[“”,“”]]
# n_arr([2,2,2])
# > [[[“”,“”],[“”,“”]], [[“”,“”],[“”,“”]]]

import numpy


def n_dimensional_array(dimensions):
    """Function for create n dimensional array."""
    head = dimensions[0]
    tail = dimensions[1:]
    if not tail:
        return list(numpy.repeat("", head))
    else:
        list_1 = []
        for i in range(head):
            list_1.append(n_dimensional_array(tail))
        return list_1


print(n_dimensional_array([2, 2]))
