import pandas as pd
# import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
import csv
from malss import MALSS
import time
# import better_exceptions
# better_exceptions.MAX_LENGTH = None
import os


pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def mapSex(df):
    df["Sex"] = df["Sex"].map({"female": 0, "male": 1}).astype(int)
    # df = df.drop("Sex", axis=1)
    return df


def mapEmbarked(df):
    # df["Embarked"] = df["Embarked"].map({"C": 0, "Q": 1, "S": 2}).astype(int)
    df = df.drop("Embarked", axis=1)
    return df


def mapAge(df):
    # df["Age"] = df["Age"].fillna(df.Age.median())
    return df


def mapFare(df):
    # df["Fare"] = df["Fare"].fillna(df.Fare.median())
    return df


def mapFamilySize(df):
    # df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
    return df


def mapName(df):
    def name_classifier(name_df):
        columns = {'Miss', 'Mrs', 'Master', 'Mr'}
        name_class_df = pd.DataFrame(columns=columns)
        for name in name_df:
            if 'Miss' in name:
                ldf = pd.DataFrame([[1, 0, 0, 0]], columns=columns)
            elif 'Mrs' in name:
                ldf = pd.DataFrame([[0, 1, 0, 0]], columns=columns)
            elif 'Master' in name:
                ldf = pd.DataFrame([[0, 0, 1, 0]], columns=columns)
            elif 'Mr' in name:
                ldf = pd.DataFrame([[0, 0, 0, 1]], columns=columns)
            else:
                ldf = pd.DataFrame([[0, 0, 0, 0]], columns=columns)
            name_class_df = name_class_df.append(ldf, ignore_index=True)
        return name_class_df
    df = pd.concat([df, name_classifier(df.Name)], axis=1)
    df = df.drop("Name", axis=1)
    return df


def func(df):
    arr = ["SibSp", "Parch", "Ticket", "Cabin", "Sex", "Age", "Fare"]
    df = mapName(df)
    df = mapSex(df)
    df = mapEmbarked(df)
    df = mapAge(df)
    df = mapFare(df)
    df = mapFamilySize(df)
    return df.drop(arr, axis=1)


df = pd.read_csv("train.csv")
df = func(df)
print(df.isnull().any())
forest = RandomForestClassifier(n_estimators=10, max_depth=7, max_features=0.3)
forest = forest.fit(df.values[:, 2:], df["Survived"].values)
test_data = func(pd.read_csv("test.csv")).values
xs_test = test_data[:, 1:]
output = forest.predict(xs_test)
zip_data = zip(test_data[:, 0].astype(int), output.astype(int))
predict_data = list(zip_data)

os.makedirs("tmp", exist_ok=True)
with open("tmp/submission-" + time.strftime('%d%m%Y%H%M%S') + ".csv", "w") as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["PassengerId", "Survived"])
    for pid, survived in zip(test_data[:, 0].astype(int), output.astype(int)):
        writer.writerow([pid, survived])
#
# X = df.values[:, 2:]
# y = df["Survived"].values
#
# from sklearn import svm
#
# clf = svm.SVC(C=10.0, gamma=0.01)
# clf.fit(X, y)
# output = clf.predict(xs_test)
# zip_data = zip(test_data[:, 0].astype(int), output.astype(int))
# predict_data = list(zip_data)
#
# with open("tmp/submission.csv", "w") as f:
#     writer = csv.writer(f, lineterminator='\n')
#     writer.writerow(["PassengerId", "Survived"])
#     for pid, survived in zip(test_data[:, 0].astype(int), output.astype(int)):
#         writer.writerow([pid, survived])


        # cls = MALSS('classification',
        #             shuffle=True, standardize=True, n_jobs=3,
        #             random_state=0, lang='jp', verbose=True)
        # cls.fit(X, y, 'tmp/result_classification')
