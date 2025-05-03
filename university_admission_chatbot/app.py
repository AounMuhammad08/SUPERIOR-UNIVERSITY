from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = get_bot_response(user_input)
    return jsonify({"response": response})

def get_bot_response(message):
    message = message.lower()
    if "admission" in message:
        return "We offer admissions twice a year. Would you like to know about the requirements?"
    elif "requirements" in message:
        return "You'll need transcripts, an entrance test, and a completed application form."
    elif "deadline" in message:
        return "The deadline for Fall intake is July 15th."
    elif "contact" in message:
        return "You can contact the admission office at admissions@university.edu."
    else:
        return "I'm here to help with admissions. Could you please ask something related to that?"

if __name__ == "__main__":
    app.run(debug=True)
