print("Введите любые целые неотрицательные числа, разделенные любым не цифровым литералом(пробел, запятая, буква")
answer = input("--> ")


def find_sum_int_in_string(inputstring):

    sumnumbers = 0
    stringelement = ""

    for letter in inputstring:
        if letter.isdigit():
            stringelement += letter
        elif stringelement != "":
            sumnumbers += int(stringelement)
            stringelement = ""
    if stringelement != "":  # Проверка последнего элемента, если он был числом
        sumnumbers += int(stringelement)

    print(sumnumbers)


find_sum_int_in_string(answer)
