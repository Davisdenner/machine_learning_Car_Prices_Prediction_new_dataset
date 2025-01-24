import requests

url = "http://127.0.0.1:5000"
headers = {"Content-Type": "application/json"}
data = {
    "fueltype": 1, "doornumber": 4, "aspiration": 1, "drivewheel": 2, "enginelocation": 1, "cylindernumber": 4,
    "enginetype_dohcv": 0, "enginetype_l": 1, "enginetype_ohc": 0, "enginetype_ohcf": 0, "enginetype_ohcv": 1, "enginetype_rotor": 0,
    "carbody_hardtop": 0, "carbody_hatchback": 0, "carbody_sedan": 1, "carbody_wagon": 0,
    "fuelsystem_2bbl": 1, "fuelsystem_4bbl": 0, "fuelsystem_idi": 0, "fuelsystem_mfi": 0, "fuelsystem_spdi": 0, "fuelsystem_spfi": 0
}

response = requests.post(url, json=data, headers=headers)
print(response.json())