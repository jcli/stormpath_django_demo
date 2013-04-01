from stormpath.client import ClientBuilder

class Admin(object):
    api_key_file = 'bookmark/stormpath_api_key/apiKey.yml'
    client = ClientBuilder().set_api_key_file_location(api_key_file).build()
    tenant = client.current_tenant
    applications = tenant.applications     

    @classmethod
    def app_url(cls,app_name):
        for app in cls.applications:
            if (app.name==app_name):
                return app.href
        return ''
