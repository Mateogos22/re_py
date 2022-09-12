import datetime

name = input('Enter your name: ')

print("Hello", name,", enter your age and I'll tell you when you turn 75 years old")

age = int(input('Enter your age: '))

year = datetime.datetime.now().year

age75 = year - age + 75

print(name + ", you will be 75 years old in the year " + str(age75))
