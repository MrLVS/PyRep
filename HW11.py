# Home work # 11


def letters_range(start, stop, step=1):
    """ Function to generate a list of letters in the desired range."""
    letter_list = [x for x in [chr(i) for i in range(ord(start), ord(stop), step)]]
    print(letter_list)


letters_range('a', 'z')
