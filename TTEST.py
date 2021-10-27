# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 10:22:05 2021

@author: apowe
"""

import pandas as pd
from scipy.stats import shapiro 
from matplotlib import pyplot
import scipy.stats as stats
from scipy.stats import ttest_ind

## DF and SAMPLE
diabetes= pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')

diabetes_sample = diabetes.sample(100)

##VAR NAMES
list(diabetes_sample)

## T-TESTS
## QUESTION 1:Is there a difference between sex (M:F) and the number of days in hospital?
list(diabetes)
Male=diabetes[diabetes['gender']=='Male']
Female=diabetes[diabetes['gender']=='Female']
ttest_ind(Female['time_in_hospital'], Male['time_in_hospital'])
##Result:(statistic=9.542637042242887, pvalue=1.4217299655114968e-21)
##The p-value is below .05, this means that there is a significant diffrence between these groups

##QUESTION 2:Is there a difference between RACE (Caucasian and African American) and the number of days in hospital?
list(diabetes)
Caucasian=diabetes[diabetes['race']=='Caucasian']
AfricanAmerican=diabetes[diabetes['race']=='AfricanAmerican']
ttest_ind(Caucasian['time_in_hospital'], AfricanAmerican['time_in_hospital'])
##Result:statistic=-5.0610017032095325, pvalue=4.178330085585203e-07
##The p-value is below .05, this means that there is a significant diffrence between these groups



##QUESTION 3:Is there a difference between RACE (Asian and African American) and the number of lab procedures performed?
list(diabetes)
Caucasian = diabetes[diabetes['race']=='Caucasian']
AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']
ttest_ind(Caucasian['num_lab_procedures'], AfricanAmerican['num_lab_procedures'])
##Result:(statistic=-7.895811662166183, pvalue=2.914809830143658e-15)
##The p-value is below .05, this means that there is a significant diffrence between these groups