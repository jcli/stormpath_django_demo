from stormpath.client import ClientBuilder
from stormpath.resource import Application, Account, Directory
from stormpath.auth import UsernamePasswordRequest
import sys

def app_url(applications, app_name):
    for app in applications:
        if (app.name==app_name):
            return app.href
    return ''
    
api_key_file = 'stormpath_api_key/apiKey.yml'
client = ClientBuilder().set_api_key_file_location(api_key_file).build()
tenant = client.current_tenant
applications = []
for app in tenant.applications:
    applications.append(app)

href = app_url(applications, 'bookmark_django')

print (href)
application = client.data_store.get_resource(href, Application)


directory_href = 'https://api.stormpath.com/v1/directories/1o0nIXQ6UsMsmFtaUZKWqw'

directory = client.data_store.get_resource(href, Directory)

account = client.data_store.instantiate(Account)
account.given_name = 'def'
account.surname = 'def'
account.username = 'def'
account.email = 'def@abc.com'
account.middle_name = 'def'
account.password = 'qwerQWER1'

account = directory.create_account(account)


# for account in application.accounts:
#     print ("last name: ", account.given_name)
    
# request = UsernamePasswordRequest('abc', 'qwerQWER1')

# result = application.authenticate_account(request)

# print (result)