def calc(number1, number2):
    my_list = []
    for i in range(1, 1001):
        if i % number1 == 0 and i % number2 == 0:
            my_list.append(i)
    print(my_list)
