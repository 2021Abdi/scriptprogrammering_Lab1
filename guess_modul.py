def Gissa_tal():
    import random
    försök = 0
    random_number = random.randint(1, 100)
    while True:
        number = int(input("Gissa tal mellan 0-100: "))
        if random_number < number:
            försök = försök + 1
            print("För stor försök igen.")
        elif random_number > number:
            försök = försök + 1
            print("För lite försök igen.")
        else:
            print("yässs du fick den på {0} försök".format(försök))
            break
