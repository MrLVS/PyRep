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



print(type(a))  # <class 'bool'>
print(type(b))  # <class 'str'>
print(type(x))  # <class 'bool'>
print(x)  # True  bool a(True) соотвествует int c(1)
print(type(y))  # <class 'bool'>
print(y)  # False
print(z) # True bool d(False) соответствует int e(0)
print(w) # False

# input demonstration
name = input("Enter your name: ")
print(name)
print(type(name))

numbers = input("Enter your Age: ")
print(numbers)
print(type(numbers))
