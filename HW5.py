print("Введите неотрицательные целые числа, через пробел: ")
answer = input("--> ")


def find_min_int_out_of_string(some_string):
    """ A function to find the minimum number outside the list. """
    int_list = list(map(int, some_string.split()))

    for i in range(len(int_list)):
        if i not in int_list:
            print(i)
            break


find_min_int_out_of_string(answer)

