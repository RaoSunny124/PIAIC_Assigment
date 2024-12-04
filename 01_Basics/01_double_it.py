def number_double():
    user_input = int(input('Enter a number:'))
    if user_input >= 100:
        print('Your number is incorrect.')
    else:
        while user_input <= 100:
         user_input = user_input*2
         print(user_input , end=" ")
    print('number is higher than 100')


number_double()