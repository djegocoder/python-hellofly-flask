import os
from flask import Flask, render_template,request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'diegotadsil'
app.config['MAIL_PASSWORD'] = 'iucllhycwtqvcqfv'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_SUPPRESS_SEND'] = False
mail = Mail(app)


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

@app.route("/email",methods=['GET','POST'])
def index():
    formulario = [x for x in request.form.values()]
    nome = formulario[0]
    email = formulario[1]
    assunto = formulario[2]
    menssagem = formulario[3]
    msg = Message(subject='Portifólio: '+assunto, sender = email, recipients = ['diegotadsil@gmail.com'])
    msg.body = 'Enviado por: '+nome+'\nE-mail: '+email+'\n\n'+menssagem
    mail.send(msg)
    return "OK"


    app.logger.debug(message.subject)



if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True, host='0.0.0.0', port=port)
