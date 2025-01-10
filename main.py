import pandas as pd
from pandas import DataFrame

#Загрузка DataFrame
df = pd.read_csv('dz02.csv', encoding='windows-1251')
#Вывод первых 5 строк
print(df.head())
print()
print(f"Средняя оценка по алгебре - {df['Алгебра'].mean()}")
print(f"Средняя оценка по английскому - {df['Английский'].mean()}")
print(f"Средняя оценка по биологии - {df['Биология'].mean()}")
print(f"Средняя оценка по географии - {df['География'].mean()}")
print(f"Средняя оценка по геометрии - {df['Геометрия'].mean()}")
print()
print(f"Медианная оценка по алгебре - {df['Алгебра'].median()}")
print(f"Медианная оценка по английскому - {df['Английский'].median()}")
print(f"Медианная оценка по биологии - {df['Биология'].median()}")
print(f"Медианная оценка по географии - {df['География'].median()}")
print(f"Медианная оценка по геометрии - {df['Геометрия'].median()}")

