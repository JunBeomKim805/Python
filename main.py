import requests
import pandas as pd
import matplotlib.pyplot as plt
plt.close("all")
response = pd.read_csv('school.csv')
res = pd.DataFrame(response)
res_sort = res.sort_values(by=['REF_DATE'])


is_on = True

while is_on:
    choice = input("Choose number in menu (1~4) ")
    if choice == '1':
        search = int(input("Type the index you want to search "))
        for (index, row) in res.iterrows():
            if index == search:
                print(row)

    if choice == '2':
        for (index, row) in res_sort.iterrows():
            print(row)
        print('sorted by year')
    if choice == '3':
        res_sort.plot(stacked=True, x='REF_DATE', y='VALUE')
        plt.show()

    if choice == '4':
        is_on=False
