list1 = []
for i in range(1, 101):
    list1.append(i)
print(f'Первоначальный список:\n {list1}')

for i in range(len(list1)):
    if (list1[i] % 3 == 0) and (list1[i] % 5 == 0):
        list1[i] = 'FizzBuzz'
    elif list1[i] % 3 == 0:
        list1[i] = 'Fizz'
    elif list1[i] % 5 == 0:
        list1[i] = 'Buzz'

print(f'\nПолученный список:\n {list1}')
