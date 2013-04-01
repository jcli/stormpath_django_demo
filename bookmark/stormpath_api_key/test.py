from stormpath.client import ClientBuilder
from stormpath.resource import Application
from stormpath.auth import UsernamePasswordRequest
from stormpath.client import ApiKey, Client
import httplib2

api_key_file = 'apiKey.yml'
client = ClientBuilder().set_api_key_file_location(api_key_file).build()
tenant = client.current_tenant

print (tenant)
