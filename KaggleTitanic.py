import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("train.csv")
# print(df.dtypes)
df["Gender"] = df["Sex"].map({"female": 0, "male": 1}).astype(int)
print(df["Gender"])

import pandas as pd
import pylab as plt

data = pd.read_csv("train.csv").replace("male",0).replace("female",1)
data = data.replace("C",0).replace("Q",1).replace("S",2)
split_data = []
for did_survive in [0,1]:
    split_data.append(data[data.Survived==did_survive])
temp = [i["Age"].dropna() for i in split_data]
plt.hist(temp, histtype="barstacked", bins=16)
plt.show()

temp = [i["Pclass"].dropna() for i in split_data]
plt.hist(temp, histtype="barstacked", bins=3)
plt.show()
# print((df["Gender"] + df["Sex"]))
# print(df.head(10))
# df["Age"].fillna(df.Age.median(), inplace=True)
#
# df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
# df2 = df.drop(["Name", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"], axis=1)
# print(df2)
# train_data = df2.values
# xs = train_data[:, 2:]
# y = train_data[:, 1]
# # print(y)
#
# forest = RandomForestClassifier(n_estimators=100)
# # 学習
# forest = forest.fit(xs, y)
#
# test_df = pd.read_csv("test.csv").replace("male", 0).replace("female", 1)
# # 欠損値の補完
# test_df["Age"].fillna(df.Age.median(), inplace=True)
# test_df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
# test_df2 = test_df.drop(["Name", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"], axis=1)
#
# test_data = test_df2.values
# xs_test = test_data[:, 1:]
# output = forest.predict(xs_test)
#
# print(len(test_data[:, 0]), len(output))
# zip_data = zip(test_data[:, 0].astype(int), output.astype(int))
# predict_data = list(zip_data)
# print(predict_data)
# import csv
#
# with open("predict_result_data.csv", "w") as f:
#     writer = csv.writer(f, lineterminator='\n')
#     writer.writerow(["PassengerId", "Survived"])
#     for pid, survived in zip(test_data[:, 0].astype(int), output.astype(int)):
#         writer.writerow([pid, survived])
