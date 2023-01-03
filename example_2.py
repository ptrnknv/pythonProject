from functools import wraps


class MaxRetriesException(Exception):
    pass


def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except:
                    pass
            raise MaxRetriesException
        return wrapper
    return decorator


@retry(9)
def add(a, b):
    add.calls = add.__dict__.get('calls', 0) + 1
    if add.calls < 10:
        raise ValueError
    return a + b


try:
    print(add(10, 20))
except Exception as e:
    print(type(e))