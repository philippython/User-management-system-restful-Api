from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/evaluator', methods=['POST'])
def evaluator():
    operand = request.json.get('operation_type')
    x = request.json.get('x')
    y = request.json.get('y')
    response = {"slackUsername":"OdulajaPhilip"}
    def ans():
        if len(operand) > 15: 
            operation_string = operand.split(" ")
            numbers = []
            for word in operation_string:
                try:
                    numbers.append(int(word))
                except ValueError:
                    pass
            if len(numbers) < 2:
                response.update({"operation_type": operand.lower(), "result": "invalid string input for operation type"})
            elif "add" in operation_string: 
                response.update({"operation_type": "addition", "result":numbers[0] + numbers[1]})
            elif "substract" in operation_string:
                response.update({"operation_type": "substraction", "result":numbers[0] - numbers[1]})
            elif "multiply" in operation_string: 
                response.update({"operation_type": "multiplication", "result":numbers[0] * numbers[1]})
        if operand.lower() == "addition" : response.update({"operation_type": "addition", "result":x + y})
        if operand.lower() == "substraction" : response.update({"operation_type": "substraction", "result":x - y})
        if operand.lower() == "multiplication": response.update({"operation_type": "multiplication", "result":x * y})

    ans()
    return jsonify(response)


if "__main__" == __name__:
    app.debug()
