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

@app.route("/portfolio1")
def portfolio1():
    return render_template("portfolio-1.html")

@app.route("/portfolio2")
def portfolio2():
    return render_template("portfolio-2.html")

@app.route("/portfolio3")
def portfolio3():
    return render_template("portfolio-3.html")

@app.route("/portfolio4")
def portfolio4():
    return render_template("portfolio-4.html")

@app.route("/portfolio5")
def portfolio5():
    return render_template("portfolio-5.html")

@app.route("/portfolio6")
def portfolio6():
    return render_template("portfolio-6.html")

@app.route("/portfolio7")
def portfolio7():
    return render_template("portfolio-7.html")    

@app.route("/portfolio8")
def portfolio8():
    return render_template("portfolio-8.html")

@app.route("/portfolio9")
def portfolio9():
    return render_template("portfolio-9.html")

@app.route("/portfolio10")
def portfolio10():
    return render_template("portfolio-10.html")

@app.route("/portfolio11")
def portfolio11():
    return render_template("portfolio-11.html")

@app.route("/portfolio12")
def portfolio12():
    return render_template("portfolio-12.html")

@app.route("/portfolio13")
def portfolio13():
    return render_template("portfolio-13.html")

@app.route("/portfolio14")
def portfolio14():
    return render_template("portfolio-14.html")

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
