from flask import Flask, render_template, request, redirect, url_for
from formatfile import csvParse
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

@app.route('/upload_file', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['filename']
        csvParse(f)
        return redirect('http://localhost:8080/', code=200)


#this needs to change to port 80 when we deploy on docker
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
