from flask import Flask
app = Flask(__name__)

@app.route('/home')
def hello():
    return 'Welcome to the Measurement Tool Page.'

@app.route('/check_file')
def check_file_page():
    return "This page will be for inputting a file with multiple rows of estimates needed."

@app.route('/check_manual')
def check_manual_page():
    return "This page will be for inputting values for a single row needing to be estimated."


if __name__ == '__main__':
    app.run(port=8080)
