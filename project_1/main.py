from flask import *
import pickle as pk
import numpy as np

app = Flask(__name__)
model = pk.load(open('linear_regession.pkl', 'rb'))


@app.route('/')
def house():
    return render_template('index.html')


@app.route("/index", methods=["POST"])
def func():
    value = int(request.form['area'])

    arr = np.array([[value]])
    pre = int(model.predict(arr))
    return render_template("index.html",boss="Price : {} tk".format(pre))


app.run(debug=True)
