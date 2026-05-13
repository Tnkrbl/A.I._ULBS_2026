import pandas as pd

import openpyxl as xl
from pandas import set_option

# EXPLORAREA DATELOR

data = pd.read_csv(r'D:\Facultate\Anul III\Inteligenta Artificiala\StudentsPerformance.csv')

set_option('display.max_columns', None)
set_option('display.max_rows', None)

# print(data.head(5))

# data.info()

describe = data.describe()

# print(describe)

# IDENTIFICAREA TIPURILORE DE VARIABILE

categorice = data.select_dtypes(exclude=['number']).columns.tolist()
numerice = data.select_dtypes(include=['number']).columns.tolist()

print("Variabile categorice:", categorice)
print("Variabile numerice:", numerice)

for col in categorice:
    print(f"\n{col}: {data[col].nunique()} valori unice")
    print(f"  -> {data[col].unique()}")

# CURATAREA DATELOR

print("Valori lipsa (inainte)")
missing_initial = data.isnull().sum()
print(missing_initial)
print(f"\nTotal valori lipsa: {missing_initial.sum()}")

for col in numerice:
    if data[col].isnull().sum() > 0:
        mediana = data[col].median()
        data[col] = data[col].fillna(mediana)
        print(f"[NUMERIC] '{col}' → înlocuit cu mediana: {mediana}")

for col in categorice:
    if data[col].isnull().sum() > 0:
        data[col] = data[col].fillna('Unknown')
        print(f"[CATEGORIC] '{col}' → înlocuit cu 'Unknown'")

print("\nValori lipsa (dupa)")
missing_final = data.isnull().sum()
print(missing_final)
print(f"\nTotal valori lipsa ramase: {missing_final.sum()}")

if missing_final.sum() == 0:
    print("\nDate OK — nu exista valori lipsa!")
else:
    print("\nExista valori lipsa!")

