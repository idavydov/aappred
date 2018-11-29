#!/usr/bin/python3
import random

letters = 'ALRKNMDFCPQSETGWHYIV'
n=100000
print('>seq')
print(''.join(random.choices(letters, k=n)))
