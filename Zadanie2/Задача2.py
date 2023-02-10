new_list = [2, 'Наталья', 50.5, None, complex(5, 6), True, [1, 2, 3]]
i, j = 0, 1
while len(new_list) > j:
    new_list[i], new_list[j] = new_list[j], new_list[i]
    i += 2
    j += 2
print('Результат:', new_list)