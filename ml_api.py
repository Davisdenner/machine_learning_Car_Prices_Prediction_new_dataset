from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Carregando o modelo treinado
with open('modelo.pkl', 'rb') as f:
    model = pickle.load(f)

# Definindo as features usadas no treinamento
FEATURES = [
    "fueltype", "doornumber", "aspiration", "drivewheel", "enginelocation", "cylindernumber",
    "wheelbase", "carlength", "carwidth", "carheight", "curbweight",
    "enginesize", "boreratio", "stroke", "compressionratio", "horsepower", "peakrpm",
    "citympg", "highwaympg",

    #  variáveis categóricas
    "enginetype_dohcv", "enginetype_l", "enginetype_ohc", "enginetype_ohcf", "enginetype_ohcv", "enginetype_rotor",
    "carbody_hardtop", "carbody_hatchback", "carbody_sedan", "carbody_wagon",
    "fuelsystem_2bbl", "fuelsystem_4bbl", "fuelsystem_idi", "fuelsystem_mfi", "fuelsystem_spdi", "fuelsystem_spfi",

    #  marcas dos carros
    "car_brands_audi", "car_brands_bmw", "car_brands_chevrolet", "car_brands_dodge", "car_brands_honda",
    "car_brands_isuzu", "car_brands_jaguar", "car_brands_mazda", "car_brands_mercedes", "car_brands_mitsubishi",
    "car_brands_nissan", "car_brands_peugeot", "car_brands_plymouth", "car_brands_porsche", "car_brands_renault",
    "car_brands_saab", "car_brands_subaru", "car_brands_toyota", "car_brands_volkswagen", "car_brands_volvo", 
    "car_brands_buick", "car_brands_mercury", "car_brands_alfa-romero"

]

@app.route('/')
def home():
    return jsonify({"mensagem": "API está rodando!"})

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

   