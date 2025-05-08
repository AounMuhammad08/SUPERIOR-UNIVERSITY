# Spam Message Detector

This is a Flask web app that uses NLP to detect whether a message is spam or not.

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Train the model:
```bash
python model/train_model.py
```

4. Run the app:
```bash
python run.py
```

Then go to `http://127.0.0.1:5000` in your browser.
