from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today().date()
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

name = 'thiago'
middlename = 'dos anjos'
birthdate = '1986-08-26'
age = calculate_age(birthdate)
height = 1.73
legal_adults = age >= 18

print('Nome', name)
print('Sobrenome', middlename)
print('Idade', age)
print('Ano de Nascimento', birthdate)
print('É maior de idade', legal_adults)
print('Altura em metros', height)





