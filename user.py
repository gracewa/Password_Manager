class User:
    "template for new users"
    user_list=[]
    def __init__(self,username, password):
        '''
        generates a new user
        :param username: new user's username
        :param password: new user's password
        '''
        self.username = username
        self.password = password

    def save_user(self):

            '''
            saves user objects into user_list
            '''

            User.user_list.append(self)