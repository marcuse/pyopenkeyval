# pyopenkeyval

*[OpenKeyval.org](http://openkeyval.org/)* is a service for easily storing and
retrieving key/value pairs via HTTP. *pyopenkeyval* is a Python interface to
this service, presented as a dict-like object that accesses data on OpenKeyval.

## Example

    from pyopenkeyval import pyopenkeyval
    okv = pyopenkeyval()
    okv['example'] = 'Hello, online key/value storage!'
    print okv['example']

If you need the result from storing a value, use the `store()` method instead:

    result = okv.store('example', 'Hello, online key/value storage!')
    print result['read_only_key']

To delete a key, either set its value to '' or use the `del` keyword:

    del okv['example']

## Requirements

Python 2.5 and lower require *simplejson* to be installed.

