import json

# حفظ المتركس العادية
metrics = {"accuracy": 0.98}
with open('metrics.json', 'w') as f:
    json.dump(metrics, f)

# عمل بيانات للرسم (Plots) عشان الشاشة البيضا تتملي
data = [
    {"loss": 0.5, "epoch": 1},
    {"loss": 0.3, "epoch": 2},
    {"loss": 0.2, "epoch": 3},
    {"loss": 0.1, "epoch": 4}
]
with open('scores.json', 'w') as f:
    json.dump(data, f)

print("Metrics and Scores saved successfully!")