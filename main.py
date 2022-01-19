import requests
import pandas as pd
import matplotlib.pyplot as plt
plt.close("all")
response = pd.read_csv('school.csv')
res = pd.DataFrame(response)

is_on = True

while is_on:
    choice = input("Choose number in menu (1~4) ")
    if choice == '1':
        search = int(input("Type the index you want to search "))
        for (index, row) in res.iterrows():
            if index == search:
                print(row)

    if choice == '2':
        for (index, row) in res.iterrows():
            print(row)
    if choice == '3':
        res['Students'] = res['Students'].astype(int);

        res["Students"].plot(y='Students')
        plt.show()

    if choice == '4':
        is_on=False
