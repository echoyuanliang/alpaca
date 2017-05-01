# coding: utf-8

"""
  __author__ = allen

"""

import numbers
import datetime

def bytes2human(bytes, suffix='B'):
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(bytes) < 1024:
            return '%3.2f%s%s' %(bytes, unit, suffix)

        bytes /= 1024.0

    return "%.1f%s%s" % (bytes, 'Yi', suffix)

def _obj2dict(obj, methods, override, ignore):
    res = dict()
    my_ignore = ignore.get(type(obj), []) if ignore else []
    my_override = override.get(type(obj), {}) if override else {}

    for key in dir(obj):
        if key.startswith('_'):
            continue
        if key in my_ignore:
            continue

        try:
            if callable(getattr(obj, key)) and methods:
                val = getattr(obj, key)()
            else:
                val = getattr(obj, key)
        except Exception:
            continue

        if key in my_override:
            res[key] = my_override[key](val)
        else:
            res[key] = obj2dict(val, methods, override, ignore)

    return res

def obj2dict(obj, methods=False, override=None, ignore=None):
    simple_types = (basestring, numbers.Number)
    if obj is None:
        return None
    if isinstance(obj, simple_types):
        return obj
    elif isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    elif isinstance(obj, dict):
        for key, val in obj.items():
                obj[key] = obj2dict(val, methods, override, ignore)
        return obj
    elif type(obj) in (list, tuple):
       item_list = []
       for item in obj:
           item_list.append(obj2dict(item, methods, override, ignore))
       return item_list
    else:
        return _obj2dict(obj, methods, override, ignore)

