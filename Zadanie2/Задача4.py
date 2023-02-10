user_str = input("Введите несколько слов, разделенных пробелами: ").split()
for i, el in enumerate(user_str, 1):
    print(f'{i}. {el[:10]}')
