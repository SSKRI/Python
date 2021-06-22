misha = {'first_name': 'misha', 'last_name': 'homutov', 'age': 43,\
    'city': 'Novoch'}
# print(person['first_name'].title())
# print(person['last_name'].title())
# print(person['age'])
# print(person['city'].title())
sweta = {'first_name': 'sweta', 'last_name': 'bukina', 'age': 26,\
    'city': 'Moskow'}
lena = {'first_name': 'elena', 'last_name': 'gorina', 'age': 35,\
    'city': 'Berlin'}
people = [misha, sweta, lena]
# print(people)
for person in people:
    print(person['first_name'].title() + ' ' + person['last_name'].title() + \
        ':')
    for key, value in person.items():
        if key == 'first_name' or key == 'last_name':
            print(f'\t{key}: {value.title()}')
        else:
            print(f'\t{key}: {value}')
    print('\n')
        


