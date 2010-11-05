# pyopenkeyval

*[OpenKeyval.org](http://openkeyval.org/)* is a service for easily storing and
retrieving key/value pairs via HTTP. *pyopenkeyval* is a Python interface to
this service, presented as a dict-like object that accesses data on OpenKeyval.

## Examples

### Normal usage

    from pyopenkeyval import pyopenkeyval
    okv = pyopenkeyval()
    okv['example'] = 'Hello, online key/value storage!'
    print okv['example']

If you need the result from storing a value, use the `store()` method instead:

    result = okv.store('example', 'Hello, online key/value storage!')
    print result['read_only_key']

To check if a key has a value, use the `in` keyword. Note that this will also
cache the value if caching is activated.

    if 'example' in okv:
         ...

### Deleting keys
To delete a key, either set its value to '' or use the `del` keyword:

    del okv['example']

### Caching

If you want to cache retrieved values locally, set the `cache_time` argument
when constructing the `pyopenkeyval` object. This specifies the number of
seconds to cache individual values.

    okv = pyopenkeyval(cache_time=60)

To clear the cache completely at any time, call the `clear_cache()` method.

## Requirements

Python 2.5 and lower require *simplejson* to be installed.

