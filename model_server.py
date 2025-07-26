from flask import Flask, request
from preprocessing_utils import *
from keras.models import load_model

app = Flask(__name__)
model = load_model('models/CONV-914.keras')

@app.route('/', methods=['GET'])
def home():
    return 'Hello!'

@app.route('/data', methods=['POST'])
def receive_data():
    raw_data = request.json.get('trace') # type: ignore
    print("Data received.")
    processed_input = process_raw_data(raw_data)
    prediction = model.predict(processed_input) # type: ignore
    
    return {'status': 'OK', 'prediction':str(prediction[0][0])}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)