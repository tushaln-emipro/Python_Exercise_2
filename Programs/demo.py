
# product_details = \
#     {'PRD1': {'ProductName': 'Tea', 'ProductUnitPrice': '10', 'product_stock': '5'},
#      'PRD2': {'ProductName': 'Coffee', 'ProductUnitPrice': '12', 'product_stock': '10'}}
# product_stock_details = {'PRD1': 20, 'PRD2': 10}
# product_details['PRD1'].pop('product_stock', None)
# print(product_details['PRD1'])

# sales_order_details = {'SO1': {'customer': 'cust_1', 'order_line':
#     [{'product_sku': 'PRD1', 'unit_price': 10, 'quantity': 1, 'sub_total': 10, 'state': 'Draff'},
#      {'product_sku': 'PRD2', 'unit_price': 15, 'quantity': 1, 'sub_total': 15, 'state': 'Draff'}],
#                        'order_date': '2021-12-06', 'state': 'Draft', 'order_total_amount': 20}}

sales_order_details = {'SO1': {'customer': 'cust_1', 'order_line':
     [{'product_sku': 'PRD1', 'unit_price': 10, 'quantity': 1, 'sub_total': 10, 'state': 'Draft'},
      {'product_sku': 'PRD2', 'unit_price': 10, 'quantity': 1, 'sub_total': 10, 'state': 'Draft'}],
                               'order_date': '2021-12-06', 'state': 'Draft', 'order_total_amount': 20},
                       'SO2': {'customer': 'cust_2', 'order_line':
    [{'product_sku': 'PRD1', 'unit_price': 10, 'quantity': 1, 'sub_total': 10, 'state': 'Draft'},
     {'product_sku': 'PRD2', 'unit_price': 10, 'quantity': 1, 'sub_total': 10, 'state': 'Draft'}],
                               'order_date': '2021-12-06', 'state': 'Draft', 'order_total_amount': 20}}


# product_stock_details = {'PRD1': 10,'PRD2': 10}
# sales_order_details['state'] = 'Confirm'
print(sales_order_details['SO1']['order_line'])

for i in sales_order_details['SO1']['order_line']:
    print(i['product_sku'])

for i in sales_order_details:
    print("\n{:<5} {:<10} {:<10} {:<10}".format('Sale Order NO : ', i, 'Customer :', sales_order_details[i]['customer']))
    print("{:<10} {:<8} {:<10} {:<12}{:<12}".format('Product SKU |', 'Unit Price |', 'Quantity |', 'Sub Total |', 'State |'))
    for j in sales_order_details[i]['order_line']:
        print("{:<15} {:<12} {:<10} {:<10}{:<12}".format(j['product_sku'], j['unit_price'], j['quantity'], j['sub_total'], j['state']))


delivery_order_details = {'DO1': {'sales_order': 'SO1', 'customer_id': 'cust_1', 'stock_moves':
    [{'product_code': 'PRD1', 'product_qty': 1, 'state': 'Confirm'}], 'state': 'Draft'},
    'DO2': {'sales_order': 'SO1', 'customer_id': 'cust_1', 'stock_moves':
    [{'product_code': 'PRD1', 'product_qty': 1, 'state': 'Confirm'}], 'state': 'Draft'}
                          }


print(delivery_order_details['DO1']['state'])

if delivery_order_details.get('DO1'):
    print('Sorry not DO key found. Please try again....')
else:
    print('Sorry not DO key found. Please try again..')

# if delivery_order_details:
#     for i in delivery_order_details:
#         print(
#             "\n{:<5} {:<10} {:<10} {:<10}".format('DO No. : ', i, 'SO No. :', delivery_order_details[i]['sales_order']))
#         print("{:<10} {:<10} {:<12} ".format('Product Code |', 'Quantity |', 'State |'))
#         for j in delivery_order_details[i]['stock_moves']:
#             print("{:<15} {:<8} {:<12}".format(j['product_code'], j['product_qty'], j['state']))
# else:
#     print('No any delivery order')

# sales_order_details['SO2']['state'] = 'c'
# print(sales_order_details['SO2']['state'])
# print(sales_order_details.get('SO3'))
# print(sales_order_details['SO1']['order_line'])
# print(product_stock_details)
# for i in sales_order_details['SO1']['order_line']:
#     if product_stock_details.get(i['product_sku']) != None:
#         product_stock_details[i['product_sku']] -= i['quantity']


# print(product_stock_details['PRD1'])

temp_stock_moves_list = []
for i in sales_order_details['SO1']['order_line']:
    temp_stock_moves_list.append({'product_code': i['product_sku'], 'product_qty': i['quantity'], 'state': i['state']})

delivery_order_details = {'DO1': {'sales_order': 'SO1', 'customer_id': 'cust_1', 'stock_moves':
    [{'product_code': 'PRD1', 'product_qty': 1, 'state': 'Confirm'}], 'state': 'Draft'}}

# print(delivery_order_details)
# print('001',delivery_order_details['DO1']['state'])

# print(delivery_order_details['DO1']['sales_order'])
# print(delivery_order_details['DO1']['state'])
# for i in delivery_order_details:
#     if (delivery_order_details[i]['sales_order'] == 'SO1'):
#         print(i)

