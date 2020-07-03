# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here

#STEP 1
bank=pd.DataFrame(bank_data)

categorical_var=bank.select_dtypes(include='object')
print(categorical_var.shape)

numerical_var=bank.select_dtypes(include='number')
print(numerical_var.shape)

#STEP 2
banks=pd.DataFrame(bank.drop(['Loan_ID'],axis=1))
print(banks.shape)

bank_mode=banks.mode()
banks=banks.fillna(bank_mode.iloc[0])
print(banks.isnull().sum().values.sum())

#STEP 3
avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')
print(avg_loan_amount['LoanAmount'][1],2)

#STEP 4
loan_approved_se=len(banks[(banks['Self_Employed']== 'Yes') & (banks['Loan_Status']== 'Y')])
loan_approved_nse=len(banks[(banks['Self_Employed']== 'No') & (banks['Loan_Status']== 'Y')])
Loan_Status=614

percentage_se=(loan_approved_se/Loan_Status*100)
print(percentage_se)
percentage_nse=(loan_approved_nse/Loan_Status*100)
print(percentage_nse)

#STEP 5
loan_term=banks['Loan_Amount_Term'].apply(lambda x: x/12)
big_loan_term=len(banks[loan_term>=25])
print(big_loan_term)

#STEP 6
loan_groupby=banks.groupby('Loan_Status')
loan_groupby=loan_groupby[['ApplicantIncome','Credit_History']]
mean_values=loan_groupby.mean()
print(mean_values.iloc[1,0], 2)




