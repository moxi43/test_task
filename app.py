from crypt import methods
from flask import Flask, render_template, request, redirect
import os
import csv
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    data = []
    if request.method == 'POST':
        if request.files:
            uploaded_file = request.files['filename'] # This line uses the same variable and worked fine
            filepath = os.path.join(app.config['FILE_UPLOADS'], uploaded_file.filename)
            uploaded_file.save(filepath)
            with open(filepath) as file:
                csv_file = csv.reader(file)
                for row in csv_file:
                    data.append(row)
            return redirect(request.url)
    return render_template('index.html', data=data)


@app.route('/graph', methods=["GET"])
def graph():
    df = pd.read_csv('uploads/table.csv')
    label = list(set(df['code'].tolist())   )
    dates = df['date'].tolist()
    values = [[45, 33, 41], [21, 23, 54], [13, 2, 3]]
    #values = df['pt1'].tolist()

    return render_template('graph.html', label=label, dates=dates, values=values)
    
    

app.config['FILE_UPLOADS'] = "uploads/"