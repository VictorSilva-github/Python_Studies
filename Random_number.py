import random

# generate a random integer between 0 and 9
random_number = random.randint(0, 100)

if random_number <= 10:
    print(" Menor que 10")
    print("O numeror menor que 10 foi: ", random_number)
else:
    print("O numero aliatorio foi: ", random_number)
