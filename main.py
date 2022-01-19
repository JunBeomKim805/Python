import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('Agg')

response = pd.read_csv('school.csv')
res = pd.DataFrame(response)
res_sort = res.sort_values(by=['REF_DATE'])

is_on = True

while is_on:
    choice = input("Choose number in menu (1~4) ")
    if choice == '1':
        search = input("Type the year you want to search ")
        for (index, row) in res.iterrows():
            if(row['REF_DATE'][0:4] == search):
                print(row)

    if choice == '2':
        for (index, row) in res_sort.iterrows():
            print(row)
        print('sorted by year')
    if choice == '3':
        res_sort.plot( x='REF_DATE', y='VALUE')
        plt.savefig('graph.png')

    if choice == '4':
        is_on=False
