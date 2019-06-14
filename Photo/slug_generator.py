from string import ascii_letters
from random import choice
def slug_generator():
    numer = '123456789'
    all_char = ascii_letters
    all_char += numer
    slug = ''

    for i in range(0,1):
        slug += choice(all_char)
    return slug
