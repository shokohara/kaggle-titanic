import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
import csv

arr = ["Name", "Age", "Sex", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked", "AltEmbarked"]
df = pd.read_csv("train.csv")
df["AltSex"] = df["Sex"].map({"female": 0, "male": 1}).astype(int)
df["AltEmbarked"] = df["Embarked"].map({"C": 0, "Q": 1, "S": 2})
df["AltAge"] = df["Age"].fillna(df.Age.median())
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df = df.drop(arr, axis=1)

print(df.dtypes)
xs = df.values[:, 2:]
y = df.values[:, 1]

forest = RandomForestClassifier(n_estimators=100)
forest = forest.fit(xs, y)

test_df = pd.read_csv("test.csv")
test_df["AltSex"] = test_df["Sex"].map({"female": 0, "male": 1}).astype(int)
test_df["AltEmbarked"] = test_df["Embarked"].map({"C": 0, "Q": 1, "S": 2})
test_df["AltAge"] = test_df["Age"].fillna(test_df.Age.median())
test_df["FamilySize"] = test_df["SibSp"] + test_df["Parch"] + 1
test_df = test_df.drop(arr, axis=1)
test_data = test_df.values
xs_test = test_data[:, 1:]
output = forest.predict(xs_test)
zip_data = zip(test_data[:, 0].astype(int), output.astype(int))
predict_data = list(zip_data)

with open("tmp/submission.csv", "w") as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["PassengerId", "Survived"])
    for pid, survived in zip(test_data[:, 0].astype(int), output.astype(int)):
        writer.writerow([pid, survived])
