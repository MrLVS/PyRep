print("Введите неотрицательные целые числа, через пробел: ")
answer = input("--> ")


def find_min_int_out_of_string(some_string):
    """ A function to find the minimum number outside the list. """
    int_list = list(map(int, some_string.split()))

    check =[]
    for i in range(1, len(int_list)):
        if i in int_list:
            continue
        elif i not in int_list:
            print(i)
            check.append(i)
            break

    if check:
        pass
    else:
        print(len(int_list)+1)


find_min_int_out_of_string(answer)
