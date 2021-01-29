# palindrome

def decimal_palindrome(number):
    number = str(number)
    if number == number[::-1]:
        return number


def binary_palindrome(number):
    number = bin(number)[2:]
    if number == number[::-1]:
        return number


def find_billion_palindrome(bilrange = 1000000):
    sum = 0
    for i in range(1,bilrange):
        if decimal_palindrome(i) and binary_palindrome(i):
            sum += i
    print(sum)

find_billion_palindrome()


