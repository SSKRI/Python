my_foods = ['pizza', 'falafel', 'cake']
friend_foods = my_foods
my_foods.append('pie')
friend_foods.append('fish')
print('My favorite foods are:')
for food in my_foods:
    print(food)
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)

my_foods = ['pizza', 'falafel', 'cake']
friend_foods = my_foods[:]
my_foods.append('pie')
friend_foods.append('fish')
print('\nMy favorite foods are:')
for food in my_foods:
    print(food)
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)