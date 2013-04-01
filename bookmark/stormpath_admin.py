from stormpath.client import ClientBuilder
from stormpath.resource import Application, Account, Directory
from stormpath.auth import UsernamePasswordRequest
import sys

class UserInfo(object):
    def __init__(self, username):
        self.username = username;

    def __str__(self):
        return str(self.username)
        
class Admin(object):
    api_key_file = 'bookmark/stormpath_api_key/apiKey.yml'
    client = ClientBuilder().set_api_key_file_location(api_key_file).build()
    tenant = client.current_tenant
    applications = []
    for app in tenant.applications:
        applications.append(app)

    @classmethod
    def app_url(cls,app_name):
        for app in cls.applications:
            if (app.name==app_name):
                return app.href
        return ''

    @classmethod
    def user_signin(cls, username, password, app_name):
        href = cls.app_url(app_name)
        application = cls.client.data_store.get_resource(href, Application)
        request = UsernamePasswordRequest(username, password)
        print (username, " ", password)
        for account in application.accounts:
            print ("last name: ", account.given_name)

        try:
            result = application.authenticate_account(request)
            print (result)
            return UserInfo(username)
        except:
            print ("Unexpected error from application.authenticate_account:", sys.exc_info()[0])
            return None

    @classmethod
    def user_signup(cls, username, password, app_name):
        # hard code directory href for now
        directory_href = 'https://api.stormpath.com/v1/directories/1o0nIXQ6UsMsmFtaUZKWqw'
        directory = cls.client.data_store.get_resource(directory_href, Directory)

        account = cls.client.data_store.instantiate(Account)
        account.given_name = username.split('@')[0]
        account.surname = username.split('@')[0]
        account.username = username
        account.email = username
        account.middle_name = username.split('@')[0]
        account.password = password

        try:
            account = directory.create_account(account)
            return UserInfo(username)
        except:
            print("Unexpected error from directory.create_account:", sys.exc_info()[0])
            return None
        