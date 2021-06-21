favorite_languages = {
    'Elena': 'JS',
    'Tobik': 'Python',
    'Sveta': 'Python',
    'Anna': 'C',
}
people = ['Anna', 'Tamara', 'Rem', 'Opra', 'Elena']
for person in people:
    if person in favorite_languages.keys():
        print(f'{person}, thank you for participating in the survey')
    else:
        print(f'{person}, we invite you to take part in the survey')
