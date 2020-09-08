from user import User
from random import randint
import urllib.parse as parse


def new():
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
                with open('users.txt', 'a') as userfile:
                    userfile.write(selected_username + '@@@' + selected_password + '\n')

            else:
                print('Account not created because passwords failed to match again! Try again later')

        else:
            print('Congratulations ' + selected_username + '! Your password manager account has been created')
            with open('users.txt', 'a') as userfile:
                userfile.write(selected_username + '@@@' + selected_password + '\n')

    elif selection == 2:
        logins=[]
        print('Enter your username:' + '\n')
        login_username = str(input())
        print('Enter your password:' + '\n')
        login_password = str(input())
        login_credentials = (login_username + '@@@' + login_password)
        with open('users.txt', 'r', encoding='utf-8') as userfile:
            for line in userfile:
                saved_credentials= line.strip("\n")
                logins.append(saved_credentials)
        if login_credentials in logins:
            print('Login Successful')
        else:
            print('Login Not Successful, Please try again')
            print('Enter your username:' + '\n')
            login_username = str(input())
            print('Enter your password:' + '\n')
            login_password = str(input())
            login_credentials = (login_username + '@@@' + login_password)
            if login_credentials in logins:
                print('Login Successful')
            else:
                print('Login Failed. Try again later!')
        print('Enter 3 to save new credentials OR 4 to view saved credentials:' + '\n')
        credential_selection = int(input())
        if credential_selection == 3:
            credential_website = str(input("Please enter the website url here: "))
            parsed_url = parse.urlparse(credential_website)
            parsed_domain = parsed_url.netloc
            credential_username = str(input("Please enter your " + parsed_domain + " user name: "))
            credential_password = str(input("Please enter the password here: "))

            file_name = str(login_credentials) + '.txt'
            try:
                with open(file_name, 'a', encoding='utf-8') as usercredentials:
                    usercredentials.write(credential_website + '@@@' + credential_username + '@@@' + credential_password + '\n')
                    print('Credentials Saved!')

            except FileNotFoundError:
                with open(file_name, 'a', encoding='utf-8') as usercredentials:
                    usercredentials.write(credential_website + '@@@' + credential_username + '@@@' + credential_password + '\n')
                    print('Credentials Saved!')

        elif credential_selection == 4:
            file_name = str(login_credentials) + '.txt'
            try:
                with open(file_name, 'r', encoding='utf-8') as usercredentials:
                    for line in usercredentials:
                        a,b,c = line.strip('\n').split('@@@')
                        print('Website: ' + a + '\n' + 'Username: ' + b + '\n' + 'Password: ' + c + '\n')

            except FileNotFoundError:
                print('You have no saved passwords')


if __name__ == '__main__':
    new()
