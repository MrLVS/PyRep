print("Введите неотрицательные целые числа, через пробел: ")
answer = input("--> ")


def find_min_int_out_of_string(some_string):
    int_list = list(map(int, some_string.split()))

    print(int_list)
    for i in range(1, len(int_list)):
        if i not in int_list:
            print(i)
            break





find_min_int_out_of_string(answer)

