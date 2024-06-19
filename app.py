from flask import Flask, render_template, request,url_for
from functions import (load_model, predict_spam, load_credit_model, predict_credit)
from passfunc import (load_pass_model, predict_password_strength, extract_features)  

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("ecommerce.html", spam_prediction=None, error=None)


@app.route("/features")
def features():
    return render_template("features.html", spam_prediction=None, error=None)


@app.route("/teams")
def teams():
    return render_template("team.html", spam_prediction=None, error=None)


@app.route("/creditcard")
def creditcard():
    return render_template("creditcard.html", spam_prediction=None, error=None)


@app.route("/credit_predict", methods=["POST"])
def credit_predict():
    if request.method == "POST":
        card_content = request.form["card_content"]
        try:
            credit_prediction = predict_credit(card_content, load_credit_model())  # Load model once
            return render_template("creditcard.html", credit_prediction=credit_prediction, error=None)
        except Exception as e:
            return render_template("creditcard.html", credit_prediction=None, error=str(e))


@app.route("/email")
def email():
    return render_template("emailspam.html", spam_prediction=None, error=None)


@app.route("/emailpredict", methods=["POST"])
def predict():
    if request.method == "POST":
        email_content = request.form["email_content"]
        try:
            model, vectorizer = load_model()
            prediction = predict_spam(email_content, model, vectorizer)
            return render_template("emailspam.html", spam_prediction=prediction, error=None)
        except Exception as e:
            return render_template("emailspam.html", spam_prediction=None, error=str(e))


@app.route("/password")
def password():
    return render_template("password.html")




@app.route("/password_predict", methods=['GET','POST'])
def password_predict():
    if request.method == "POST":
        exampleInputPassword1 = request.form["password"]
        
        pass_model = load_pass_model()
        prediction = predict_password_strength(exampleInputPassword1, pass_model)
        return render_template("password.html", strength=prediction)
    else:
        return render_template("password.html", strength="")


if __name__ == "__main__":
    app.run(debug=True)
