# Pithon script

a = True
b = "True"
c = 1
d = False
e = 0
f = "False"
x = a == c
y = a == b
z = d == e
w = f == d
strvar = bool("Любая строка, кроме пустой '', будет True")
nullstr = bool('')
int1 = bool(1)  # Положительные и отрицательные числа, кроме нуля True
int0 = bool(0)  # Число int(0) соответствует False
bool(100.0)  # положительные и отрицательные числа float соответствуют True
bool(0.0)  # соответствует False
bool([])  # пустой список соответствует False
bool([1, 2, 3])  # список с элементами соотвествует True
bool(set())  # пустое множество соответствует False
bool({1, 2, 3})  # множество с элементами соответствует True
bool(())  # пустой кортеж соотвествует False
bool((0,))  # кортеж c элементами соответствует True
bool(0j)  # комплексное число равное нулю соответствует False
bool(-1+0j)  # отрицательные или положительные еомплексные числа соответствуют True

print(type(a))  # <class 'bool'>
print(type(b))  # <class 'str'>
print(type(x))  # <class 'bool'>
print(x)  # True  bool a(True) соотвествует int c(1)
print(type(y))  # <class 'bool'>
print(y)  # False
print(z)  # True bool d(False) соответствует int e(0)
print(w)  # False
print(str)  # True
print(nullstr)  # False

# input demonstration
name = input("Enter your name: ")
print(name)
print(type(name))

numbers = input("Enter your Age: ")
print(numbers)
print(type(numbers))
