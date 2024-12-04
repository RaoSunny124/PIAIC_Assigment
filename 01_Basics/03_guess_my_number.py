def guess_game ():
    import random
    
    guess_my_num = random.randint(0 , 100)
    # print('Guessed number is' , guess_my_num) 
    user_input = int(input('Enter a number:')) 
    if user_input > guess_my_num:
        print('User number is too high.')
    elif user_input < guess_my_num:
        print('User number is too low.')
    elif user_input == guess_my_num:
        print(' Congrats! 🏆 The number was:' , guess_my_num)
    else:
        print('invalid syntax.')               
    print('Guessed number is:' , guess_my_num)

guess_game()  