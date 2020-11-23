def vowel_count(phrase):
    VOWELS = set("aeiou")

    phrase = phrase.lower()
    counter = {}

    for ltr in phrase:
        if ltr in VOWELS:
            counter[ltr] = counter.get(ltr, 0) + 1

    return counter

print(vowel_count('rithm school'))
