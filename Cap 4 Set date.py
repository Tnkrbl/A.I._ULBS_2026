import numpy as np

import pandas as pd

import openpyxl as xl
from pandas import set_option

data = pd.read_excel(r'D:\Facultate\Anul III\Inteligenta Artificiala\data.xlsx')

set_option('display.max_columns', None)
set_option('display.max_rows', None)

# print(data.head())

first_10 = data[data['Age'] > 40].head(10)
# print(first_10)

overall_age = data[(data['Overall'] >= 85) & (data['Age'] <25)].head(10)
# print(overall_age)

skill_moves = data.sort_values(by='Skill Moves', ascending=True).head(10)
#print(skill_moves)

contract = data[data['Contract Valid Until'] == 2021].head(10)
print(contract)




