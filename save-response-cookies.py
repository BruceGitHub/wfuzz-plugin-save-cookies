import sys,os

# Python 2 and 3
if sys.version_info >= (3, 0):
    from urllib.parse import urljoin
else:
    from urlparse import urljoin

from wfuzz.plugin_api.mixins import DiscoveryPluginMixin
from wfuzz.plugin_api.base import BasePlugin
from wfuzz.plugin_api.urlutils import check_content_type
from wfuzz.externals.moduleman.plugin import moduleman_plugin
from pprint import pprint


@moduleman_plugin
class savecookie(BasePlugin, DiscoveryPluginMixin):
    name = "save-response-cookies"
    author = ("Roberto Diana",)
    version = "0.1.0"
    summary = "save the response cookies to file"
    description = ("Each file is the name of request's number.",)
    category = ["default"]
    priority = 99

    parameters = (
    )

    def __init__(self):
        BasePlugin.__init__(self)

    def validate(self, fuzzresult):
        if not os.path.exists('saved-cookies'):
            os.makedirs('saved-cookies')

        return True

    def process(self, fuzzresult):
        new_cookies = list(fuzzresult.history.cookies.response.items())

        if len(new_cookies) > 0:
            for name, value in new_cookies:
                self.add_result("Cookie - %s=%s" % (name, value))
                with open('saved-cookies/request_number_'+str(fuzzresult.nres)+'.txt', 'w') as file:
                    file.write("%s - %s=%s" % (fuzzresult.payload[0],name, value))

