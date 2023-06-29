import pandas as pd
from scipy import stats
import numpy as np

def explanatory_analysis(charges_data_path, personal_data_path, plan_data_path):
    # write you solution here

    # part 1
    charges_data = pd.read_csv(charges_data_path)
    personal_data = pd.read_csv(personal_data_path)
    plan_data = pd.read_csv(plan_data_path)

    # part 2
    trimmed_mean = stats.trim_mean(charges_data['monthlyCharges'], proportiontocut=0.1)
    trimmed_mean = round(trimmed_mean)

    charges_data['monthlyCharges'].fillna(trimmed_mean, inplace=True)
    charges_data['totalCharges'].fillna(charges_data['monthlyCharges']* \
    charges_data['tenure'], 
    inplace=True)

    # part 3
    bins = [0, 24, 48, 60, float('inf')]  
    labels = ['group1', 'group2', 'group3', 'group4'] 
    charges_data['tenureBinned'] = pd.cut(charges_data['tenure'], 
                                            bins=bins, 
                                            labels=labels)

    # part 4
    charges_data['churn'] = charges_data['churn'].map({'No': 0, 'Yes': 1})
    churn_rate = round(sum(charges_data['churn'])/len(charges_data['churn'])*100)

    # part 5
    merged_data = charges_data.merge(personal_data, on='customerID', how='inner')
    merged_data = merged_data.merge(plan_data, on='customerID', how='left')

    # part 6
    age_check = (merged_data['age'] > 60).astype(int)
    above_80 = round(np.mean(age_check)*100)

    # part 7
    internet_service_counts = merged_data['internetService'].value_counts().to_dict()

    results = {
        "monthly_charges_mean": trimmed_mean,
        "charges_data_updated": charges_data,
        "churn_pct": churn_rate, 
        "data_merged": merged_data, 
        "pct_age_above_60": above_80, 
        "internet_service_counts": internet_service_counts 
    }
    return results




out = explanatory_analysis('./data/charges_data.csv',
                      './data/personal_data.csv', 
                      './data/plan_data.csv')

print(out)                     