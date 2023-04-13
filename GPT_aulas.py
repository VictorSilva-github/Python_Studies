


"""# Day 1 - Hello World
print("Hello, World!")

# Day 2 - Variables and Data Types
name = input("What's your name? ")
age = int(input("How old are you? "))
print("Hello, " + name + "! You are " + str(age) + " years old.")

# Day 3 - Control Structures
for i in range(1, 11):
    print(i)

# Day 4 - Functions
def add(a, b):
    return a * b

result = add(3, 4)
print(result)



# Day 5 - Lists and Tuples
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.remove("apple")
print(fruits)



# Day 6 - Dictionaries
counts = {}
with open("input.txt", "r") as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
with open("output.txt", "w") as file:
    for word, count in counts.items():
        file.write(word + ": " + str(count) + "\n")



# Day 7 - Modules
import math
result = math.sqrt(16)
print(result)


# Day 8 - File Input and Output
with open("input.txt", "r") as file:
    data = file.read()
with open("output.txt", "w") as file:
    file.write(data)


# Day 9 - Exception Handling
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("That's not a number. Please try again.")



# Day 10 - Classes and Objects
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, other_name):
        print("Hello, " + other_name + "! My name is " + self.name + ".")

person = Person("Alice")
person.greet("Bob")"""