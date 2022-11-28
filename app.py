import json
import os

import pandas as pd
import pickle
from flask import Flask, jsonify, redirect, render_template, request, url_for
from pycaret.classification import *

app = Flask(__name__)


modelo = load_model('static/assets/models/my_best_pipeline')
colunas = ['ITEM_ID','ALTURA','CAPACIDADE_(L)','COMPOSICAO','COR','FORMATO','LARGURA','MARCA',
'PARA_LAVA_LOUCAS','PARA_MICRO_ONDAS','PESO','PROFUNDIDADE','TEMPO_GARANTIA','TEM_FERRO_FUNDIDO','TEM_GRELHA',
    'TEM_TAMPA','TIPO_PRODUTO','TIPO_WOK','SESSION_ID','ITEM_PRICE']

@app.route("/teste")
def teste():
    return render_template("teste.html")


@app.route("/teste2",methods=['POST'])
def teste2():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = colunas)
    prediction = predict_model(modelo, data=data_unseen, round = 0)
    prediction = prediction.Label[0]
    if prediction == 1.0:
        prediction = 'Interessante'
    else:
        prediction = 'Não interessante'
    return render_template("teste.html",pred=f'Esse perfil foi classificado como {prediction}')


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
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True, host='0.0.0.0', port=port)
