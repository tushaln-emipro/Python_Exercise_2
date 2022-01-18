"""
    Program 6 of Python Exercise - 2
"""
county_names = {'USA': 'United States of America','AU':'Astronomical Unit','ES':'Enterprise Solution',
                'DE':'DE','UK':'The United Kingdom','IT':'IT'}
data_dict = {}
import csv
with open('csvdatafile.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile)
    spamreader_lits = list(spamreader)
    for row in spamreader_lits:
        if row['OrderNo'] not in data_dict:
            data_dict[row['OrderNo']] = {"customer": {"name": row['Customer'], 'address 1': row['Address1'],
                                                   'address 2': row['Address2'], 'city': row['City'],
                                                   'country': county_names[row['Country']], 'zipcode': row['Zipcode']},
                                      'orderLines': []}
        else:
            data_dict[row['OrderNo']]['orderLines'].append({'sku': row['SKU'], 'price': row['Price'], 'qty': row['Qty']})

print(data_dict)
