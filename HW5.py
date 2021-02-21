print("Введите неотрицательные целые числа, через пробел: ")
answer = input("--> ")

def find_min_int_out_of_string(some_string):
    """ A function to find the minimum number outside the list. """
    int_list = list(map(int, some_string.split()))

    for i in range(1, max(int_list)+1):
        if i not in int_list:
            print(i)
            break
        elif i not in int_list and i == 1:
            print(max(int_list)+1)
            break
        elif i == max(int_list):
            print(max(int_list)+1)
            break


find_min_int_out_of_string(answer)
