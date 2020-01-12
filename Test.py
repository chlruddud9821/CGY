from random import random

count = 0

for i in range(30000):
    if random()**2+random()**2 <= 1:
        count += 1

print(4*count/i)