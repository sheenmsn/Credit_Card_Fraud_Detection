# FindDefault (Prediction of Credit Card fraud)

## Overview

This project aims to develop a machine-learning model for the detection of fraud in credit card transactions. A dataset containing a range of credit card transaction characteristics, such as the number of transactions, time, and further relevant information is used to train this model.

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

Ensure that the credit card transaction data is stored in a CSV file called csvcard.csv, which you put into your project directory.

Run the main Python script:

_python main.py_

This script will load the data, preprocess it, train multiple machine learning models (Logistic Regression, Random Forest, AdaBoost, and CatBoost), evaluate their performance using the ROC AUC score, and print the best model and corresponding score. To process data, train models and evaluate performance, follow the prompts in this script.

# Description of Design Choices

## Data Preprocessing

- **Handled missing values**: Checked for missing data and deleted duplicate rows. No missing values have been found, and a total of 1081 duplicate rows have been deleted.

- **Data Imbalance Treatment**: To visualize and address the imbalance of classes, used the oversampling technique SMOTE.

- **Skewness Correction**: To correct the skewness in the dataset of the data set, used PowerTransformer.

- **Feature Engineering**: Created new features such as Hour from the Time feature to enhance the model performance.

- **Model Selection and Hyperparameter Tuning**: Used various classification algorithms such as Logistic Regression, Random Forest, AdaBoost, and CatBoost have been used. 

To improve the model's performance, GridSearchCV was used for hyperparameter adjustment.

Evaluated models using key metrics such as accuracy, precision, recall, F1 score, and ROC AUC score.

## Performance Evaluation of the Model

### Model Performance
- **Logistic Regression** : Obtained a ROC AUC score of 94.19% after hyperparameter tuning.

- **Random Forest Classifier**: Obtained an ROC AUC score of 91.53% after hyperparameter tuning.

- **AdaBoost Classifier**: Obtained an ROC AUC score of 92.79% after hyperparameter tuning.

- **CatBoost Classifier**: Obtained an ROC AUC score of 97.61% after hyperparameter tuning.

## Comparison and Selection of Best Model**

The CatBoost Classifier Obtained the highest ROC AUC score of 97.61% among all models. Hence, the CatBoost Classifier is selected as the best model for credit card fraud detection.

# Discussion of Future Work

## Potential Improvements

- Feature Engineering: Additional exploration of feature engineering techniques to enhance model performance.

- Advanced Algorithms: Exploring advanced algorithms like XGBoost, LightGBM, or neural networks. 

- Real-time Monitoring: Implementation of the model into a real-time monitoring system for timely detection of fraudulent transactions.

- Regular Model Updates: Periodic re-training of the model with new data to adjust to changing fraud patterns.

# Benefits for the Company

- **Cost Savings**: This model helps to prevent financial losses resulting from fraud, by accurately identifying fraudulent transactions. This is to reimburse customers for illegal transactions and to mitigate potential legal and administrative penalties related to fraud cases. Overall, by reducing financial liabilities associated with fraud the model helps to reduce costs.

- **Enhanced Customer Trust**: To strengthen customer trust and confidence in the company's services, efficient detection of fraud is important. The customers are reassured that their financial transactions are secure, leading to a higher level of satisfaction and loyalty. This will allow the company to attract and retain more customers, thereby improving its reputation and market position.

- **Reduced Operational Risks**: Fraudulent activities not only result in the company's financial position but also pose operational risks to the company. Such risks include damage to reputation, legislative scrutiny, and the disruption of operations. The company can proactively mitigate these risks and maintain operational resilience by implementing a robust model for detecting fraud.

- **Scalability and Adaptability**: To take into account the evolving needs and business environment of the company, the fraud detection model can be scaled and adapted. To ensure optimal performance, the model may be updated and refined as transaction volumes increase or new fraud patterns emerge. This scalability ensures that the company can effectively manage fraud risks regardless of its growth trajectory.

 
