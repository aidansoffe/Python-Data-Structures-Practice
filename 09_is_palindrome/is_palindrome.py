def is_palindrome(phrase):
    normalized = phrase.lower().replace(' ', '')
    return normalized == normalized[::-1]


print(is_palindrome("race carl"))  