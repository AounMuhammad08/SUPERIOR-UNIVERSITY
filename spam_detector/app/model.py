import joblib
import os

# Load model
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'spam_model.pkl')
model = joblib.load(model_path)

def predict_spam(text):
    prediction = model.predict([text])[0]
    return 'Spam' if prediction == 1 else 'Not Spam'
