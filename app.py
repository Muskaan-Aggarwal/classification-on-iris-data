from flask import Flask, request, jsonify, send_from_directory  # Add send_from_directory here
import joblib
import numpy as np
import os

app = Flask(__name__, static_folder='public', static_url_path='')

# Load the saved Iris classification model
model = joblib.load('iris_model.pkl')

@app.route('/', methods=['GET'])
def home():
    return send_from_directory('public', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Extract features from request
    features = [data['sepalLength'], data['sepalWidth'], data['petalLength'], data['petalWidth']]
    prediction = model.predict([np.array(features)])

    # Map prediction to Iris species name
    species = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    result = species[prediction[0]]

    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
