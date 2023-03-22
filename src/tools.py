from transliterate import translit


def tr(s):
    return translit(s, reversed=True)
