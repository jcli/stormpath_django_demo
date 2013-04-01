from stormpath.client import ClientBuilder
from stormpath.resource import Application
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
for account in application.accounts:
    print ("last name: ", account.given_name)
    
request = UsernamePasswordRequest('def', 'qwerQWER1')

result = application.authenticate_account(request)

print (result)
