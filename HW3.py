

print("Введите любые слова через пробел и получите .")
answer = input("--> ")


def count_words(text):
    bigdict = dict()
    wordlist = text.lower().split()

    for word in wordlist:
        if word in bigdict:
            bigdict[word] += 1
        else:
            bigdict[word] = 1

    maxdict = max(bigdict.values())

    for key in bigdict:
        if bigdict[key] >= maxdict:
            print(key, bigdict[key])


count_words(answer)
