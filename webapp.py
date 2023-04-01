from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import pandas as pd
# from formatfile import csvParse
import os
from scripts.ml2 import machine_learning
from io import StringIO
import threading as th

upload_folder = './uploaded_files'
allowed_extensions = {'csv', 'xml'}

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
        f = request.files['file']
        filename = secure_filename(f.filename)

        if f and allowed_file(filename):
            file = request.files.get('file')
            cols = ["OID_"," id", "floor_area_sf", "civic_number"]
            df = pd.read_csv(file, usecols=cols)
            # model_thread = th.Thread(target=run_ml, args=(df,filename,))
            # model_thread.start()
            # model_thread.join()
            new_df = machine_learning(df)
            filename = f'estimated-{filename}'
            return redirect(url_for("download_csv", df=new_df, filename=filename))
        return redirect(url_for("manual"))
    
# @app.route('/model')
def run_ml(df, filename):
    with app.app_context():
        new_df = machine_learning(df)


@app.route('/download')
def download_page():
    return render_template('download.html')

@app.route('/download/<filename>')
def download_csv(df, filename):
    # convert the dataframe to a CSV file and save it to disk
    attachment_name = f'estimated-{filename}'
    dummy_file = StringIO()
    df.to_csv(dummy_file, index=False)
    # return the CSV file to the browser
    return send_file(dummy_file, attachment_filename=attachment_name, as_attachment=True)

@app.route('/loader')
def loader():
    return render_template('loading.html')

#this needs to change to port 80 when we deploy on docker
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
