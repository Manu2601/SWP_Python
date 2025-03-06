import json
import functools

def jsonify(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result, indent=2, ensure_ascii=False)
    return wrapper