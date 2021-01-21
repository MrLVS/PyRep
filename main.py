# Pithon script

a = True
b = "True"
c = 1
x = a == c
y = a == b

print(type(a))  # <class 'bool'>
print(type(b))  # <class 'str'>
print(type(x))  # <class 'bool'>
print(x)  # True  bool a соотвествует int c
print(type(y))  # <class 'bool'>
print(y)  # False

name = input("Enter your name: ")
print(name)
