import os
import json
from datetime import datetime


def log_decorator_to(log_to=None):
    def wrapper(func):
        def wrapped_func(*args, **kwargs):
            log_file = log_to
            func_name = func.__name__
            args_str = json.dumps(args)
            kwargs_str = json.dumps(kwargs)
            return_val = func(*args, **kwargs)
            line = ':'.join(
                [datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
                 'name = {}'.format(func_name), 'args = {}'.format(args_str),
                 'kwargs = {}'.format(kwargs_str), 'return = {}'.format(str(return_val))]
            )
            if not log_file:
                log_file = os.path.join(os.path.abspath('.'),
                                        '.'.join([func_name, 'txt']))
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write(line)
        return wrapped_func
    return wrapper

