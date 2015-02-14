import re


def underscoreify(attr):
  """Return a camel case attr's name with underscores.

  Sometime it's obstructive to have camel case attributes in a project that
  otherwise uses underscores. This is a helper to translate camel case
  attribute names to their underscore using equivalent.

  :param attr: The came case attribute to convert.

  """
  def replacer(match):
    return '{first}_{second}'.format(
      first=match.group('first'),
      second=match.group('second').lower())
  return re.sub('((?P<first>[a-z])(?P<second>[A-Z]))', replacer, attr)


def set_attributes(obj, key, value):
  """Set all attributes on `obj` for the key.

  This is more complicated that just calling `setattr` because we also want to
  normalize camel case strings for non-class names.

  This method takes the same arguments as :func:`setattr`.

  """
  if not key:
    raise ValueError('Attribute key cannot be None.')
  setattr(obj, key, value)
  if key[0].islower():
    setattr(obj, underscoreify(key), value)


def Metastruct(d):
  """Convert a :class:`dict` to an object.

  Recursively convert a :class:`dict` into an object with attributes matching
  the keys of the original :class:`dict`.

  :param d: The :class:`dict` to convert.

  """
  top = type('MetastructElement', (object,), d)
  seqs = tuple, list, set, frozenset
  for key, value in d.items():
    # If a `dict`, create another Metastruct
    if isinstance(value, dict):
      set_attributes(top, key, Metastruct(value))
    # If a `seqs`, process each item
    elif isinstance(value, seqs):
      seq = []
      for sub_value in value:
        if isinstance(sub_value, dict):
          seq.append(Metastruct(sub_value))
        else:
          seq.append(sub_value)
      set_attributes(top, key, type(value)(seq))
    # Else it is just a simple attribute
    else:
      set_attributes(top, key, value)
  return top
