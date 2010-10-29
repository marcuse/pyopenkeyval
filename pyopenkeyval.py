import urllib
import urllib2
try:
    import json
except ImportError:
    import simplejson as json

__version__ = '0.1'

class pyopenkeyval(object):
    _api_url = 'http://api.openkeyval.org/%s'

    def __getitem__(self, key):
        try:
            result = urllib2.urlopen(self._api_url % key).read()
            return result
        except urllib2.HTTPError, e:
            if e.code == 404:
                raise(KeyError(key))
            else:
                raise

    def __setitem__(self, key, value):
        self.store(key, value)

    def store(self, key, value):
        data = urllib.urlencode({'data': value})
        result = urllib2.urlopen(self._api_url % key, data).read()
        return json.loads(result)

