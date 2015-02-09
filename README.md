# metastruct

[![Latest Version](https://pypip.in/version/metastruct/badge.svg?style=flat)](https://pypi.python.org/pypi/metastruct/)
[![Travis](https://secure.travis-ci.org/sholsapp/metastruct.png?branch=master)](https://travis-ci.org/sholsapp/metastruct)

This library, simply, translates Python dictionary objects into first-class
Python objects whose attributes match that of the original Python dictionaty
object.

This library can be used to clean up code that would otherwise be riddled with
messy string-based dictionary lookups. This library also lends itself to the
use of `operators.attrgetter`, which can be used to further clean up and
simplify code bases.

```python
>>> from metastruct import Metastruct
>>> from operator import attrgetter
>>> s = Metastruct({'product': {'name': 'foo', 'type': 'foo_type'}, 'quantity': 10})
>>> s.product.name
'foo'
>>> s.quantity
10
>>> attrgetter('product.name')(s)
'foo'
>>> attrgetter('quantity')(s)
10
```

## todo

- Implement code to allow camelcase or underscore notation when accessing
  attributes on the class.

- Implement code to dump a metastruct.Metastruct class back to JSON.

