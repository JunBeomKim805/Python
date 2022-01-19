import requests
import pandas as pd
import matplotlib.pyplot as plt
plt.close("all")
response = requests.get("https://data.princeedwardisland.ca/resource/bpnh-prdc.json")
res = pd.DataFrame(response.json())
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
        res['students'] = res['students'].astype(int);

        res["students"].plot(y='students')
        plt.show()

    if choice == '4':
        is_on=False
