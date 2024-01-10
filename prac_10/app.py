from flask import Flask

app = Flask(__name__)


# home page
@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


# /greet/
# greets whatever is after the /
@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


# /f/
# converts celsius to fahrenheit after the /
@app.route('/f')
@app.route('/f/<user_input_value>')
def celsius_fahrenheit(user_input_value=""):
    """Convert celsius to fahrenheit"""
    answer = float(user_input_value) * 9.0 / 5 + 32
    return f"{user_input_value} degree celsius is {answer} fahrenheit"


if __name__ == '__main__':
    app.run()
