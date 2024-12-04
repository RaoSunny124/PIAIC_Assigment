def random_number():
    from random import randint

    for x in range(1 , 11):
        random_number = randint(1 , 101)
        print(random_number , end=" ")

random_number()   