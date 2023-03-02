from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from formatfile import csvParse
import os

upload_folder = './uploaded_files'
allowed_extensions = {"'csv', 'xml'"}

app = Flask(__name__)
app.config['upload_folder'] = upload_folder

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

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/upload_file', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        #checks if the post request has the file
        f = request.files['filename']
        # f.save(f.filename)
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['upload_folder'], filename))
            return redirect(url_for('display', name=filename))

        csvParse(f)
        return redirect('http://localhost:8080/', code=200)


#this needs to change to port 80 when we deploy on docker
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
