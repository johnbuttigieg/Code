
name = input('What is your name?')
choice = input('Type H to be greeted, type G to be farewelled or type Q to quit the program').upper()
while choice != 'Q':
    if choice == 'H':
        print('Hello', name)

    elif choice == 'G':
        print('Goodbye', name)

    else:
        print('Invalid message')

    choice = input('Type H to be greeted, type G to be farewelled or type Q to quit the program').upper()



