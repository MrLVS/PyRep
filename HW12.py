#Function Fibonacci,


def fib():
    """ Fibonacci function with output of all elements of the sequence."""
    n = int(input("Введите желаемый номер элемента из ряда Фибоначчи: \n-->"))

    def fibrec(n):
        if n < 3:
            return 1
        return fibrec(n - 1) + fibrec(n - 2)

    list_digit = [fibrec(i) for i in range(n+1)]
    print(list_digit)

fib()
