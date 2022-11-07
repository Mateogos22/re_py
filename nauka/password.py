password = input('Podaj hasło: ')

lowercase = False
uppercase = False
space = False
special_character = False

for char in password:
    if char.islower():
        lowercase = True
    elif char.isupper():
        uppercase = True
    elif char.isspace():
        space = True
    else:
        special_character = True
password_lenght = len(password) >= 8

correct_pass = lowercase and uppercase and special_character and not space

if correct_pass:
    print('Twoje hasło jest odpowiednie')
else:
    print('Twoje hasło nie jest bezpieczne!')
    if not lowercase:
        print('* Hasło musi zawierać jedną małą literę')
    if not uppercase:
        print('* Hasło musi zawierać jedną dużą literę')
    if not special_character:
        print('* Hasło musi zawierać jeden znak specjalny')
    if space == True:
        print('* Hasło NIE może zawierać spacji!')
    if not password_lenght:
        print('* Hasło musi zawierać minimum 8 znaków')