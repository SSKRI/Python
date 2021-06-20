food = "apple"
print('Is food == "APPLE"? I predict False')
print(food == 'APPLE')

print('\nIs food == "APPLE"? I predict True')
print(food.upper() == 'APPLE')

food = food.upper()
print('\n' + food)
print('Is food != "APPLE"? I predict False')
print(food != 'APPLE')
print('Is food != "APPLE"? I predict True')
print(food.lower() != "APPLE")
print(food.lower())

digit = 23
print('\nIs digit == 23? I predict True')
print(digit == 23)

print('\nIs digit != 15? I predict True')
print(digit != 15)

print('\nIs digit > 8? I predict True')
print(digit > 8)

print('\nIs digit < 0? I predict False')
print(digit < 0)
print('\nIs digit >= 23? I predict True')
print(digit >= 23)

print('\nIs digit <= 116? I predict True')
print(digit <= 116)

digit = -33
print('\nIs digit < 0 and digit < -20? I predict True')
print(digit < 0 and digit < -20)

print('\nIs digit < 0 and digit >= -15? I predict False')
print(digit < 0 and digit >= -15)

print('\nIs digit > 15 or digit < 0? I predict True')
print(digit > 15 or digit < 0)

print('\nIs digit > 15 or digit > -1 I predict False')
print(digit > 15 or digit > -1)

list = [12, 1, 33, 44679, 79, -8]
print('\nIs -8 in list? I predict True')
print(-8 in list)
print('\nIs 15 in list? I predict False')
print(15 in list)

foods = ['meat', 'fish', 'tea']
print('\nIs "koffee" in foods? I predict False')
print('koffee' in foods)
print('\nIs "tea" in foods? I predict True')
print('tea' in foods)
print('\nIs "koffee" not in foods? I predict True')
print('koffee' not in foods)