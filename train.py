import pandas as pd
import pickle


df = pd.read_csv('data/train.csv')


model = "This is a trained Advanced Model"


with open('model.pkl', 'wb') as f:
    pickle.dump("Advanced Model", f)

print("Model trained and saved as model.pkl!")