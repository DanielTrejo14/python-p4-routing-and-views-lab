#!/usr/bin/env python3

from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return make_response('<h1>Python Operations with Flask Routing and Views</h1>', 200)


@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return make_response(parameter, 200)


@app.route('/count/<int:parameter>')
def count(parameter):
    new_str = ''
    for i in range(0, parameter):
        new_str += str(f'{i}\n')
    return make_response(new_str, 200)


@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    new_val = 0
    if(operation == '+'):
        return make_response(str(num1 + num2), 200)
    elif(operation == '-'):
        return make_response(str(num1 - num2), 200)
    elif(operation == '*'):
        return make_response(str(num1 * num2), 200)
    elif(operation == 'div'):
        return make_response(str(num1/num2), 200)
    elif(operation == '%'):
        return make_response(str(num1%num2), 200)
    else:
        return make_response({}, 200)




if __name__ == '__main__':
    app.run(port=5555, debug=True)