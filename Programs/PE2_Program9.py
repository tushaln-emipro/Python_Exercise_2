"""
    Program 9 from Python Exercise 2
"""
import datetime


class SalesManagement:

    def __init__(self):
        self.product_details = {}
        self.product_stock_details = {}
        self.customer_details = {}
        self.customer_address_details = {}
        self.sales_order_details = {}
        self.temp_customer_key_details = {}

    # BEGIN PRODUCT MANAGEMENT

    def manage_product(self):
        product_vals = self.prepare_product()
        self.create_product(product_vals)

    def prepare_product(self):
        # This method prepare temporarily product dict() and return its.
        product_name = input("Enter Product Name : ")
        product_unit_price = input("Enter Product Unit Price : ")
        product_cost_price = input("Enter Product Cost Price : ")
        product_stock = input("Enter Product Stock : ")
        prepare_product_dict = {'product_name': product_name, 'product_unit_price': int(product_unit_price),
                                'product_cost_price': int(product_cost_price), 'product_stock': int(product_stock)}
        return prepare_product_dict

    def create_product(self, product_vals):

        # BEGIN NEW GENERATE PRODUCT ID
        new_product_id = 'PRD'
        if len(self.product_details) != 0:
            last_key = list(self.product_details.items())[-1][0]
            new_product_id += str(int(last_key[-1]) + 1)
        else:
            new_product_id += '1'
        # END NEW GENERATE PRODUCT ID

        # BEGIN Finally Add Product In Main dict()
        self.product_stock_details.update({new_product_id: product_vals['product_stock']})
        self.product_details.pop('product_stock', None)
        self.product_details.update({new_product_id: product_vals})
        # END Finally Add Product In Main dict()

        return new_product_id

    def update_product_stock(self):
        get_productkey = self.ask_for_productkey()
        if self.product_stock_details.get(get_productkey) == None:
            self.want_to_retry_exit(0)
        else:
            stock_qty = input("\nPlease Enter Stock Quantity : ")
            self.product_stock_details[get_productkey] += int(stock_qty)
            self.want_to_retry_exit(1)

    def display_product_details(self):
        # BEGIN display table view of products details
        print("\n{:<12} {:<1} {:<12} {:<2} {:<10}".format('Product Key', '|', 'Product Name', '|', 'Quantity'))
        for k, v in self.product_details.items():
            print("{:<12} {:<1} {:<12} {:<2} {:<10}".format(k, '|', v['product_name'], '|',
                                                            self.product_stock_details.get(k)))
        # END display table view of products details

    def ask_for_productkey(self):
        self.display_product_details()
        product_key = input("\nEnter Product Key : ")
        return product_key

    def want_to_retry_exit(self, flaf):
        num = ''
        while num != '0':
            if flaf == 0:
                print("\n1. You enter wrong Product Key. Do you want to retry?")
            if flaf == 1:
                print("\n1. Stock Updated Successfully. Do you want to continue?")
                break

            print("2. Enter 0 to Exit.")
            num = input("\nWhat would you like to do? ")
            if num == '1':
                self.update_product_stock()
            elif num == '0':
                break

    # END PRODUCT MANAGEMENT

    # BEGIN CUSTOMER MANAGEMENT

    def manage_customer(self):
        customer_vals = self.prepare_customer()
        self.create_cutomer(customer_vals)

    def prepare_customer(self):
        # This method prepare temporarily customer dict() and return its.
        customer_name = input("Enter Customer Name : ")
        customer_email = input("Enter Customer Email : ")
        customer_phone = input("Enter Customer Phone : ")
        customer_address1 = input("Enter Customer Address 1 : ")
        customer_address2 = input("Enter Customer Address 2 : ")
        customer_city = input("Enter Customer City : ")
        customer_state = input("Enter Customer state : ")
        customer_country = input("Enter Customer Country : ")
        customer_zipcode = input("Enter Customer ZipCode : ")

        customer_details_dict = {'customer_name': customer_name, 'customer_email': customer_email,
                                 'customer_phone': customer_phone, 'customer_address1': customer_address1,
                                 'customer_address2': customer_address2, 'customer_city': customer_city,
                                 'customer_state': customer_state, 'customer_country': customer_country,
                                 'customer_zipcode': customer_zipcode}
        return customer_details_dict

    def create_cutomer(self, customer_vals):
        # BEGIN NEW GENERATE Customer ID
        new_customer_id = 'cust_'
        if len(self.customer_details) != 0:
            last_key = list(self.customer_details.items())[-1][0]
            new_customer_id += str(int(last_key[-1]) + 1)
        else:
            new_customer_id += '1'
        # END NEW GENERATE Customer ID

        # BEGIN Finally Add Customer In Main dict()
        self.customer_details.update({new_customer_id: customer_vals})
        self.customer_address_details.update({new_customer_id: {
            'customer_address1': customer_vals['customer_address1'], 'customer_address2': customer_vals['customer_address2'],
            'customer_city': customer_vals['customer_city'], 'customer_state': customer_vals['customer_state'],
            'customer_country': customer_vals['customer_country'], 'customer_zipcode': customer_vals['customer_zipcode']}})
        # END Finally Add Customer In Main dict()

        return  new_customer_id

    def display_cutomer_details(self):
        # BEGIN display table view of cutomer details
        print("\n{:<6} {:<1} {:<14} {:<2} {:<16} {:<2} {:<10}".format('Key', '|', 'Name', '|', 'Email', '|', 'Phone'))
        for k, v in self.customer_details.items():
            print("{:<6} {:<1} {:<14} {:<2} {:<16} {:<2} {:<10}".format(k, '|', v['customer_name'], '|',
                                                                        v['customer_email'], '|', v['customer_phone']))
        # END display table view of cutomer details

    # END CUSTOMER MANAGEMENT

    # BEGIN SALES ORDER MANAGEMENT

    def manage_sale_order(self):
        self.prepare_sales_order()

    def create_sales_order(self):
        # BEGIN NEW GENERATE SALE ORDER
        new_so_id = 'SO'
        if len(self.sales_order_details) != 0:
            last_key = list(self.sales_order_details.items())[-1][0]
            new_so_id += str(int(last_key[-1]) + 1)
        else:
            new_so_id += '1'
        # END NEW GENERATE SALE ORDER

        # BEGIN Finally Generated Sala Order
        self.sales_order_details.update({new_so_id: self.temp_customer_key_details,
                                         'order_date': str(datetime.date.today()), 'state': 'Draft',
                                         'order_total_amount': sum(int(item['sub_total']) for item in self.temp_customer_key_details['order_line'])})
        # END Finally Generated Sala Order

        return  new_so_id

    def prepare_sales_order(self):
        get_cust_key = self.ask_for_cust_key()
        self.temp_customer_key_details = {}
        if self.customer_details.get(get_cust_key) == None:
            self.customer_want_to_retry_exit()
        else:
            self.temp_customer_key_details = {'CustomerKey': get_cust_key}

        if len(self.temp_customer_key_details) != 0:
            self.ask_add_product()
        else:
            print('Order can not be generated because Custormer detail not enter')

    def display_sales_order(self):
        if (len(self.sales_order_details) != 0):
            print(self.sales_order_details)
        else:
            print('No Records')

    def ask_for_cust_key(self):
        self.display_cutomer_details()
        cust_key = input("\nEnter Customer Key : ")
        return cust_key

    def customer_want_to_retry_exit(self):
        num = ''
        while num != '0':
            print("\n1. You enter wrong Customer Key. Do you want to retry?")
            print("2. Enter 0 to Exit.")
            num = input("\nWhat would you like to do? ")
            if num == '1':
                self.prepare_sales_order()
            elif num == '0':
                break

    def ask_add_product(self):
        choice_num = ''
        while choice_num != '0':
            choice_num = input("\n 1. Do you want to add product?")
            if choice_num == '1':
                get_product_key = self.ask_for_productkey()
                if self.product_details.get(get_product_key) == None:
                    print('You enter wrong Product Key.')
                else:
                    num_qty = input("Enter Number of Quantity")
                    temp_dict = {'product_sku': get_product_key,
                            'unit_price': int(self.product_details[get_product_key].get('product_unit_price')),
                            'quantity': int(num_qty),
                            'sub_total': int(self.product_details[get_product_key].get('product_unit_price')) * int(num_qty),
                            'state': 'Draff'}
                    if self.temp_customer_key_details.get('order_line') == None:
                        self.temp_customer_key_details.update({'order_line': [temp_dict]})
                    else:
                        self.temp_customer_key_details['order_line'].append(temp_dict)
            elif choice_num == '0':
                break

        if "order_line" in self.temp_customer_key_details:
                self.create_sales_order()

    def confirm(self):
        if(len(self.sales_order_details) != 0):
            if self.sales_order_details['state'] == 'Cancel':
                print('Order already Cancel')
            else:
                self.sales_order_details['state'] = 'Confirm'
                for i in self.sales_order_details['SO1']['order_line']:
                    i['state'] = 'Confirm'
                print('Order Confirm Successfully')
        else:
            print('No Records')

    def done(self):
        if (len(self.sales_order_details) != 0):
            if self.sales_order_details['state'] == 'Cancel':
                print('Order already Cancel')
            else:
                self.sales_order_details['state'] = 'Done'
                for i in self.sales_order_details['SO1']['order_line']:
                    i['state'] = 'Done'
                print('Order Done Successfully')
        else:
            print('No Records')

    def cancel(self):
        if (len(self.sales_order_details) != 0):
            self.sales_order_details['state'] = 'Cancel'
            for i in self.sales_order_details['SO1']['order_line']:
                i['state'] = 'Cancel'
            print('Order Cancel Successfully')
        else:
            print('No Records')

    def draff(self):
        if (len(self.sales_order_details) != 0):
            if self.sales_order_details['state'] == 'Confirm':
                print('Order already Confirm')
            else:
                self.sales_order_details['state'] = 'Draff'
                for i in self.sales_order_details['SO1']['order_line']:
                    i['state'] = 'Draff'
                print('Order Draff Successfully')
        else:
            print('No Records')

    # END SALES ORDER MANAGEMENT


sales_management = SalesManagement()
choice = ''
while choice != '0':

    print("\n[1] Add Product.")
    print("[2] Update Product.")
    print("[3] Show Product Details")
    print("[4] Add Customer Details")
    print("[5] Show Customer Details")
    print("[6] Generate Sales Order")
    print("[7] Show Sales Order")
    print("[8] Change Order to Confirm")
    print("[9] Change Order to Done")
    print("[10] Change Order to Cancel")
    print("[11] Change Order to Draff")
    print("[0] Enter 0 to Exit.")

    choice = input("\nWhat would you like to do?")
    if choice == '1':
        sales_management.manage_product()
    if choice == '2':
        sales_management.update_product_stock()
    if choice == '3':
        sales_management.display_product_details()
    if choice == '4':
        sales_management.manage_customer()
    if choice == '5':
        sales_management.display_cutomer_details()
    if choice == '6':
        sales_management.manage_sale_order()
    if choice == '7':
        sales_management.display_sales_order()
    if choice == '8':
        sales_management.confirm()
    if choice == '9':
        sales_management.done()
    if choice == '10':
        sales_management.cancel()
    if choice == '11':
        sales_management.draff()
    elif choice == '0':
        break
