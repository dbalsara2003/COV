from flask import Flask, render_template
app = Flask(__name__)

# This is the home page thats in templates folder
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/manual')
def manual():
    return render_template('check_file.html')

@app.route('/check_manual')
def check_manual_page():
    return "This page will be for inputting values for a single row needing to be estimated."

#this needs to change to port 80 when we deploy on docker
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
