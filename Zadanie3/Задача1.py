def div_func():
    global var_1, var_2
    var_1 = int(input("Укажите первое число: "))
    var_2 = int(input("Укажите второе число: "))
    if var_2 == 0:
        print ("Ошибка")
    else:
        return var_1 / var_2

s = div_func()
print (s)







