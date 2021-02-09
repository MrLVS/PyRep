# Solution of the Collatz Hypothesis


def Collatz(number):
    """ A function that divides a number by two if the number is even,
     divides by three if the number is not even, and starts a new loop.
      Counts the number of cycles until the number is exactly 1. """
    i = 0
    while number > 1:
        if number % 2 == 0:
            number = number / 2
            i += 1
        elif number % 2 != 0:
            number = number * 3 + 1
            i += 1
    print(i)


Collatz(12)
