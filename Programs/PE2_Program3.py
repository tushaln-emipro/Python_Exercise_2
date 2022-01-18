"""
    Program 3 from Python Exercise 2
"""


class InventoryManagement:
    def __init__(self):
        self.product_quantity = 0

    def purchase_product(self, num_product):
        self.product_quantity += int(num_product)
        print("Purchased successfully")

    def sale_product(self, num_sale):
        if self.product_quantity >= int(num_sale):
            self.product_quantity += - int(num_sale)
            print(num_sale, "Sale successfully and available quantities is ", self.product_quantity)
        else:
            print("Not enough product quantities to sell")

    def display_product_quantity(self):
        print("Available Product Quantities is ", self.product_quantity)


inventory_management = InventoryManagement()
choice = ''
while choice != '0':

    print("\n[1] Enter 1 to Purchase Product.")
    print("[2] Enter 2 to Sale Product.")
    print("[3] Enter 3 to View Available Product Quantities.")
    print("[4] Enter 0 to Exit.")

    choice = input("\nWhat would you like to do? ")
    if choice == '1':
        product_qty = input("Enter number of Qty for ")
        inventory_management.purchase_product(product_qty)
    elif choice == '2':
        sale_qty = input("Enter no of qty to be sale ")
        inventory_management.sale_product(sale_qty)
    elif choice == '3':
        inventory_management.display_product_quantity()
    elif choice == '0':
        break
