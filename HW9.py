# ProjectEuler.ru,  problem solutions №№ 6, 9 , 40, 48

import time
from itertools import combinations
import numpy


# Solution problem #6
def difference_squares_sum(number=100):
    result = sum([i for i in range(number + 1)]) ** 2 - sum([i ** 2 for i in range(number + 1)])
    print("Solution problem #6")
    print(f"Разница сумм квадратов = {result}\n")
    return result


difference_squares_sum()


# problem #9
# solution #1
def pythagorean_triplet_list_comprehension():
    triplet = [[a, b, (a ** 2 + b ** 2) ** 0.5] for a, b in combinations(range(1, 500), 2) if
               1000000 - 2000 * a - 2000 * b + 2 * a * b == 0]

    triplet2 = [[a, b, 1000 - a - b] for a in range(1, 333) for b in range(a + 1, 500) if
                a ** 2 + b ** 2 == (1000 - a - b) ** 2]
    result = numpy.prod(triplet)
    result2 = numpy.prod(triplet2)
    print("Solution problem #9")
    print(f"Тройки пифагора {triplet}, произведение {result} - list comprehension var 1")
    print(f"Тройки пифагора {triplet2}, произведение {result2} - list comprehension var 2\n")


start_time = time.time()
pythagorean_triplet_list_comprehension()
end_time = time.time()
print("Время выполнения", end_time - start_time)


# problem #9
# solution #2 more quickly that solution #1 Euclid formula (a=m ^ 2 - n ^ 2, b = 2mn, c = m ^ 2 + n ^ 2)
def pythagorean_triplet_m_n():
    for n in range(1, 32):
        for m in range(1, 32):
            a = n ** 2 - m ** 2
            b = 2 * n * m
            c = n ** 2 + m ** 2
            if a + b + c == 1000:
                return a * b * c


start_time1 = time.time()
print("Solution problem #9")
print(pythagorean_triplet_m_n(), " - более быстрое решение через формулу Эйлера, но с применением циклов.")
end_time1 = time.time()
print("Время выполнения", end_time1 - start_time1, "\n")


# Solution problem #40
list_d = [int(num) for num in ''.join((str(num) for num in range(186000)))]
print("Solution problem #40")
print(list_d[1] * list_d[10] * list_d[100] * list_d[1000] * list_d[10000] * list_d[100000] * list_d[1000000], "\n")

# Solution problem #48

a = str(sum([pow(x, x) for x in range(1001)]))
print("Solution problem #48")
print(a[-10:])
