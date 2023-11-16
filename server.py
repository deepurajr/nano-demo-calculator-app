from flask import Flask, request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World'

@app.route("/calculator/add", methods=['POST'])
def add():
    if request.form:
        num1 = request.form.get('first')
        num2 = request.form.get('second')
        print(f'{num1} and {num2}')
        return f'Sum of the two numbers = {num1+num2}'
    elif request.json:
        print(f'json data = {request.json}')
        json = request.json
        num1 = json['first']
        num2 = json['second']
        print(f'{num1} and {num2}')
        return f'Sum of the two numbers = {num1+num2}'
    else:
        print(f'received other data types')
    

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    if request.form:
        num1 = request.form.get('first')
        num2 = request.form.get('second')
        print(f'{num1} and {num2}')
        return f'Sum of the two numbers = {num1-num2}'
    elif request.json:
        print(f'json data = {request.json}')
        json = request.json
        num1 = json['first']
        num2 = json['second']
        print(f'{num1} and {num2}')
        return f'Difference of the two numbers = {num1-num2}'
    else:
        print(f'received other data types')

@app.route("/calculator/multiply", methods=['POST'])
def multiply():
    if request.form:
        num1 = request.form.get('first')
        num2 = request.form.get('second')
        print(f'{num1} and {num2}')
        return f'Sum of the two numbers = {num1*num2}'
    elif request.json:
        print(f'json data = {request.json}')
        json = request.json
        num1 = json['first']
        num2 = json['second']
        print(f'{num1} and {num2}')
        return f'Product of the two numbers = {num1*num2}'
    else:
        print(f'received other data types')

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
