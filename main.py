#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler, PowerTransformer


# In[2]:


# Load the saved model
with open('classifier.pkl', 'rb') as file:
    model = pickle.load(file)


# In[3]:


# Load the dataset that need to be predict
raw_data_url = 'https://github.com/sheenmsn/Credit_Card_Fraud_Detection/raw/main/Data/creditcard_newlist.csv'
df = pd.read_csv(raw_data_url)


# In[4]:


# Check if any duplicate rows exist in the dataframe
df.drop_duplicates(inplace=True)


# In[5]:


# Dropping the column Time as it is not impactful
df = df.drop(['Time'], axis=1)


# In[6]:


# Scaling the feature "Amount" for better result
sc = StandardScaler()
amount = df['Amount'].values

df['Amount'] = sc.fit_transform(amount.reshape(-1, 1))


# In[7]:


# Define predictor variables (X) for the new dataset
X_new = df.drop('true_labels', axis=1)


# In[8]:


# Make predictions using the loaded model
predictions = model.predict(X_new)

# Print or use the predictions as needed
print(predictions)

