"""
    Program 4 from Python Exercise 2
"""


class InventoryManagement:
    def __init__(self):
        self.dict_index = 0
        self.product_dictionary = {}


    def purchase_product(self, price, qty):
        self.dict_index += 1
        self.product_dictionary[self.dict_index] = {'price': price, 'qty': qty, 'subtotal': price*qty}
        print("Purchased successfully")

    def sale_product(self, num_sale):
        print("001", self.product_dictionary)
        total_qty = self.find_totals_qty()
        remove_index_list = []
        if total_qty >= num_sale:
            for i, j in self.product_dictionary.items():
                if self.product_dictionary[i].get('qty') > num_sale:
                    self.product_dictionary[i]["qty"] = self.product_dictionary[i]["qty"] - num_sale
                    self.product_dictionary[i]["subtotal"] = self.product_dictionary[i]["qty"] * self.product_dictionary[i]["price"]
                    break
                else:
                    num_sale -= self.product_dictionary[i]["qty"]
                    self.product_dictionary[i]["qty"] = 0
                    remove_index_list.append(i)
        else:
            print("Sorry, Available Product Quantities is ", total_qty)

        print("Saled Successfully And Now Available Product Quantities Is ", self.find_totals_qty())
        self.remove_index(remove_index_list)
        print("002", self.product_dictionary)

    def display_product_quantity(self):
        print("Available Product Quantities is ", self.find_totals_qty())

    def showvaluation(self):
        if bool(self.product_dictionary):
            temp_qty = 0
            temp_subtotal = 0
            for i, j in self.product_dictionary.items():
                for k, v in j.items():
                    if k == 'qty': temp_qty += v
                    if k == 'subtotal': temp_subtotal += v
            print('Valuation is ', temp_subtotal/temp_qty)
        else:
            print("Sorry, Available Product Quantities is ", self.find_totals_qty())

    def find_totals_qty(self):
        total = 0
        if bool(self.product_dictionary):
            for i, j in self.product_dictionary.items():
                    total += self.product_dictionary[i]["qty"]
        return total

    def remove_index(self,remove_index_list):
        for index in remove_index_list:
            del self.product_dictionary[index]
            # for key, value in dict(self.product_dictionary).items():
            #     if any(i == 0 for i in value.values()):
            #         del self.product_dictionary[key]


inventory_management = InventoryManagement()
choice = ''
while choice != '0':

    print("\n[1] Enter 1 to Purchase Product.")
    print("[2] Enter 2 to Sale Product.")
    print("[3] Enter 3 to View Available Product Quantities.")
    print("[4] Enter 4 to Show Valuation.")
    print("[5] Enter 0 to Exit.")

    choice = input("\nWhat would you like to do? ")
    if choice == '1':
        product_price, product_qty = input("Enter product price & Qty ").split()
        inventory_management.purchase_product(int(product_price), int(product_qty))
    elif choice == '2':
        sale_qty = input("Enter no of qty to be sale ")
        if int(sale_qty) != 0:
            inventory_management.sale_product(int(sale_qty))
        else:
            print("Please Enter Greater Thane Zero")
    elif choice == '3':
        inventory_management.display_product_quantity()
    elif choice == '4':
        inventory_management.showvaluation()
    elif choice == '0':
        break
