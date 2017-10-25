import pandas as pd


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
    name_class_df["miss"] = name_class_df["miss"].astype(int)
    name_class_df["mrs"] = name_class_df["mrs"].astype(int)
    name_class_df["master"] = name_class_df["master"].astype(int)
    name_class_df["mr"] = name_class_df["mr"].astype(int)
    return name_class_df


def func(ldf):
    arr = ["Name"]
    ldf["Sex"] = ldf["Sex"].map({"female": 0, "male": 1}).astype(int)
    ldf = pd.concat([ldf, name_classifier(ldf.Name)], axis=1)
    return ldf.drop(arr, axis=1)