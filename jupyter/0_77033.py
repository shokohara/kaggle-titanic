import csv
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

arr = ["Name", "Age", "Sex", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]


def func(ldf):
    ldf["Sex"] = ldf["Sex"].map({"female": 0, "male": 1}).astype(int)
    ldf["AltAge"] = ldf["Age"].fillna(ldf.Age.median())
    ldf["AltFare"] = ldf["Fare"].fillna(ldf.Fare.median())
    ldf["FamilySize"] = ldf["SibSp"] + ldf["Parch"] + 1
    ldf = pd.concat([ldf, name_classifier(ldf.Name)], axis=1)
    return ldf.drop(arr, axis=1)


def name_classifier(name_df):
    name_class_df = pd.DataFrame(columns={'miss', 'mrs', 'master', 'mr'})
    for name in name_df:
        if 'Miss' in name:
            ldf = pd.DataFrame([[1, 0, 0, 0]], columns={'miss', 'mrs', 'master', 'mr'})
        elif 'Mrs' in name:
            ldf = pd.DataFrame([[0, 1, 0, 0]], columns={'miss', 'mrs', 'master', 'mr'})
        elif 'Master' in name:
            ldf = pd.DataFrame([[0, 0, 1, 0]], columns={'miss', 'mrs', 'master', 'mr'})
        elif 'Mr' in name:
            ldf = pd.DataFrame([[0, 0, 0, 1]], columns={'miss', 'mrs', 'master', 'mr'})
        else:
            ldf = pd.DataFrame([[0, 0, 0, 0]], columns={'miss', 'mrs', 'master', 'mr'})
        name_class_df = name_class_df.append(ldf, ignore_index=True)
    return name_class_df


df = pd.read_csv("train.csv")
df = func(df)
forest = RandomForestClassifier(n_estimators=10, max_depth=7, max_features=0.3)
forest = forest.fit(df.values[:, 2:], df["Survived"].values)
test_data = func(pd.read_csv("test.csv")).values
xs_test = test_data[:, 1:]
output = forest.predict(xs_test)
zip_data = zip(test_data[:, 0].astype(int), output.astype(int))
predict_data = list(zip_data)

with open("tmp/submission.csv", "w") as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["PassengerId", "Survived"])
    for pid, survived in zip(test_data[:, 0].astype(int), output.astype(int)):
        writer.writerow([pid, survived])
