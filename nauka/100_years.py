import datetime

name = input('Enter your name: ')

print("Hello", name,", enter your age and I'll tell you when you turn 100 years old")

age = int(input('Enter your age: '))

year = datetime.datetime.now().year

age100 = year - age + 100

print(name + ", you will be 100 years old in the year " + str(age100))
