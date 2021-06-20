gests = ['Лорак', 'Бланшет', 'Мадонна']
print(gests)
invite = f'Уважаемая, {gests[0]}, приглашаю Вас на обед.\nУважаемая\
, {gests[1]}, приглашаю Вас на обед.\nУважаемая, {gests[2]}, приглашаю Вас\
 на обед.'
print(invite)
print(f'{gests[0]} прийти не сможет')
gests[0] = 'красотка'
invite = 'приглашаю Вас на обед.'
print(f'Уважаемая, {gests[0]}, {invite}')
print(f'Уважаемая, {gests[1]}, {invite}')
print(f'Уважаемая, {gests[2]}, {invite}')
print("Список гостей расширен до 6 человек.")
gests.insert(0, 'Пугачева')
gests.insert(2, 'Галкин')
gests.append('Петросян')
print(gests)
print(f'Уважаемая, {gests[0]}, {invite}')
print(f'Уважаемая, {gests[1].title()}, {invite}')
print(f'Уважаемый, {gests[2]}, {invite}')
print(f'Уважаемая, {gests[3]}, {invite}')
print(f'Уважаемая, {gests[4]}, {invite}')
print(f'Уважаемый, {gests[5]}, {invite}')
print(f'На обед приглашено {len(gests)} человек')
print("Нихрена стол не приедет, на обед приглашаю только 2 гостя.")
del_guest = gests.pop()
print(f'{del_guest}, я сожалею, что отменяю приглашение!')
del_guest = gests.pop()
print(f'{del_guest}, я сожалею, что отменяю приглашение!')
del_guest = gests.pop()
print(f'{del_guest}, я сожалею, что отменяю приглашение!')
del_guest = gests.pop()
print(f'{del_guest}, я сожалею, что отменяю приглашение!')
print(f'На обед приглашено только {len(gests)} гостя')
print(f'{gests[0]}, более раннее приглашение остается в силе!')
print(f'{gests[1].title()}, более раннее приглашение остается в силе!')
del gests[1]
del gests[0]
print(gests)