"""
    Program 7 of Python Exercise - 2
"""
county_names = {'USA': 'United States of America','AU':'Astronomical Unit','ES':'Enterprise Solution',
                'DE':'DE','UK':'The United Kingdom','IT':'IT'}
data_dict = {}
import csv
with open('customerdata.csv', newline='') as csvfile:
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
with open('NewCustomerData.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Order No', 'Customer', 'SKU', 'Qty', 'Price', 'Address1', 'Address2', 'Zipcode',
                         'City', 'Country'])
    for a in data_dict:
        for b in data_dict[a]['orderLines']:
            spamwriter.writerow([a, data_dict[a]['customer']['name'], b['sku'], b['price'], b['qty'],
                                 data_dict[a]['customer']['address 1'], data_dict[a]['customer']['address 2'],
                                 data_dict[a]['customer']['zipcode'], data_dict[a]['customer']['city'],
                                 data_dict[a]['customer']['country']])
