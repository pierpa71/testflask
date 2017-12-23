# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""
from flask import Flask, render_template  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    """Say hello"""
    return 'Hello, world!'

@app.route('/pierpa')   # URL '/' to be handled by main() route handler
def pierpa():
    """Say hello Pierpa"""
    return render_template('hello.html')

if __name__ == '__main__':  # Script executed directly?
    app.run()  # Launch built-in web server and run this Flask webapp
