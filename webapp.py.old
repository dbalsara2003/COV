from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from formatfile import csvParse
import os

upload_folder = './uploaded_files'
allowed_extensions = { 'csv':'.csv', 
                      'xml':'.xml'}

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

def allowed_file(filename:str):
    # return '.' in filename and \
    #        filename.rsplit('.', 1)[-1].lower() in allowed_extensions
    ext = filename.rsplit('.', 1)[-1].lower()
    if ext in allowed_extensions:
        if filename.endswith(allowed_extensions[ext]):
            return True

@app.route('/upload_file', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        #checks if the post request has the file
        f = request.files['filename']
        # f.save(f.filename)
        new_dir = os.path.join(os.getcwd(), app.config['upload_folder'])
        if not os.path.exists(new_dir):
            os.makedirs(app.config['upload_folder'])
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['upload_folder'], filename))
            print("File saved")
            print(f)
            dataframe = (csvParse(f))
            print(dataframe)
            #call Ml methods here
            # return redirect(url_for('display', name=filename))
        return redirect(url_for('home'))

def process_data(dataframe):
    print(dataframe)



#this needs to change to port 80 when we deploy on docker
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
