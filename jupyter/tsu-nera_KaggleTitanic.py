# https://github.com/tsu-nera/kaggle/blob/master/titanic/titanic-keras-nn.ipynb
import numpy as np
import pandas as pd

import keras
from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.core import Flatten, Dense, Activation, Dropout

row_data = pd.read_csv('train.csv', index_col=0)
test_data = pd.read_csv('test.csv', index_col=0)
test_ind = test_data.index

data = row_data[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']].dropna()
t_data = test_data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]

Pclass = pd.get_dummies(data['Pclass'])
Pclass.columns = ['1st', '2nd', '3rd']
Pclass = Pclass.drop('1st', axis=1)

tPclass = pd.get_dummies(t_data['Pclass'])
tPclass.columns = ['1st', '2nd', '3rd']
tPclass = tPclass.drop('1st', axis=1)

Sex = pd.get_dummies(data['Sex'])
Sex = Sex.drop('male', axis=1)

tSex = pd.get_dummies(t_data['Sex'])
tSex = tSex.drop('male', axis=1)


def adult_kids(age):
    if age > 15:
        if age > 60:
            return 'older'
        else:
            return 'adult'
    else:
        if age < 16:
            return 'kids'
        else:
            return np.nan


data['adult_kids'] = data['Age'].apply(adult_kids)
Age_cat = pd.get_dummies(data['adult_kids']).drop('adult', axis=1)
t_data['adult_kids'] = t_data['Age'].apply(adult_kids)
tAge_cat = pd.get_dummies(t_data['adult_kids']).drop('adult', axis=1)

Data_tmp = data[['Survived', 'SibSp', 'Parch', 'Fare']]

Merge_data = pd.merge(Data_tmp, Pclass, right_index=True, left_index=True)
Merge_data = pd.merge(Merge_data, Sex, right_index=True, left_index=True)
Merge_data = pd.merge(Merge_data, Age_cat, right_index=True, left_index=True)
y = Merge_data['Survived'].values
x = Merge_data.drop('Survived', axis=1).values

Data_tmp = t_data[['SibSp', 'Parch', 'Fare']]

Merge_data = pd.merge(Data_tmp, tPclass, right_index=True, left_index=True)
Merge_data = pd.merge(Merge_data, tSex, right_index=True, left_index=True)
Merge_data = pd.merge(Merge_data, tAge_cat, right_index=True, left_index=True)
tx = Merge_data

(x.shape, y.shape, tx.shape)

# create model
model = Sequential()
model.add(Dense(64, input_shape=(8,)))

for i in range(0, 8):
    model.add(Dense(units=64))
    model.add(Activation('relu'))

model.add(Dense(units=1))
model.add(Activation('linear'))

model.compile(loss='mean_squared_error', optimizer='rmsprop')

model.fit(x, y, epochs=300)

p_survived = model.predict_classes(tx.values)
submission = pd.DataFrame()
submission['PassengerId'] = test_ind
submission['Survived'] = p_survived
submission.to_csv('tmp/submission.csv', index=False)
