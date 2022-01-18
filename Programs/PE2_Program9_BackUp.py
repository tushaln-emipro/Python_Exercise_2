"""
    Program 9 from Python Exercise 2
"""
import datetime


class ProductManagement:

    def __init__(self):
        self.product_details = {}
        self.product_stock_details = {}

    def manage_product(self):
        product_vals = self.prepare_product()
        self.create_product(product_vals)

    def prepare_product(self):
        # This method prepare temporarily product dict() and return its.
        product_name = input("Enter Product Name : ")
        product_unit_price = input("Enter Product Unit Price : ")
        product_cost_price = input("Enter Product Cost Price : ")
        product_stock = input("Enter Product Stock : ")
        prepare_product_dict = {'ProductName': product_name, 'ProductUnitPrice': int(product_unit_price),
                                'ProductCostPrice': int(product_cost_price), 'ProductStock': int(product_stock)}
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
        self.product_details.update({new_product_id: product_vals})
        self.product_stock_details.update({new_product_id: product_vals['ProductStock']})
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
            print("{:<12} {:<1} {:<12} {:<2} {:<10}".format(k, '|', v['ProductName'], '|',
                                                            self.product_stock_details.get(k)))
        # END display table view of products details

    def ask_for_productkey(self):
        self.display_product_details()
        product_key = input("\nEnter Product Key : ")
        return product_key

    def want_to_retry_exit(self, flaf):
        num = ''
        while num != '0':
            if flaf == 0: print("\n1. You enter wrong Product Key. Do you want to retry?")
            if flaf == 1: print("\n1. Stock Updated Successfully. Do you want to continue?")
            print("2. Enter 0 to Exit.")
            num = input("\nWhat would you like to do? ")
            if num == '1':
                self.update_product_stock()
            elif num == '0':
                break


class CustomerManagement:

    def __init__(self):
        self.customer_details = {}
        self.customer_address_details = {}

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
        customer_state = input("Enter Customer State : ")
        customer_country = input("Enter Customer Country : ")
        customer_zipcode = input("Enter Customer ZipCode : ")

        customer_details_dict = {'CustomerName': customer_name, 'CustomerEmail': customer_email,
                                 'CustomerPhone': customer_phone, 'CustomerAddress1': customer_address1,
                                 'CustomerAddress2': customer_address2, 'CustomerCity': customer_city,
                                 'CustomerState': customer_state, 'CustomerCountry': customer_country,
                                 'CustomerZipCode': customer_zipcode}
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
            'CustomerAddress1': customer_vals['CustomerAddress1'], 'CustomerAddress2': customer_vals['CustomerAddress2'],
            'CustomerCity': customer_vals['CustomerCity'], 'CustomerState': customer_vals['CustomerState'],
            'CustomerCountry': customer_vals['CustomerCountry'], 'CustomerZipCode': customer_vals['CustomerZipCode']}})
        # END Finally Add Customer In Main dict()

        return  new_customer_id

    def display_cutomer_details(self):
        # BEGIN display table view of cutomer details
        print("\n{:<6} {:<1} {:<14} {:<2} {:<16} {:<2} {:<10}".format('Key', '|', 'Name', '|', 'Email', '|', 'Phone'))
        for k, v in self.customer_details.items():
            print("{:<6} {:<1} {:<14} {:<2} {:<16} {:<2} {:<10}".format(k, '|', v['CustomerName'], '|',
                                                                        v['CustomerEmail'], '|', v['CustomerPhone']))
        # END display table view of cutomer details


class SalesOrder(CustomerManagement, ProductManagement):

    def __init__(self):
        CustomerManagement.__init__(self)
        self.sales_order_details = {}
        self.temp_customer_key_details = {}

    def generate_sales_order(self):
        self.create_sales_order()

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
                                         'OrderDate': datetime.date.today(), 'State': 'Draft',
                                         'OrderTotalAmount': sum(item['SubTotal'] for item
                                                                 in self.temp_customer_key_details['OrderLine'])})
        # END Finally Generated Sala Order

        return  new_so_id

    def prepare_sales_order(self):
        get_cust_key = self.ask_for_cust_key()
        self.temp_customer_key_details = {}
        print(customer_management.customer_details) # doute
        if self.customer_details.get(get_cust_key) == None:
            self.customer_want_to_retry_exit(0)
        else:
            self.temp_customer_key_details = {'CustomerKey': get_cust_key}

        if len(self.temp_customer_key_details) != 0:
            self.ask_add_product()
        else:
            print('Order can not be generated because Custormer detail not enter')

    def create_sales_order(self, sales_vals):
        print(sales_vals)

    def ask_for_cust_key(self):
        customer_management.display_cutomer_details()
        cust_key = input("\nEnter Customer Key : ")
        return cust_key

    def customer_want_to_retry_exit(self, flaf):
        num = ''
        while num != '0':
            if flaf == 0: print("\n1. You enter wrong Customer Key. Do you want to retry?")
            if flaf == 1:
                print("\n1. Customer Added Successfully.")
                break

            print("2. Enter 0 to Exit.")
            num = input("\nWhat would you like to do? ")
            if num == '1':
                self.prepare_sales_order()
            elif num == '0':
                break

    def ask_add_product(self):
        choice_num = ''
        while choice_num != '0':
            product_management.display_product_details()
            choice_num = input("\n 1. Do you want to add product?")
            if choice_num == '1':
                get_product_key = product_management.ask_for_productkey()
                num_qty = input("Enter Number of Quantity")
                if self.product_stock_details.get(get_product_key):
                    print('You enter wrong Product Key.')
                else:
                    if self.temp_customer_key_details.get('OrderLine'):
                        self.temp_customer_key_details.update({'OrderLine': [
                            {'ProductKey': get_product_key},
                            {'UnitPrice': int(self.product_details[get_product_key].get('ProductUnitPrice'))},
                            {'Quantity': int(num_qty)},
                            {'SubTotal': int(self.product_details[get_product_key].get('ProductUnitPrice') * num_qty)},
                            {'State': 'Draff'}
                        ]})
                    else:
                        self.temp_customer_key_details['OrderLine'].append(
                            {'ProductKey': get_product_key},
                            {'UnitPrice': int(self.product_details[get_product_key].get('ProductUnitPrice'))},
                            {'Quantity': int(num_qty)},
                            {'SubTotal': int(self.product_details[get_product_key].get('ProductUnitPrice') * num_qty)},
                            {'State': 'Draff'})
            else:
                break

        self.generate_sales_order()


product_management = ProductManagement()
customer_management = CustomerManagement()
sales_order = SalesOrder()
choice = ''

while choice != '0':

    print("\n[1] Add Product.")
    print("[2] Update Product.")
    print("[3] Show Product Details")
    print("[4] Add Customer Details")
    print("[5] Show Customer Details")
    print("[6] Generate Sales Order")
    print("[0] Enter 0 to Exit.")

    choice = input("\nWhat would you like to do?")
    if choice == '1':
        product_management.manage_product()
    if choice == '2':
        product_management.update_product_stock()
    if choice == '3':
        product_management.display_product_details()
    if choice == '4':
        customer_management.manage_customer()
    if choice == '5':
        customer_management.display_cutomer_details()
    if choice == '6':
        sales_order.prepare_sales_order()
    elif choice == '0':
        break