# for key_order_line in sales_order_details[delivery_order_details['DO1']['sales_order']]['order_line']:
#     if product_stock_details.get(key_order_line['product_sku']) != None:
#         print(key_order_line)

# for i in delivery_order_details['DO1']['stock_moves']:
#     i['state'] = 'Done'

# print(delivery_order_details['DO1']['sales_order'])
# print(delivery_order_details['DO1']['stock_moves'])

temp = {'SO2': {'CustomerKey': 'cust_2',
                                'order_line': [{'ProductKey': 'PRD3', 'UnitPrice': 10, 'Quantity': 1, 'SubTotal': 10, 'State': 'Draff'},
                                {'ProductKey': 'PRD3', 'UnitPrice': 15, 'Quantity': 1, 'SubTotal': 15, 'State': 'Draff'}]},
                                'OrderDate': '2021-12-4', 'State': 'Draft', 'OrderTotalAmount': 50}

# {'CustomerKey': 'cust_1', 'order_line': [{'product_sku': 'PRD1', 'unit_price': 10, 'quantity': 1, 'sub_total': 10, 'state': 'Draff'}]}
# sales_order_details.update(temp)

# customer_details = {'cust_1':{'name':'TUSHAL','email':'T@G.COM','phone':'8849999698'}}
# customer_address_details = {'cust_1':{'address1':'A1','address2':'A2','city':'RJ','state':'GJ','country':'I','zipcode':'36'}}
#
# print(sales_order_details)
# print(sales_order_details['SO1']['CustomerKey'])
# print(customer_details[sales_order_details['SO1']['CustomerKey']]['name'])
# print(customer_address_details[sales_order_details['SO1']['CustomerKey']]['address1'])
#
# print("\n{:<5} {:<20} {:<5} {:<2} ".format('Order No : ', list(sales_order_details)[0] , 'Order Date : ', sales_order_details['OrderDate']))
# print("{:<5} {:<20}".format('Order Status : ', sales_order_details['State']))
# print("{:<5} {:<20}{:<15}".format('Customer :', sales_order_details['SO1']['CustomerKey']+','+
#                             customer_details[sales_order_details['SO1']['CustomerKey']]['name'],
#                             customer_address_details[sales_order_details['SO1']['CustomerKey']]['address1']))

# print('S.no','\t','Product','\n','Unit','\t','Price')
# print(sales_order_details['SO1']['OrderLine'])
# for i in sales_order_details['SO1']['OrderLine']:
#     i['State'] = 'C'
#     print(i['State'])
# print(sales_order_details['SO1']['OrderLine'])

# print(len(sales_order_details))
# print(sales_order_details['State'])

# for k, v in sales_order_details.items():
#     print("{:<12} {:<1} {:<12} {:<2} {:<10}".format(k, '|', v['ProductName'], '|',
#                                                     sales_order_details.get(k)))

# class A:
#     def method_a(self):
#         print('Called method of Class A')
#
# class B:
#     def __init__(self):
#         self.customer_details = {}
#
#     def method_b(self):
#         print('Called method of Class B')
#
#     def display_cutomer_details(self):
#         # BEGIN display table view of cutomer details
#         print("\n{:<6} {:<1} {:<14} {:<2} {:<16} {:<2} {:<10}".format('Key', '|', 'Name', '|', 'Email', '|', 'Phone'))
#         for k, v in self.customer_details.items():
#             print("{:<6} {:<1} {:<12} {:<2} {:<10} {:<2} {:<10}".format(k, '|', v['CustomerName'], '|',
#                                                                         v['CustomerEmail'], '|', v['CustomerPhone']))
#         # END display table view of cutomer details
#
# class C(A, B):
#     def method_c(self):
#         self.method_a()
#         self.method_b()
#         print('Called method of Class C')
#
#     def method_d(self):
#         self.method_a()
#         self.method_b()
#         self.display_cutomer_details()
#
# obj_c = C()
#
# print(obj_c.method_d())


import datetime
#
# product_dictionary = {}
# product_dictionary['PRD1'] =  {'price':400,'qty':0}
# product_dictionary['PRD2'] =  {'price':500,'qty':15}
# # product_dictionary['PRD3'] =  {'price':500,'qty':15}
#
# # new_product_id = 'PRD'
# # if len(product_dictionary) != 0:
# #     last_key = list(product_dictionary.items())[-1][0]
# #     new_product_id += str(int(last_key[-1]) + 1)
# #     print(new_product_id)
# # else:
# #     new_product_id += '1'
# #     print(new_product_id)
# #
# #

# print(product_stock_details.get('PRD0'))
#
# temp_customer_key_details = \
# {'CustomerKey': 'cust_1', 'OrderLine': [{'ProductKey': 'PRD1'}, {'UnitPrice': 10}, {'Quantity': 5}, {'SubTotal': 50}, {'State': 'Draff'}]}
#
# print('001')
# print(temp_customer_key_details)

# # print(sum(int(item['SubTotal']) for item in temp_customer_key_details['OrderLine']))
# for item in temp_customer_key_details['OrderLine']:
#     print(item)

