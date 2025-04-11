# import pandas as pd
# import numpy as np


# #EXTRACT
# #Load the dataset
# df = pd.read_csv('heart.csv')
# df.head()

# #CLEAN
# #Check for missing values
# print(df.isnull().sum())
# #Check Datatypes
# print(df.dtypes)
# #Basic Stats
# print(df.describe())

# #TRANSFORM
# # Example Transformation: Normalize 'age' and 'chol' columns
# df['age_norm'] = (df['age'] - df['age'].mean()) / df['age'].std()
# df['chol_norm'] = (df['chol'] - df['chol'].mean()) / df['chol'].std()


import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('heart.csv')

# Normalizing numeric features using NumPy
df['age_norm'] = np.round((df['age'] - np.mean(df['age'])) / np.std(df['age']), 2)
df['chol_norm'] = np.round((df['chol'] - np.mean(df['chol'])) / np.std(df['chol']), 2)

# Create a new feature: 'risk_level'
df['risk_level'] = np.where((df['age'] > 50) & (df['chol'] > 240), 'High', 'Normal')

# Encode categorical column 'sex' into 'Male' and 'Female'
df['sex_label'] = df['sex'].apply(lambda x: 'Male' if x == 1 else 'Female')

# Final selected columns for Data Warehouse
final_df = df[['age', 'age_norm', 'chol', 'chol_norm', 'sex_label', 'risk_level', 'target']]

# Preview the transformed data
print(final_df.head())




# Save to a new CSV file
final_df.to_csv('transformed_heart_data.csv', index=False)
