# metastruct

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
>>> attrgetter('product.name')(s)
'foo'
>>> attrgetter('quantity')(s)
10
```
