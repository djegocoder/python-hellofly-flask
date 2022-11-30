import os
import numpy as np
import pandas as pd
import pickle
from flask import Flask, jsonify, redirect, render_template, request, url_for
from pycaret.classification import load_model, predict_model

app = Flask(__name__)

@app.route("/")
def resume():
    return render_template("index.html")

@app.route("/portifolio1")
def portifolio1():
    return render_template("portifolio-1.html")

@app.route("/portifolio2")
def portifolio2():
    return render_template("portifolio-2.html")

@app.route("/portifolio3")
def portifolio3():
    return render_template("portifolio-3.html")

@app.route("/portifolio4")
def portifolio4():
    return render_template("portifolio-4.html")

@app.route("/portifolio5")
def portifolio5():
    return render_template("portifolio-5.html")

@app.route("/portifolio6")
def portifolio6():
    return render_template("portifolio-6.html")

@app.route("/portifolio7")
def portifolio7():
    return render_template("portifolio-7.html")    

@app.route("/portifolio8")
def portifolio8():
    return render_template("portifolio-8.html")

@app.route("/portifolio9")
def portifolio9():
    return render_template("portifolio-9.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5001))
    app.run(debug=True, host='0.0.0.0', port=port)
