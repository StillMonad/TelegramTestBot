import functools
from transliterate import translit
import sys, getopt


def tr(s):
    """
    cyrillic to latin letters translation
    """
    return translit(s, reversed=True)


def show_call(f):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        print(f.__name__ + ' ', end="")
        return f(*args, **kwargs)

    return inner

