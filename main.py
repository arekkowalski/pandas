import numpy as np
import pandas as pd
import xlrd
import openpyxl

# zad1
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)

# zad2
# print(df[df['Liczba'] < 1000])
# print()

# print(df[df.Imie == 'ARKADIUSZ'])
# print()

# print(sum(df['Liczba']))
# print()

# print(sum(df['Liczba'] & ((df.Rok) > 2004) & ((df.Rok) < 2011) ))
# print()

# print(sum(df['Liczba'] & ((df.Plec) == 'M') & ((df.Rok) == 2000) ))
# print()

# d = df[(df.Plec == 'K')]
# m = df[(df.Plec == 'M')]
# print(df.Imie[df.Liczba == max(d.Liczba)])
# print(df.Imie[df.Liczba == max(m.Liczba)])

# grupa = df.groupby(['Rok', 'Plec']).agg({'Liczba':['max']})
# print(grupa)

# zad3
# df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal=',')
# nazwiska = df['Sprzedawca']
# nazwiska = nazwiska.unique()
# print(pd.Series(nazwiska))
#
# df['Utarg'] = df['Utarg'].astype(float)
# utargi = (df.sort_values(by='Utarg', ascending=False).head(5))
# print(utargi['Utarg'])
#
# print(df.groupby('Sprzedawca').agg({'Sprzedawca':['count']}))
#
# print(df.groupby('Kraj').agg({'Kraj':['count']}))
#
# df['Data zamowienia'] = df['Data zamowienia'].astype('datetime64[ns]')
# polacy = (df[(df.Kraj == 'Polska') & (df['Data zamowienia'].dt.year == 2005)])
# print(polacy.groupby('Kraj').agg({'Utarg':['sum']}))
#
# czwarty = df[(df['Data zamowienia'].dt.year == 2004)]
# print(czwarty['Utarg'].mean())
#
# czwarty = df[(df['Data zamowienia'].dt.year == 2004)]
# piaty = df[(df['Data zamowienia'].dt.year == 2005)]
# czwarty.to_csv('zamowienia_2004.csv', index=False)
# piaty.to_csv('zamowienia_2005.csv', index=False)