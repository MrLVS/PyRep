# ProjectEuler.ru,  problem solutions №№ 6, 9 , 40, 48

from itertools import combinations
import numpy


# Solution problem #6
def difference_squares_sum(number=100):
    """ Function for finding the difference of squares of numbers"""
    result = sum([i for i in range(number + 1)]) ** 2 - sum([i ** 2 for i in range(number + 1)])
    print("Solution problem #6")
    print(f"Разница сумм квадратов = {result}\n")
    return result


difference_squares_sum()


# problem #9
# solution #1
def pythagorean_triplet_list_comprehension():
    """ Function for finding Pythagoras triples with a sum equal to 1000."""
    triplet = numpy.prod([[a, b, (a ** 2 + b ** 2) ** 0.5] for a, b in combinations(range(1, 500), 2) if
                          1000000 - 2000 * a - 2000 * b + 2 * a * b == 0])

    triplet2 = numpy.prod([[a, b, 1000 - a - b] for a in range(1, 333) for b in range(a + 1, 500) if
                           a ** 2 + b ** 2 == (1000 - a - b) ** 2])

    print("Solution problem #9")
    print(f"Тройки пифагора вариант 1 - {triplet} - list comprehension var 1")
    print(f"Тройки пифагора вариант 2 - {triplet2} - list comprehension var 2\n")


pythagorean_triplet_list_comprehension()

# Solution problem #40
list_d = [int(num) for num in ''.join((str(num) for num in range(186000)))]
print("Solution problem #40")
print(list_d[1] * list_d[10] * list_d[100] * list_d[1000] * list_d[10000] * list_d[100000] * list_d[1000000], "\n")

# Solution problem #48
print("Solution problem #48")
print(str(sum([pow(x, x) for x in range(1, 1001)]))[-10:])
