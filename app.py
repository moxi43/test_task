from flask import Flask, render_template, request, redirect
import os
import csv

# Well, I need to get CSV FROM THE USER AND GET THE DATA FROM THE CSV FOR PLOTTING
# the graph with chart.js 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    data = [
        ("01-01-2018", "100"),
        ("01-02-2018", "200"),
        ("01-03-2018", "300"),
        ("01-04-2018", "100"),
        ("01-05-2018", "500"),
        ("01-06-2018", "600"),
        ("01-07-2018", "700"),
    ]
    
    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("graph.html", values=values, labels=labels)

@app.route('/about')
def about():
    return render_template("about.html")
