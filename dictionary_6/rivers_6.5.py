rivers = {'Volga': 'Russia', 'Don': 'Russia', 'Rhine': 'Germany'}
for river, country in rivers.items():
    print(f'The {river} runs through {country}')
print('\n')

for river in rivers.keys():
    print(f'The {river}')
print('\n')

for country in rivers.values():
    print(country)