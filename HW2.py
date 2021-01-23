# input function
#


uniqueList = []
print("Введите любые слова, слоги или числа и разделите их пробелом.")
answer = input("--> ")


def functionone(text):
    splittext = text.split()

    for i in splittext:
        if i not in uniqueList:
            uniqueList.append(i)

    print(splittext)
    print(uniqueList)


functionone(answer)


def functiontwo(text):
    splittext = text.split()
    righttext = sorted(set(splittext), key=splittext.index)


    print(splittext)
    print((righttext))


functiontwo(answer)

def functionthree(text):
    splittext = text.split()
    lastlist = list(dict.fromkeys(splittext))
    print(lastlist)

functionthree(answer)
