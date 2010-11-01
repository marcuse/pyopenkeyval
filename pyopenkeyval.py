"""
A simple interface to OpenKeyval.org

OpenKeyval.org is a service for easily storing and retrieving key/value pairs
via HTTP. pyopenkeyval is a Python interface to this service, presented as a
dict-like object that accesses data on OpenKeyval.

Website: http://github.com/marcuse/pyopenkeyval
"""

import time
import urllib
import urllib2
try:
    import json
except ImportError:
    import simplejson as json

__version__ = '0.2'

class pyopenkeyval(object):
    """A dict-like object that can read and write values to keys stored on OpenKeyval.org"""

    _api_url = 'http://api.openkeyval.org/%s'
    _cache_time = None
    _cache = {}

    def __init__(self, cache_time=None):
        """Construct a new pyopenkeyval object.

        Keyword arguments:
        cache_time -- number of seconds to cache fetched values (default None)"""
        self._cache_time = cache_time

    def __getitem__(self, key):
        self._expire_cache()
        if self._cache_time:
            if self._cache.has_key(key):
                return self._cache[key][0]
        try:
            result = urllib2.urlopen(self._api_url % key).read()
            self._update_cache(key, result)
            return result
        except urllib2.HTTPError, e:
            if e.code == 404:
                raise(KeyError(key))
            else:
                raise

    def __setitem__(self, key, value):
        self._expire_cache()
        if self._cache_time:
            if self._cache.has_key(key):
                del self._cache[key]
        self.store(key, value)

    def __delitem__(self, key):
        self.store(key, '')

    def store(self, key, value):
        """Stores `value` on `key`, returns a dict of the parsed JSON response."""
        data = urllib.urlencode({'data': value})
        result = urllib2.urlopen(self._api_url % key, data).read()
        return json.loads(result)

    def clear_cache(self):
        """Removes all cached values regardless of expiration time."""
        self._cache = {}

    def _update_cache(self, key, value):
        if self._cache_time:
            self._cache[key] = (value, time.time())

    def _expire_cache(self):
        if self._cache_time:
            now = time.time()
            for key in self._cache.keys():
                if now - self._cache[key][1] > self._cache_time:
                    del self._cache[key]
