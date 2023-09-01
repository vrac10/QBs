""" Importing all the require libraries
1) Random forest regressor - The machine laerning model that is used here to perform the fitting and predictions
2 train_test_split - To split the train data for validation purposes
3) numpy - To perform numpy array operations , in this case the square root as the competition uses rms metric
4) math - To make use of the euler's constant
5) pandas - To extract , use, make changes and all other data related operations
6) mean_squared_error - To calculate the error"""

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import numpy as np
import math
import pandas as pd
from sklearn.metrics import mean_squared_error

#----------------------Data Loading--------------------------#

path = "kaggle/train.csv" # Local file

data = pd.read_csv(path)

path2 = "kaggle/test.csv" # Local file 

test_data = pd.read_csv(path2)

""" The columns QV2M and T2M are present in the train dataset but not present in test data set hence the model cannot be trained on the entire dataset.

To tackle this, the missing columns of the test data set can be calculated using the other values in the columns. """

#----------------------T2M calculations----------------------#

# The T2M column is the average temperature so # can be calculated by taking (Minimum+maximum)/2

test_data['T2M'] = (test_data['T2M_MAX'] + test_data['T2M_MIN'])/2
print(test_data.head())

#----------------------QV2M calculations----------------------#

# Saturation_vapour_pressure = 6.112 * exp(17.67 * T_avg / (T_avg + 243.5))
# Actual_vapour_pressure = (RH2M / 100) * Saturation_vapour_pressure
# QV2M = (0.622 * Actual_vapour_pressure) / (PS - 0.378 * Actual_vapour_pressure)

QV2M = []

test_data['QV1M'] = x
for i in range(len(test_data['T2M'])):
    Saturation_vapour_pressure = 6.112 * math.exp(17.67 * test_data['T2M'][i] / (test_data['T2M'][i] + 243.5))
    Actual_vapour_pressure = (test_data['RH2M'][i] / 100) * Saturation_vapour_pressure
    x = 100*(0.622 * Actual_vapour_pressure) / (test_data['PS'][i] - 0.378 * Actual_vapour_pressure)
    QV2M.append(x)


test_data['QV2M'] = QV2M

#-------------------------Model Creation------------------------#

features = ['YEAR', 'T2M_RANGE', 'T2M_MAX', 'T2M_MIN', 'RH2M', 'PS', 'WS10M','T2M','QV2M']

X = data[features]
Y = data["VACATION_RATE"]

# train_x,val_x,train_y,val_y = train_test_split(X,Y, random_state= 1)
def model_test(x,y,w,z,n):
    model = RandomForestRegressor(n,random_state= 1)
    model.fit(x,y)
    predictions = model.predict(w)
    error = np.sqrt(mean_squared_error(z,predictions))
    return error


# for i in [10,50,100,250,500,750,1000,1050]:
#      print(model_test(train_x, train_y,val_x,val_y,i), i)

VACATION_RATE = RandomForestRegressor(1050)

VACATION_RATE.fit(X,Y)

actual = test_data.drop(['ID'],axis= 1)
predictions = VACATION_RATE.predict(actual)

final = pd.DataFrame({'ID' : test_data['ID'],
                     'VACATION_RATE' : predictions})

final.to_csv('submission.csv', header=['ID','VACATION_RATE'], index=False)
