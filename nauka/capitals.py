from random import choice

capitals = {
    'Poland' : 'Warsaw',
    'Germany' : 'Berlin',
    "France" : 'Paris',
    'Spain' : 'Madrit',
    'Italy' : 'Rome',
    'Netherlands' : 'Amsterdam',
    'Czechia' : 'Prague',
    'Grece' : 'Athens',
    'Portugal' : 'Lisabon',
    'Hungary' : 'Budapest'
}

select_country = choice(list(capitals.keys()))

print('What is the capital of', select_country,'?')

capital = input('The capital is: ')

if capitals[select_country] == capital.capitalize():
    print('Very good!')
else:
    print('Wrong answer! The capital is', capitals[select_country])