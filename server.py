from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    if request.form:
        # print(f'Inside form request')
        num1 = request.form.get('first')
        num2 = request.form.get('second')
        # print(f'{num1} and {num2}')
        ans = int(num1)+int(num2)
        str = {"result": ans}
        return jsonify(str)
    elif request.json:
        # print(f'json data = {request.json}')
        json = request.json
        num1 = json['first']
        num2 = json['second']
        # print(f'{num1} and {num2}')
        ans = int(num1)+int(num2)
        str = {"result": ans}
        return jsonify(str)
    else:
        print(f'received other data types')
    # return f'response: bad request'
    

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    if request.form:
        # print(f'Inside form request')
        num1 = request.form.get('first')
        num2 = request.form.get('second')
        ans = int(num1)-int(num2)
        str = {"result": ans}
        return jsonify(str)
    elif request.json:
        # print(f'json data = {request.json}')
        json = request.json
        num1 = json['first']
        num2 = json['second']
        ans = int(num1)-int(num2)
        str = {"result": ans}
        return jsonify(str)
    else:
        print(f'received other data types')
    # return f'response: bad request'

# @app.route("/calculator/multiply", methods=['POST'])
# def multiply():
#     if request.form:
#         # print(f'Inside request')
#         num1 = request.form.get('first')
#         num2 = request.form.get('second')
#         # print(f'{num1} and {num2}')
#         ans = int(num1)*int(num2)
#         str = {"result": ans}
#         return jsonify(str)
#     elif request.json:
#         # print(f'json data = {request.json}')
#         json = request.json
#         num1 = json['first']
#         num2 = json['second']
#         ans = int(num1)*int(num2)
#         str = {"response": ans}
#         return jsonify(str)
#     else:
#         print(f'received other data types')
#     return f'response: bad request'

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
