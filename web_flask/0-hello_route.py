from flask import Flask
"""A script that starts flask web application"""


app = Flask(__name__, strict_slashes=False)
"""Sets strict slash verification to false"""

@app.route('/')
def home():
    """
    Describes the home page message
    Return: greeting
    """
    return "Hello HBNB!"
if __name__ = '__main__':
    app.run(host='0.0.0.0', port=5000)
