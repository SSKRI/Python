menu = ('fish', 'meat', 'pie', 'cake', 'juice')
print('Menu:')
for food in menu:
    print(f'\t{food}')
    print('\t' + food)
print('\n' + menu[0])
# menu[0] = 'tea'
menu = ('fish', 'meat', 'pei', 'tea', 'coffee')
print('New_menu:')
for food in menu:
    print(f'\t{food}')