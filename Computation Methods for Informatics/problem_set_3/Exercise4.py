from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("problem_set_3/Chronic_Kidney_Dsease_data.csv")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods = ["POST"])
def analyze():
    column_name = request.form["column_name"]
    column_data = df[column_name]
    mean = column_data.mean()
    std = column_data.std()
    result = "The mean for " + column_name + " is " + str(mean) + ", and the standard deviation is " + str(std) + "."
    return render_template("analyze.html", analysis = result, column_name = column_name)

if __name__ == "__main__":
    app.run(debug = True)