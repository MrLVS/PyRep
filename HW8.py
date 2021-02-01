import time

"""Функция для преобразования строки в число с помощью рекурсии. Проверяет возможность преобразования строки в число,
если число четное, то делит его на 2, в противном случае на 3."""


def converting_str_to_int():
    enter = input("""Введите текст.\n--> """)
    if enter.isdigit():
        print("""Колдуем...\nОжидайте ответ.""")
        time.sleep(1.5)

        def str_to_int(text):
            if text:
                return (ord(text[-1]) - ord('0')) + 10 * str_to_int(text[:-1])
            else:
                return 0

        resNumber = str_to_int(enter)

        if resNumber % 2 == 0:
            print(resNumber / 2)
        else:
            print(resNumber * 3 + 1)

        converting_str_to_int()

    elif enter == "cancel":
        exit()

    elif not enter.isdigit():
        print("Не удалось преобразовать текст в число, попробуйте еще раз.")
        print('Если хотите закрыть программу, введите "cancel"')
        converting_str_to_int()


converting_str_to_int()
