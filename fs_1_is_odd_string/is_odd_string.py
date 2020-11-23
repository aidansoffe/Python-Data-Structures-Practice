def is_odd_string(word):

    length = len(word)
    if (length % 2) == 0:
        return False
    else:
        return True


print(is_odd_string('A'))