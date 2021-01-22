# input function

list = []
print("Введите любые слова, слоги или числа и разделите их пробелом.")
text = input("--> ")

splittext = text.split()

for i in splittext:
    if i not in list:
        list.append(i)

print(splittext)

print(list)