from user import User
from random import randint


def new():
    print('What would you like to do?' + '\n')
    print('Enter 1 to create a new password manager account, 2 to view saved passwords:' + '\n')
    selection = int(input())
    if selection == 1:
        print('Enter a username for your password manager account:' + '\n')
        selected_username = str(input())
        print('Enter a password for your password manager account:' + '\n')
        selected_password = str(input())
        print('Please enter your password again to confirm:' + '\n')
        confirmed_password = str(input())
        if selected_password != confirmed_password:
            print('Your passwords did not match!')
            print('Enter your password again:'+ '\n')
            selected_password = str(input())
            print('Please enter your password one more time to confirm:' + '\n')
            confirmed_password = str(input())
            print('Congratulations ' + selected_username + '! Your password manager account has been created')
        else:
            print('Congratulations ' + selected_username + '! Your password manager account has been created')



if __name__ == '__main__':
    new()
