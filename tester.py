from flask import Flask, redirect, render_template, flash, request

app = Flask(__name__)


@app.route('/evaluator', methods=['POST'])
def evaluator():
    operand = request.args.get('operation_type')
    x = request.args.get('x')
    y = request.args.get('y')

    print(operand, x , y)



if "__main__" == __name__:
    app.debug()
