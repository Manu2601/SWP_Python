from jsonify import jsonify

@jsonify
def test():
    return {'message': 'Hello, World!'}

print(test())

@jsonify
def test2():
    return [{'message1': 'Hello, World!'}, {'message2': 'Hello, World2!'}]

print(test2())