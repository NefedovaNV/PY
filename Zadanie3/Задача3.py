def my_func(my_list):
    largest = 0
    second_largest = 0
    for item in my_list:
        if item > largest:
            second_largest = largest
            largest = item
        elif largest > item > second_largest:
            second_largest = item
    return largest, second_largest
my_list = [1, 70, 80]
print (my_func(my_list))




