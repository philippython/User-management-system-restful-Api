from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/evaluator', methods=['POST'])
def evaluator():
    operand = request.json.get('operation_type')
    x = request.json.get('x')
    y = request.json.get('y')
    
    def ans():
        if len(operand) > 15: 
            operation_string = operand.split(" ")
            numbers = []
            for word in operation_string:
                try:
                    numbers.append(int(word))
                except ValueError:
                    pass
            print(numbers)
            if "add" in operation_string: 
                return numbers[0] + numbers[1]
            if "substract" in operation_string:
                return numbers[0] + numbers[1]
            if "multiply" in operation_string: 
                return numbers[0] + numbers[1]
        if operand.lower() == "addition" : return x + y
        if operand.lower() == "substraction" : return x - y
        if operand.lower() == "multiplication" : return x * y


    answer = ans()
    return jsonify({"slackUsername":"OdulajaPhilip", "operation_type":operand.lower(), "result": answer})


if "__main__" == __name__:
    app.debug()
