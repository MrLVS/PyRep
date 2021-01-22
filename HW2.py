# input function


emptylist = []
print("Введите любые слова, слоги или числа и разделите их пробелом.")
answer = input("--> ")


def functionone(text):
    splittext = text.split()

    for i in splittext:
        if i not in list:
            list.append(i)

    print(splittext)
    print(list)


functionone(answer)


def functiontwo(text):
    splittext = set(text.split())

    print(splittext)


functiontwo(answer)
