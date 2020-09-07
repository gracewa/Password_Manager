from user import User
from random import randint


def new():
    while True:
        print('What would you like to do?' + '\n')
        print('Enter 1 to create a new password manager account, 2 to log into your password manager account:' + '\n')
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
                if selected_password == confirmed_password:
                    print('Congratulations ' + selected_username + '! Your password manager account has been created')

                else:
                    print('Account not created because passwords failed to match again! Try again later')

            else:
                print('Congratulations ' + selected_username + '! Your password manager account has been created')
        with open('users.txt', 'a') as userfile:
            userfile.write(selected_username + '@@@' + selected_password + '\n')
        continue
        if selection == 2:




if __name__ == '__main__':
    new()
