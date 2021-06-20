names = ['Андрей', "Петр", "Светлана", "admin", "Лена", 'kirill', 'tobik']
# names = []
if names:
    for name in names:
        if name == 'admin':
            print('\nHello, admin, would you like to see a status report?')
        else:
            print(f'\nHello, {name}, thank you for logging in again')
else:
    print('We need to ind some users')