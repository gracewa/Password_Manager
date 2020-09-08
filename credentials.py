class Credential:
    "template for saving new credentials"
    credential_list=[]
    def __init__(self,username, password, website):
        '''
        saves user's credentials
        :param username: user's username
        :param password: user's password
        :param website: website that the credentials apply to
        '''
        self.username = username
        self.password = password
        self.website = website
