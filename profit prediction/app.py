from flask import *
import pickle as pk
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pk.load(open('multiple_linear_regression.pkl', 'rb'))

@app.route("/")
def main():
    return render_template("font_page.html")


@app.route("/font_page", methods=["POST"])
def fun():
    area = request.form["city"]
    if area == "Dhaka":
        dhaka = 1
        ctg = 0
        rangpur = 0

    elif area == "CTG":
        dhaka = 0
        ctg = 1
        rangpur = 0

    else:
        dhaka = 0
        ctg = 0
        rangpur = 1

    Mcost = request.form['mcost']
    Acost = request.form['acost']
    Tcost = request.form["tcost"]

    value = pd.DataFrame([[Mcost,Acost,Tcost,dhaka,rangpur]])
    pred = float (abs(model.predict(value)))
    result = round(pred,2)
    return render_template("font_page.html",boss="Price : {} lack".format(result))

app.run(debug=True)
