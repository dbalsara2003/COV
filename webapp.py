from flask import Flask, render_template, request, flash, Response, redirect, url_for
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
import io
import chardet
import tensorflow as tf
import pandas as pd
import numpy as np
from datetime import date
from io import StringIO, BytesIO
from scripts.ml2 import machine_learning

app = Flask(__name__)
app.config["SECRET_KEY"] = "test"
allowed_extensions = {'csv', 'xml'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/')
def index():
    return render_template('upload_file.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        if f and allowed_file(filename):
            # cols = ["OID_"," id", "floor_area_sf", "civic_number"]
            # df = pd.read_csv(f, usecols=cols)
            df = pd.read_csv(f)
            new_df = machine_learning(df)

            # Return the predicted data as a downloadable CSV file
            download_file = StringIO()
            new_df.to_csv(download_file, index=False)
            download_file.seek(0)

            date_str = date.today().strftime("%d/%m/%Y")
            new_name = f'estimated-{filename}-{date_str}.csv'

            # res = Response(download_file, mimetype='text/csv', headers={"Content-disposition":f"attachment; filename={new_name}"})
            # return res
            app.config['df'] = new_df
            app.config['name'] = new_name
            return redirect(url_for('download_file'))

    return render_template('upload_file.html')

@app.route('/download', methods = ['GET', 'POST'])
def download_file():
    df = app.config['df']
    new_name = app.config['name']
    if request.method == 'POST':
        download_file = StringIO()
        df.to_csv(download_file, index=False)
        download_file.seek(0)

        return Response(download_file, mimetype='text/csv', headers={"Content-disposition":f"attachment; filename={new_name}"})
    
    return render_template('download_page.html', df=df.to_html(), filename=new_name)

# @app.route('/download_page')
# def download_page(res):
#     return render_template('download_page.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
