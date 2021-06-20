'''for number in range(1, 21):
    print(number)'''
numbers = list(range(1, 1_000_001))
'''for number in numbers:
    print(number)
print(numbers)'''
print(min(numbers))
print(max(numbers))
print(sum(numbers))
numbers = list(range(1, 21, 2))
print(numbers)
for number in numbers:
    print(number)

print('\n')
numbers = list(range(3, 31, 3))
print(numbers)
for number in numbers:
    print(number)

print('\n')
numbers = []
for number in range(1, 11):
    numbers.append(number ** 3)
    print(number ** 3)
print(numbers)

numbers = [number ** 3 for number in range(1, 11)]
print(numbers)
print(f'\nThe irst three items in the list are:\n{numbers[:3]}')
print(f'\nThree items from the middle of the list are:\n{numbers[4:7]}')
print(f'\nThe last three items in the list are:\n{numbers[-3:]}')
mid_list = len(numbers) / 2 - 1
print(mid_list)
print(f'\nThree items from the middle of the list are:\n{numbers[mid_list:(mid_list + 3)]}')
print(numbers[1:8:3])