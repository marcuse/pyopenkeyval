"""
A simple interface to OpenKeyval.org

OpenKeyval.org is a service for easily storing and retrieving key/value pairs
via HTTP. pyopenkeyval is a Python interface to this service, presented as a
dict-like object that accesses data on OpenKeyval.

Website: http://github.com/marcuse/pyopenkeyval
"""

import urllib
import urllib2
try:
    import json
except ImportError:
    import simplejson as json

__version__ = '0.1'

class pyopenkeyval(object):
    """A dict-like object that can read and write values to keys stored on OpenKeyval.org"""

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

    def __delitem__(self, key):
        self.store(key, '')

    def store(self, key, value):
        """Stores `value` on `key`, returns a dict of the parsed JSON response."""
        data = urllib.urlencode({'data': value})
        result = urllib2.urlopen(self._api_url % key, data).read()
        return json.loads(result)

