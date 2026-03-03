import json


metrics = {"accuracy": 0.98}

with open('metrics.json', 'w') as f:
    json.dump(metrics, f)

print("Metrics saved as metrics.json!")