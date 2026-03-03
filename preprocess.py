import pandas as pd
import os

# Create data directory if not exists
os.makedirs('data', exist_ok=True)

# Create dummy data
df = pd.DataFrame({'feature': [1, 2, 3], 'target': [0, 1, 0]})
df.to_csv('data/train.csv', index=False)
df.to_csv('data/test.csv', index=False)
print("Data prepared!")