# print(product_details['PRD2'].get('ProductUnitPrice'))
# # print(product_stock_details)
# #
# # print("\n{:<12} {:<1} {:<12} {:<2} {:<10}".format('Product Key', '|','Product Name', '|', 'Quantity'))
# # for k, v in product_details.items():
# #     print("{:<12} {:<1} {:<12} {:<2} {:<10}".format(k,'|', v['ProductName'], '|', product_stock_details.get(k)))
# #
# # customer_details = {'cust_1' : {'CustomerName':'Tushal Nimavat','CustomerEmail':'tushal@gmail.com','CustomerPhone':'8849999698'}}
# # print(customer_details)
# #
# # print("\n{:<6} {:<1} {:<14} {:<2} {:<16} {:<2} {:<10}".format('Key', '|','Name', '|', 'Email','|', 'Phone'))
# # for k, v in customer_details.items():
# #     print("{:<6} {:<1} {:<12} {:<2} {:<10} {:<2} {:<10}".format(k,'|', v['CustomerName'], '|', v['CustomerEmail'],'|', v['CustomerPhone']))
# #
# temp_customer_key_details = {'CustomerKey': 'cust_1'}
# print(temp_customer_key_details)
# print(temp_customer_key_details.get('OrderLine'))
# temp_customer_key_details.update({'OrderLine':[{'ProductKey':'PRD1','SubTotal': str(datetime.date.today())}]})
# print(temp_customer_key_details)
# print(datetime.date.today())
# temp_customer_key_details['OrderLine'].append({'ProductKey':'PRD2','SubTotal':20})
# print(temp_customer_key_details)
# print(temp_customer_key_details['OrderLine'])
# print(sum(item['SubTotal'] for item in temp_customer_key_details['OrderLine']))
#
# import  datetime
# print(datetime.date.today())
#
# # product_key = input("\nEnter Product Key : ")
#
# # print(product_stock_details.get('PRD3'))
# #
# # product_stock_details1 = {'PRD3':10}
# # print(product_stock_details1.get('PRD3'))
# # product_stock_details1['PRD3'] = product_stock_details1.get('PRD3') + 15
# # print(product_stock_details1.get('PRD3'))
#
#
# # product_id = 'PRD1'
# # last_char_pid = int(product_id[-1]) + 1
# # print(last_char_pid)
# # print('new_product_id is ',new_product_id+str(last_char_pid))
#
# #
# # remove_index_list = []
# # remove_index_list.append(1)
# #
# # for i in remove_index_list:
# #     print(i)
# #
# # # for key, value in dict(product_dictionary).items():
# #     # print(key)
# #     # if any(i == 0 for i in value.values()):
# #     #     del product_dictionary[key]
# #
# # print(product_dictionary)
# #
# # #product_dictionary[1]["qty"] = 200
# #
# # # temp_price = 0
# # # temp_qty = 0
# # # for i, j in product_dictionary.items():
# # #     print(i)
# #
# # #print(product_dictionary)
# # #print(temp_price, temp_qty)
# # #print(product_dictionary[1].get('qty'))
# # #print(abs(product_dictionary[1].get('qty') - 10))
# # #print(abs(product_dictionary[1].get('qty') - 15))
# #
# # #product_dictionary.pop(1)
# #
# #
# # #print(product_dictionary)
# #
# # #from functools import reduce
# # #_sum = reduce((lambda x, y: x + y), product_dictionary.values())
# # #print('Total', _sum)
# #
# #
# #
# # # print(product_dictionary)
# #
# # # county_names = {'USA': 'United States of America','AU':'Astronomical Unit','ES':'Enterprise Solution',
# # #                 'DE':'DE','UK':'The United Kingdom','IT':'IT'}
# # # print(county_names['UK'])
#
#
# # import xml.etree.ElementTree as ET
# # XMLexample_stored_in_a_string ='''<?xml version ="1.0"?>
# # <States>
# # 	<state name ="TELANGANA">
# # 		<rank>1</rank>
# # 		<neighbor name ="ANDHRA" language ="Telugu"/>
# # 		<neighbor name ="KARNATAKA" language ="Kannada"/>
# # 	</state>
# # 	<state name ="GUJARAT">
# # 		<rank>2</rank>
# # 		<neighbor name ="RAJASTHAN" direction ="N"/>
# # 		<neighbor name ="MADHYA PRADESH" direction ="E"/>
# # 	</state>
# # 	<state name ="KERALA">
# # 		<rank>3</rank>
# # 		<neighbor name ="TAMILNADU" direction ="S" language ="Tamil"/>
# # 	</state>
# # </States>
# # '''
# # # parsing from the string.
# # root = ET.fromstring(XMLexample_stored_in_a_string)
# # # printing attributes of the root tags 'neighbor'.
# # for neighbor in root.iter('neighbor'):
# # 	print(neighbor.attrib)
# # # finding the state tag and their child attributes.
# # for state in root.findall('state'):
# # 	rank = state.find('rank').text
# # 	name = state.get('name')
# # 	print(name, rank)
#
#
