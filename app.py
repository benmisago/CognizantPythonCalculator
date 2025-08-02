from flask import Flask, render_template, request
import logging

app = Flask(__name__)
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 == 0:
                    error = "You can't divide by zero!"
                else:
                    result = num1 / num2
        except Exception as e:
            error = "Invalid input!"
            logging.error(f"Error: {e}")

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
