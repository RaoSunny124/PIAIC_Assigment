def joke():
    user_input : str = input('What do u want:').strip().lower()
    joke : str = "I'll meet you at the corner!😄"
    sorry :str = 'Sorry , I only tell one joke.'
    if user_input == 'joke':
        print(joke)
    else:
        print(sorry) 


joke()