import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
import csv

arr = ["Name", "Age", "Sex", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]


def func(ldf):
    ldf["AltSex"] = ldf["Sex"].map({"female": 0, "male": 1}).astype(int)
    # 欠損値が存在するため失敗する
    # ldf["AltEmbarked"] = ldf["Embarked"].map({"C": 0, "Q": 1, "S": 2}).astype(int)
    ldf["AltAge"] = ldf["Age"].fillna(ldf.Age.median())
    ldf["AltFare"] = ldf["Fare"].fillna(ldf.Fare.median())
    ldf["FamilySize"] = ldf["SibSp"] + ldf["Parch"] + 1
    ldf = pd.concat([ldf, name_classifier(ldf.Name)], axis=1)
    return ldf.drop(arr, axis=1)


# def name_classifier(name_df):
#     obj = {'miss', 'mrs', 'master', 'mr'}
#     name_class_df = pd.DataFrame(columns=obj)
#     for name in name_df:
#         if 'Miss' in name:
#             local_df = [1, 0, 0, 0]
#         elif 'Mrs' in name:
#             local_df = [0, 1, 0, 0]
#         elif 'Master' in name:
#             local_df = [0, 0, 1, 0]
#         elif 'Mr' in name:
#             local_df = [0, 0, 0, 1]
#         else:
#             local_df = [0, 0, 0, 0]
#         print("abc")
#         print(local_df)
#         name_class_df = name_class_df.append(pd.DataFrame([local_df], columns=obj), ignore_index=True)
#     # return name_class_df
#     return name_class_df


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
# name_df_train = df.iloc[:, 3]
# survive_array = df.iloc[:, 1]
# # print(df.isnull().sum())
# for name in df.iloc[:, 3]:
#     name_split = name.split(" ")
#     # name_split_first = name_split.map
#     name.split(" ").head
#     # print(name_split_first)
df = func(df)

forest = RandomForestClassifier(n_estimators=120)
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
