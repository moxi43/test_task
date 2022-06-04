from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath
import pandas as pd

# Well, I need to get CSV FROM THE USER AND GET THE DATA FROM THE CSV FOR PLOTTING
# the graph with chart.js 

app = Flask(__name__)

#enable the DEBUG mode
app.config['DEBUG'] = True

#upload folder
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# root URl
@app.route('/')
def index():
    return render_template('request.html')

# get the uploaded files
@app.route('/', methods=['POST'])
def uploadFiles():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        # set the file path
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        # save the file
        uploaded_file.save(file_path)
        parseCSV(file_path)
    
    return redirect(url_for('request'))

def parseCSV(filePath):
    # Column names
    col_names = "label", "date", "pt1", "pt2", "pt3", "pt4"
    # parse using pandas
    csvData = pd.read_csv(filePath, names=col_names, header=None)
    
    for i, row in csvData.iterrows():
        print(i , row["label"], row["date"], row["pt1"], row["pt2"], row["pt3"], row["pt4"])