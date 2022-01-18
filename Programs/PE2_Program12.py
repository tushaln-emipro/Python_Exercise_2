"""
    Program 12 from Python Exercise 2
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
        self.delivery_order_details = {}

    # BEGIN PRODUCT MANAGEMENT

    def manage_product(self):
        """ This method first call of general preparation of product and then pass to final creation product"""
        product_vals = self.prepare_product()
        self.create_product(product_vals)

    def prepare_product(self):
        """
            This method prepare temporarily dictionary of product.
            return the prepared temp dictionary
        """
        product_name = input("Enter Product Name : ")
        product_unit_price = input("Enter Product Unit Price : ")
        product_cost_price = input("Enter Product Cost Price : ")
        product_stock = input("Enter Product Stock : ")
        prepare_product_dict = {'product_name': product_name, 'product_unit_price': int(product_unit_price),
                                'product_cost_price': int(product_cost_price), 'product_stock': int(product_stock)}
        return prepare_product_dict

    def create_product(self, product_vals):
        """
        :param product_vals: In this get temp prepared prodoct
        :return: the generated new product id
        """

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
        """
        In this method is Addition of stock quantity as per given by product id
        :return: no any return
        """
        get_productkey = self.ask_for_productkey()
        if self.product_stock_details.get(get_productkey):
            self.want_to_retry_exit(0)
        else:
            stock_qty = input("\nPlease Enter Stock Quantity : ")
            self.product_stock_details[get_productkey] += int(stock_qty)
            self.want_to_retry_exit(1)

    def display_product_details(self):
        """
        display table view of products details
        :return: not any return
        """
        print("\n{:<12} {:<1} {:<12} {:<2} {:<10}".format('Product Key', '|', 'Product Name', '|', 'Quantity'))
        for k, v in self.product_details.items():
            print("{:<12} {:<1} {:<12} {:<2} {:<10}".format(k, '|', v['product_name'], '|',
                                                            self.product_stock_details.get(k)))

    def ask_for_productkey(self):
        """
        In this first display list of products and then after ask to Enter Product Key
        :return: entered product key
        """
        self.display_product_details()
        product_key = input("\nEnter Product Key : ")
        return product_key

    def want_to_retry_exit(self, flaf):
        """
        This method for call of Update product stock
        :param flaf: get zero or one for display first menu
        :return:not any return
        """
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
        """ This method first call of general preparation of customer and then pass to final creation customer"""
        customer_vals = self.prepare_customer()
        self.create_cutomer(customer_vals)

    def prepare_customer(self):
        """
            This method prepare temporarily dictionary of customer.
            return the prepared temp dictionary
        """
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
        """
               :param customer_vals: In this get temp prepared customer
               :return: the generated new customer id
        """

        # BEGIN NEW GENERATE Customer ID
        new_customer_id = 'cust_'
        if self.customer_details:
            last_key = list(self.customer_details.items())[-1][0]
            new_customer_id += str(int(last_key[-1]) + 1)
        else:
            new_customer_id += '1'
        # END NEW GENERATE Customer ID

        # BEGIN Finally Add Customer In Main dict()
        self.customer_details.update({new_customer_id: customer_vals})
        self.customer_address_details.update({new_customer_id: {
            'customer_address1': customer_vals['customer_address1'], 'customer_address2':
            customer_vals['customer_address2'], 'customer_city': customer_vals['customer_city'], 'customer_state':
            customer_vals['customer_state'], 'customer_country': customer_vals['customer_country'],
            'customer_zipcode': customer_vals['customer_zipcode']}})
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
        """
            This method first call of general preparation of sales orders
        :return:not any return
        """
        self.prepare_sales_order()

    def create_sales_order(self):
        """
        This method is generate new so id and then after add final sales order dictionary
        :return:generated new so id
        """
        # BEGIN NEW GENERATE SALE ORDER
        new_so_id = 'SO'
        if self.sales_order_details:
            last_key = list(self.sales_order_details.items())[-1][0]
            new_so_id += str(int(last_key[-1]) + 1)
        else:
            new_so_id += '1'
        # END NEW GENERATE SALE ORDER

        # BEGIN Finally Generated Sala Order
        self.sales_order_details.update({new_so_id: self.temp_customer_key_details})
        # END Finally Generated Sala Order

        return  new_so_id

    def prepare_sales_order(self):
        """
        this method is general prepared sale order as per customer and added products
        :return:not any return
        """
        get_cust_key = self.ask_for_cust_key()
        self.temp_customer_key_details = {}
        if self.customer_details.get(get_cust_key):
            self.customer_want_to_retry_exit()
        else:
            self.temp_customer_key_details = {'customer': get_cust_key}

        if len(self.temp_customer_key_details) != 0:
            self.ask_add_product()
        else:
            print('Order can not be generated because Custormer detail not enter')

    def display_sales_order(self):
        """
        display all sales orders in table view
        :return:not any return
        """
        if self.sales_order_details:
            for i in self.sales_order_details:
                print("\n{:<5} {:<10} {:<10} {:<10}".format('Sale Order NO : ', i, 'Customer :',
                                                            self.sales_order_details[i]['customer']))
                print("{:<10} {:<8} {:<10} {:<12} {:<12}".format('Product SKU |', 'Unit Price |', 'Quantity |',
                                                                 'Sub Total |', 'State |'))
                for j in self.sales_order_details[i]['order_line']:
                    print("{:<15} {:<12} {:<10} {:<10} {:<12}".format(j['product_sku'], j['unit_price'], j['quantity'],
                                                               j['sub_total'], j['state']))
        else:
            print('No Records')

    def ask_for_cust_key(self):
        """
        display all customers details and then ask for enter customer key and then final return typed key
        :return: type customer key
        """
        self.display_cutomer_details()
        cust_key = input("\nEnter Customer Key : ")
        return cust_key

    def customer_want_to_retry_exit(self):
        """
        this method first display menu for if type wrong customer key then after if type right key then go to
        general prepare sales orders method
        :return: not any return
        """
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
        """
        This method for ask to add product key
        if type right key entered then update temp dictionary
        make temp order as per product quantity and update sub total, state (default set Draft)
        :return:not any return
        """
        choice_num = ''
        while choice_num != '0':
            choice_num = input("\n 1. Do you want to add product? \n 0. Exit")
            if choice_num == '1':
                get_product_key = self.ask_for_productkey()
                if self.product_details.get(get_product_key):
                    print('You enter wrong Product Key.')
                else:
                    num_qty = input("Enter Number of Quantity")
                    temp_dict = {'product_sku': get_product_key,
                            'unit_price': int(self.product_details[get_product_key].get('product_unit_price')),
                            'quantity': int(num_qty),
                            'sub_total': int(self.product_details[get_product_key].get('product_unit_price')) * int(num_qty),
                            'state': 'Draft'}
                    if self.temp_customer_key_details.get('order_line'):
                        self.temp_customer_key_details.update({'order_line': [temp_dict]})
                    else:
                        self.temp_customer_key_details['order_line'].append(temp_dict)
                    self.temp_customer_key_details.update({'order_date': str(datetime.date.today())})
                    self.temp_customer_key_details.update({'state': 'Draft'})
                    self.temp_customer_key_details.update({'order_total_amount': sum(int(item['sub_total']) for item in
                                                 self.temp_customer_key_details['order_line'])})
            elif choice_num == '0':
                break

        if "order_line" in self.temp_customer_key_details:
                self.create_sales_order()

    def confirm(self):
        """
        this method is changed state to Confirm as per condition passing
        :return:not any return
        """
        if self.sales_order_details:
            get_so_key = self.ask_for_so_key()
            if self.sales_order_details.get(get_so_key):
                print('Sorry not SO key found. Please try again..')
            else:
                if self.sales_order_details[get_so_key]['state'] == 'Done':
                    print('This Order Is Delivered')
                    return False
                if self.sales_order_details[get_so_key]['state'] == 'Cancel':
                    print('Order already Cancel')
                else:
                    if self.delivery_order_details:
                        temp_do = self.get_dokey_by_sokey(get_so_key)
                        if temp_do == None:
                            self.final_confirm(get_so_key)
                            return  False
                        if self.delivery_order_details[temp_do]['state'] == 'Draft':
                            print(get_so_key, 'This order already in process')
                        else:
                            self.final_confirm(get_so_key)
                    else:
                        self.final_confirm(get_so_key)
        else:
            print('No Records')

    def final_confirm(self,so_num):
        """
        In this method is finally confirmed as per given so number
        :param so_num:the sale order number
        :return:not any return
        """
        self.sales_order_details[so_num]['state'] = 'Confirm'
        for i in self.sales_order_details[so_num]['order_line']:
            i['state'] = 'Confirm'
        self.create_delivery_order(so_num)
        print('Order Confirm Successfully')

    def cancel(self):
        """
        In this method change state to Cancel as per passing conditions
        :return:not any return
        """
        if self.sales_order_details:
            get_so_key = self.ask_for_so_key()
            if self.sales_order_details.get(get_so_key):
                print('Sorry not SO key found. Please try again..')
            else:
                if self.sales_order_details[get_so_key]['state'] == 'Confirm':
                    if self.delivery_order_details:
                        temp_do_num = self.get_dokey_by_sokey(get_so_key)
                        if self.delivery_order_details[temp_do_num]['state'] == 'Done':
                            print('Deliver Order Is Done')
                            return False
                        if self.delivery_order_details[temp_do_num]['state'] == 'Cancel':
                            self.final_cancel_sales_order(get_so_key)
                        else:
                            print('Cancel the delivery order first.')
                    else:
                        self.final_cancel_sales_order(get_so_key)
                else:
                    if self.sales_order_details[get_so_key]['state'] == 'Draft':
                        self.final_cancel_sales_order(get_so_key)
        else:
            print('No Records')

    def draft(self):
        """
        In this method change state to Draft as per passing conditions
        :return:not any return
        """
        if self.sales_order_details:
            get_so_key = self.ask_for_so_key()
            if self.sales_order_details.get(get_so_key):
                print('Sorry not SO key found. Please try again..')
            else:
                temp_do_num = self.get_dokey_by_sokey(get_so_key)
                if temp_do_num != None:
                    if self.sales_order_details[get_so_key]['state'] == 'Confirm':
                        if self.delivery_order_details[temp_do_num]['state'] == 'Draft':
                            print('First Cancel Delivery Order')
                            return False
                    if self.delivery_order_details[temp_do_num]['state'] == 'Done':
                        print('Delivery Order already Done')
                    if self.sales_order_details[get_so_key]['state'] == 'Cancel':
                        self.final_draft(get_so_key)
                else:
                    self.final_draft(get_so_key)
        else:
            print('No Records')

    def final_draft(self, so_key):
        """
        In this method finally changed state to Draft as per given so key
        :param so_key:get so key
        :return: not any return
        """
        self.sales_order_details[so_key]['state'] = 'Draft'
        for i in self.sales_order_details[so_key]['order_line']:
            i['state'] = 'Draft'
        print('Order Draft Successfully')

    def final_cancel_sales_order(self, so_num):
        """
        In this method final changed state to Cancel as per given so id
        :param so_num:get so id
        :return:not any return
        """
        self.sales_order_details[so_num]['state'] = 'Cancel'
        for i in self.sales_order_details[so_num]['order_line']:
            i['state'] = 'Cancel'
        print('Sales Order Cancel Successfully')

    def get_dokey_by_sokey(self, get_so_key):
        """
        In this method find DO id as per given so id
        :param get_so_key:get so id
        :return: DO id return
        """
        for i in self.delivery_order_details:
            if self.delivery_order_details[i]['sales_order'] == get_so_key:
                return i

    # END SALES ORDER MANAGEMENT

    # BEGIN DELIVERY ORDER MANAGEMENT

    def display_delivery_order(self):
        """
        Dispaly all details of Delivery Orders in table view
        :return:not any return
        """
        if self.delivery_order_details:
            for i in self.delivery_order_details:
                print("\n{:<5} {:<10} {:<10} {:<10}".format('DO No. : ', i, 'SO No. :',
                                                        self.delivery_order_details[i]['sales_order']))
                print("{:<10} {:<10} {:<12} ".format('Product Code |', 'Quantity |', 'State |'))
                for j in self.delivery_order_details[i]['stock_moves']:
                    print("{:<15} {:<8} {:<12}".format(j['product_code'], j['product_qty'], j['state']))
        else:
            print('No Records')

    def ask_for_so_key(self):
        """
            display all sales order details and then ask for enter SO key and then final return typed key
            :return: type SO key
        """
        self.display_sales_order()
        so_key = input("\nEnter SO Key : ")
        return so_key

    def ask_for_do_key(self):
        """
            display all delivery order details and then ask for enter DO key and then final return typed key
            :return: type DO key
        """
        self.display_delivery_order()
        do_key = input("\nEnter DO Key : ")
        return do_key

    def create_delivery_order(self, get_so_key):
        """
        In this method generate new do id and make delivery order as per so id
        :param get_so_key:get so key
        :return:not any return
        """
        # BEGIN NEW GENERATE delivery order
        new_do_id = 'DO'
        if len(self.delivery_order_details) != 0:
            last_key = list(self.delivery_order_details.items())[-1][0]
            new_do_id += str(int(last_key[-1]) + 1)
        else:
            new_do_id += '1'
        # END NEW GENERATE delivery order

        temp_stock_moves_list = []
        for i in self.sales_order_details[get_so_key]['order_line']:
            temp_stock_moves_list.append(
                {'product_code': i['product_sku'], 'product_qty': i['quantity'], 'state': 'Draft'})

        self.delivery_order_details.update({new_do_id: {'sales_order': get_so_key,
                                                        'customer_id': self.sales_order_details[get_so_key]['customer'],
                                                        'stock_moves': temp_stock_moves_list, 'state': 'Draft'}})

    def validate_delivery_order(self):
        """
        Changed state to Done of Delivery order as per given do id and also changed in sales order state and deduction
        of product quantity in final product stock dictionary
        :return:not any return
        """
        if self.delivery_order_details:
            get_do_key = self.ask_for_do_key()
            if self.delivery_order_details.get(get_do_key):
                print('Sorry not DO key found. Please try again..')
            else:
                temp_so_id = self.delivery_order_details[get_do_key]['sales_order']

                for key_stock_moves in self.delivery_order_details[get_do_key]['stock_moves']:
                    key_stock_moves['state'] = 'Done'
                self.delivery_order_details[get_do_key]['state'] = 'Done'

                for key_order_line in self.sales_order_details[temp_so_id]['order_line']:
                    if self.product_stock_details.get(key_order_line['product_sku']) != None:
                        self.product_stock_details[key_order_line['product_sku']] -= key_order_line['quantity']
                        key_order_line['state'] = 'Done'
                self.sales_order_details[temp_so_id]['state'] = 'Done'

                print('Delivery Order Validate Successfully')
        else:
            print('No Records')

    def cancel_delivery_order(self):
        """
        In this method Changed state to Cancel as per given DO id
        :return:not any return
        """
        if self.delivery_order_details:
            get_do_key = self.ask_for_do_key()
            if self.delivery_order_details.get(get_do_key):
                print('Sorry not DO key found. Please try again..')
            else:
                if self.delivery_order_details[get_do_key]['state'] == 'Done':
                    print('Delivery Order is already Done')
                else:
                    for key_stock_moves in self.delivery_order_details[get_do_key]['stock_moves']:
                        key_stock_moves['state'] = 'Cancel'
                    self.delivery_order_details[get_do_key]['state'] = 'Cancel'
                    print('Delivery Order Cancel Successfully')
        else:
            print('No Records')

    # END DELIVERY ORDER MANAGEMENT


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
    print("[9] Change Order to Cancel")
    print("[10] Change Order to Draft")
    print("[11] Validate Delivery Order")
    print("[12] Cancel Delivery Order")
    print("[13] Show Delivery Orders")
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
        sales_management.cancel()
    if choice == '10':
        sales_management.draft()
    if choice == '11':
        sales_management.validate_delivery_order()
    if choice == '12':
        sales_management.cancel_delivery_order()
    if choice == '13':
        sales_management.display_delivery_order()
    elif choice == '0':
        break
