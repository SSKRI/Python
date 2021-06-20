favorite_fruits = ['banana', 'apple', 'orange']
if 'apple' in favorite_fruits:
    print('\nYou really like apple!')
if 'tangerine' in favorite_fruits:
    print('\nYou really like tangerine!')
if 'banana' in favorite_fruits:
    print('\nYou really like banana!')
if 'watermelon' in favorite_fruits:
    print('\nYou really like watermelon!')
if 'orange' in favorite_fruits:
    print('\nYou really like orange!')

fruits = ['tangerine', 'watermelon', 'banana2', 'apple']
for fruit in fruits:
    if fruit in favorite_fruits:
        print(f'\nYou really like {fruit}')