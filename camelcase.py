def camelcase(s):
    return len([s for letter in s if letter.isupper()]) + 1