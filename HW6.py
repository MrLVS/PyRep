# palindrome

def decimal_palindrome(number):
    number = str(number)
    if number == number[::-1]:
        return number


def binary_palindrome(number):
    number = bin(number)[2:]
    if number == number[::-1]:
        return number


def find_billion_palindrome(billionrange=1000000):
    totalsum = 0
    for i in range(billionrange):
        if decimal_palindrome(i) and binary_palindrome(i):
            totalsum += i
    print(totalsum)


find_billion_palindrome()
