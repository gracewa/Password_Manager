from user import User
import random
import string


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
            existing_account = str(input("Do you already have a " + credential_website + " account? Y/N: "))
            if existing_account == 'Y' or existing_account == 'y':
                credential_username = str(input("Please enter your " + credential_website + " user name: "))
                credential_password = str(input("Please enter the password here: "))
            elif existing_account == 'N' or existing_account == 'n':
                credential_username = str(input("Please enter a username for your new " + credential_website + " account: "))
                generated_password = str(input("Would you like Password Manager to generate a password for you? Y/N: " ))

                if generated_password == 'Y' or generated_password =='y':
                    random_string = string.ascii_letters + string.digits
                    credential_password = ''.join((random.choice(random_string) for i in range(8)))
                    print("Your new " + credential_website + " password is: ", credential_password)
                elif generated_password == 'N' or generated_password =='n':
                    credential_password = str(input("Please enter your " + credential_website+ " password here: "))
                else:
                    print('Invalid Entry')
            else:
                print('Invalid Entry')

            file_name = str(login_credentials) + '.txt'
            try:
                with open(file_name, 'a', encoding='utf-8') as usercredentials:
                    usercredentials.write(credential_website + '@@@' + credential_username + '@@@' + credential_password + '\n')
                    print('Your Credentials Have Been Saved!')
                    print('Website: ' + credential_website + '\n' + 'User Name: ' + credential_username + '\n' + "Password: " + credential_password + '\n' )

            except FileNotFoundError:
                with open(file_name, 'a', encoding='utf-8') as usercredentials:
                    print('Your Credentials Have Been Saved!')
                    usercredentials.write(credential_website + '@@@' + credential_username + '@@@' + credential_password + '\n')

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
