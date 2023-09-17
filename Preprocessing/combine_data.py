import pandas as pd


def drop_empty_degrees(df):
    df = df[df['Degree_Field'].isnull() == False]
    return df

def join_auditor_education(df_auditor, df_education):
    df = pd.merge(df_auditor, df_education, how='inner', left_on='ID', right_on='ID')
    return df

def unique_ids(df):
    df = df.drop_duplicates(subset=['ID'])
    return df

if __name__ == "__main__":
    df_education = pd.read_csv('data/Auditor/Auditors_Education.csv')
    df_gender = pd.read_csv('data/Auditor/Auditors_Gender.csv')
    print(f"Education rows = {df_education.shape[0]}, gender rows = {df_gender.shape[0]}")

    # print(df_education[df_education["ID"]=='EP0018501129'])

    df_combo = join_auditor_education(df_gender, df_education)
    print("Combo rows (Initial)",df_combo.shape[0])
    df_combo = drop_empty_degrees(df_combo)
    print("Combo rows (after)",df_combo.shape[0])
    # print(df_combo.head())

    df_combo = unique_ids(df_combo)
    # print(df_combo.head())
    print(f"final rows = {df_combo.shape[0]}")
    df_combo.to_csv("auditors_combined.csv")
