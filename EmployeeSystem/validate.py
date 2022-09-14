def user_selection(user_input):
    while (not str(user_input).isdecimal()) or int(user_input) < 1 or int(user_input) > 5:
        print('Invalid input.')
        user_input = input('Select an option (1-5): ')

    return user_input


def y_or_n(user_input):
    while not(user_input.lower() == 'y' or user_input.lower() == 'n'):
        print('Invalid input.')
        user_input = input('Would you like to perform this action? (Y/N): ')

    return user_input


def id_number(user_input):
    while not (len(user_input) == 5 and user_input.isdecimal()):
        print('Invalid input.')
        user_input = input('Enter 5-digit ID number: ')

    return user_input


def key_in_dictionary(key, dictionary):
    while key not in dictionary:
        print('Invalid input.')
        key = input('Please re-enter value: ')

    return key