from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Carregar o modelo treinado
with open('modelo.pkl', 'rb') as f:
    model = pickle.load(f)

# Definir as features usadas no treinamento
FEATURES = [
    'fueltype', 'doornumber', 'aspiration', 'drivewheel', 'enginelocation', 'cylindernumber',
    'enginetype_dohcv', 'enginetype_l', 'enginetype_ohc', 'enginetype_ohcf', 'enginetype_ohcv',
    'enginetype_rotor', 'carbody_hardtop', 'carbody_hatchback', 'carbody_sedan', 
    'carbody_wagon', 'fuelsystem_2bbl', 'fuelsystem_4bbl', 'fuelsystem_idi', 
    'fuelsystem_mfi', 'fuelsystem_spdi', 'fuelsystem_spfi'
]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array([data[feature] for feature in FEATURES]).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "API funcionando!"})

if __name__ == '__main__':
    app.run(debug=True)