from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)
model = joblib.load(os.path.join('model', 'spam_model.pkl'))

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    if request.method == "POST":
        message = request.form["message"]
        prediction = model.predict([message])[0]
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)




# Congratulations! You have won a cash prize of 5 million rupees! Contact us now at 03XX-XXXXXXX or your prize will be given to someone else!"