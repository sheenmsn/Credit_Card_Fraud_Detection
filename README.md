# FindDefault (Prediction of Credit Card fraud)

## Overview

This project aims to develop a machine-learning model for detecting fraud in credit card transactions. A dataset containing a range of credit card transaction characteristics, such as the number of transactions, time, and further relevant information is used to train this model.

## Problem Statement:
A credit card is one of the most used financial products to make online purchases and payments. Though Credit cards can be a convenient way to manage your finances, they can also be risky. Credit card fraud is the unauthorized use of someone else's credit card or credit card information to make purchases or withdraw cash.

Credit card companies must be able to recognize fraudulent credit card transactions so that customers are not charged for items that they did not purchase.

## Introduction:
The dataset contains transactions made by credit cards in September 2013 by European cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds (473 after removing duplicate rows) out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) accounts for 0.172% of all transactions.

## Project Structure

- **main.py** : Python script that contains the code for data preprocessing, model training, evaluation, and saving of trained models.

- **requirements.txt** : File containing all dependencies needed to run this project.

- **README.md** : A file with an overview of the project, instructions, and other pertinent information

## Getting Started

### Clone the Repository

Clone the repository from GitHub:

_git clone https://github.com/sheenmsn/Credit_Card_Fraud_Detection.git_           

### Install Dependencies

Navigate to the project directory and install the required packages:

_cd Credit_Card_Fraud_Detection_

_pip install -r requirements.txt_

### Execution

Ensure that the credit card transaction data is stored in a CSV file called creditcard.csv, which you put into your project directory.

Run the main Python script:

_python main.py_

_%run C:/Users/user/Desktop/Project_Submit/main.py_ (if you saved the main.py file in your local disc. Replace the file path to where you stored the file)

This script will load the data, preprocess it, train multiple machine learning models (Logistic Regression, Random Forest, AdaBoost, and CatBoost), evaluate their performance using the ROC AUC score, and print the best model and corresponding score. To process data, train models and evaluate performance, follow the prompts in this script.

# Description of Design Choices

## 1. Data Preprocessing

- **Handled missing values**: Checked for missing data and deleted duplicate rows. No missing values have been found, and a total of 1081 duplicate rows have been deleted.

- **Data Imbalance Treatment**: To visualize and address the imbalance of classes, used the oversampling technique SMOTE.

- **Skewness Correction**: To correct the skewness in the dataset of the data set, used PowerTransformer.

- **Feature Engineering**: Created new features such as Hour from the Time feature to enhance the model performance.

## 2.Model Selection and Hyperparameter Tuning:

- Used various classification algorithms such as Logistic Regression, Random Forest, AdaBoost, and CatBoost have been used. 

- To improve the model's performance, GridSearchCV was used for hyperparameter adjustment.

## 3.Performance Evaluation of the Model

- Evaluated models using key metrics such as accuracy, precision, recall, F1 score, and ROC AUC score.

### Model Performance

- **Logistic Regression** : Obtained a ROC AUC score of 94.19% after hyperparameter tuning.

- **Random Forest Classifier**: Obtained an ROC AUC score of 91.53% after hyperparameter tuning.

- **AdaBoost Classifier**: Obtained an ROC AUC score of 92.79% after hyperparameter tuning.

- **CatBoost Classifier**: Obtained an ROC AUC score of 97.61% after hyperparameter tuning.

The CatBoost Classifier Obtained the highest ROC AUC score of 97.61% among all models. Hence, the CatBoost Classifier is selected as the best model for credit card fraud detection.

## Discussion of Future Work

### Potential Improvements

- **Feature Engineering**: Additional exploration of feature engineering techniques to enhance model performance.

- **Advanced Algorithms**: Exploring advanced algorithms like XGBoost, LightGBM, or neural networks. 

- **Real-time Monitoring**: Implementation of the model into a real-time monitoring system for timely detection of fraudulent transactions.

- **Regular Model Updates**: Periodic re-training of the model with new data to adjust to changing fraud patterns.

### Benefits for the Company

- **Cost Savings**: This model helps to prevent the financial losses incurred due to fraud. The financial losses may be as a result of compensations to customers as a result of unauthorized transactions and the legal and administrative penalties that may related due to fraud cases. Generally, it reduces the overall financial liabilities associated with fraud, hence cost reduction.

- **Enhanced Customer Trust**: Fraud detection must be effective in order to increase customer confidence in the services provided by the company. In this way, customers will be assured of the security of their transactions and satisfaction with the company is going to increase. In order to increase its market position, the company will therefore be able to attract even more customers or keep existing ones.

- **Reduced Operational Risks**: Any fraudulent activities not only compromise the company’s financial stability but also create operational risks. They can manifest through reputational damage, increased prosecutor and legislative scrutiny, and the disruption of operations. The company can reduce these risks and ensure operational sustainability through the establishment of an effective fraud-detecting model.

- **Scalability and Adaptability**: Consideration should also be given to increasing and adapting to the evolving needs and business environment of the company. The model should be revised and improved as the amount of transactions grows in order to perform more efficiently or as new patterns of fraud arise. It means that fraud risks can be managed at any time when the company is growing or slowing down.

 
