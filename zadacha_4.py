dict1 = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

rnum = str(input('Введите римское число: '))

if len(rnum) == 1:
    print(f'Арабское число: {dict1[rnum]}')
elif len(rnum) > 1:
    list1 = []
    for i in range(len(rnum)):
        list1.append(rnum[i])
    anum = 0
    for i in range(len(list1)-1):
        if dict1[list1[i]] < dict1[list1[i+1]]:
            anum = anum - dict1[list1[i]]
        elif dict1[list1[i]] > dict1[list1[i+1]] or dict1[list1[i]] == dict1[list1[i+1]]:
            anum = anum + dict1[list1[i]]
    anum = anum + dict1[list1[-1]]
    print(f'\nАрабское число: {anum}')
elif len(rnum) == 0:
    print('!!!ОШИБКА!!!: Вы не ввели римкое число')
