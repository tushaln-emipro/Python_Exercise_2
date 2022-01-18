"""
    Program 8 of Python Exercise - 2
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

# from openpyxl import Workbook

import xlsxwriter
workbook = xlsxwriter.Workbook('NewCustomerData.xls')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Order No')
worksheet.write('B1', 'Customer')
worksheet.write('C1', 'SKU')
worksheet.write('D1', 'Qty')
worksheet.write('E1', 'Price')
worksheet.write('F1', 'Address1')
worksheet.write('G1', 'Address2')
worksheet.write('H1', 'Zipcode')
worksheet.write('I1', 'City')
worksheet.write('J1', 'Country')

row = 1
col = 0
for a in data_dict:
    for b in data_dict[a]['orderLines']:
        worksheet.write(row, col, a)
        worksheet.write(row, col + 1, data_dict[a]['customer']['name'])
        worksheet.write(row, col + 2, b['sku'])
        worksheet.write(row, col + 3, b['price'])
        worksheet.write(row, col + 4, b['qty'])
        worksheet.write(row, col + 5, data_dict[a]['customer']['address 1'])
        worksheet.write(row, col + 6, data_dict[a]['customer']['address 2'])
        worksheet.write(row, col + 7, data_dict[a]['customer']['zipcode'])
        worksheet.write(row, col + 8, data_dict[a]['customer']['city'])
        worksheet.write(row, col + 9, data_dict[a]['customer']['country'])
        row += 1

workbook.close()
