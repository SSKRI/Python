my_pizzas = ['pepperoni', 'margherita', 'carbonara']
for pizza in my_pizzas:
    print(f'I like {pizza} pizza')
    print('I like ' + pizza + ' pizza')
print('\nI really love pizza!!!')
friend_pizzas = my_pizzas[:]
my_pizzas.append('crudo')
friend_pizzas.append('marinara')
print('\nMy favorite pizzas are:')
for pizza in my_pizzas:
    print('\t' + pizza)
print ('\nMy friend’s favorite pizzas are:')
for pizza in friend_pizzas:
    print('\t' + pizza)