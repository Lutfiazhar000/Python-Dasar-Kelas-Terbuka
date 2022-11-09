import string
import random

def random_string(panjang:int) -> str:
    hasil = ''.join(random.choice(string.ascii_letters) for i in range(panjang))
    return hasil
