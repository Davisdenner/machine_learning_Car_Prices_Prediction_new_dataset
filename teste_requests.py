import requests

url = "http://127.0.0.1:5000/predict"
headers = {"Content-Type": "application/json"}
data = {
    "fueltype": 1, "doornumber": 4, "aspiration": 1, "drivewheel": 2, "enginelocation": 1, "cylindernumber": 4,
    "wheelbase": 88.6, "carlength": 168.8, "carwidth": 64.1, "carheight": 48.8, "curbweight": 2548,
    "enginesize": 130, "boreratio": 3.47, "stroke": 2.68, "compressionratio": 9.0, "horsepower": 111, "peakrpm": 5000,
    "citympg": 21, "highwaympg": 27,

    #  variáveis categóricas
    "enginetype_dohcv": 0, "enginetype_l": 1, "enginetype_ohc": 0, "enginetype_ohcf": 0, "enginetype_ohcv": 1, "enginetype_rotor": 0,
    "carbody_hardtop": 0, "carbody_hatchback": 0, "carbody_sedan": 1, "carbody_wagon": 0,
    "fuelsystem_2bbl": 1, "fuelsystem_4bbl": 0, "fuelsystem_idi": 0, "fuelsystem_mfi": 0, "fuelsystem_spdi": 0, "fuelsystem_spfi": 0,

    #  marcas dos carros
    "car_brands_audi": 0, "car_brands_bmw": 0, "car_brands_chevrolet": 0, "car_brands_dodge": 0, "car_brands_honda": 1,
    "car_brands_isuzu": 0, "car_brands_jaguar": 0, "car_brands_mazda": 0, "car_brands_mercedes": 0, "car_brands_mitsubishi": 0,
    "car_brands_nissan": 0, "car_brands_peugeot": 0, "car_brands_plymouth": 0, "car_brands_porsche": 0, "car_brands_renault": 0,
    "car_brands_saab": 0, "car_brands_subaru": 0, "car_brands_toyota": 0, "car_brands_volkswagen": 0, "car_brands_volvo": 0,
      "car_brands_buick": 0, "car_brands_mercury":0, "car_brands_alfa-romero": 0

}

response = requests.post(url, json=data, headers=headers)
print(response.json())