from flask import Flask, render_template
from api import store_list
import arcgis

app = Flask(__name__)

@app.route('/')
def index():
    Vanmap = arcgis.gis.GIS().map('Vancouver, BC')
    properties = store_list.stores
    return render_template('index.html', properties=properties)


if __name__ == '__main__':
    app.run(debug=True)