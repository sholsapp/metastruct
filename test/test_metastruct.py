from metastruct import Metastruct, underscoreify


def test_underscoreify():
  assert underscoreify('fooBar') == 'foo_bar'
  assert underscoreify('fooBarBaz') == 'foo_bar_baz'


def test_stuff():
  s = Metastruct({
    'a': 'a',
    'b': {
      'a': 'ba',
      'b': 'bb',
      'c': {
        'a': 'bca',
      },
    },
    'c': [1, 2, 3],
    'dA': 'a',
    'e': [1, {'a': 'a'}, 3],
  })
  assert s.a == 'a'
  assert s.b.a == 'ba'
  assert s.b.b == 'bb'
  assert s.b.c.a == 'bca'
  assert s.c == [1, 2, 3]
  assert s.dA == 'a'
  assert s.d_a == 'a'
  assert s.e[0] == 1
  assert s.e[1].a == 'a'
  assert s.e[2] == 3
