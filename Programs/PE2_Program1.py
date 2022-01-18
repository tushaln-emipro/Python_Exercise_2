"""
    Program 1
"""


class Manufacturing:
    def __init__(self, rawmaterial, ratio, actualproduct):
        self.raw_material_quantity = 0
        self.actual_product_quantity = 0
        self.raw_material = rawmaterial
        self.ratio = ratio
        self.actual_product = actualproduct

    def purchase_raw_material(self, qty):
        self.raw_material_quantity += + int(qty)
        print("Purchased successfully")

    def produce(self, qty):
        if self.raw_material_quantity >= int(qty) * self.ratio:
            self.actual_product_quantity += int(qty)
            self.raw_material_quantity += - (int(qty) * self.ratio)
            print(qty, "produced successfully")
        else:
            print("Not enough raw material available to produce the product, please do the purchase number of ",
                  (int(qty) * self.ratio) - self.raw_material_quantity)

    def display_raw_material_stock(self):
        print("Raw Material Quantity is ", self.raw_material_quantity)

    def display_final_product_stock(self):
        print('Actual Product Quantity is ', self.actual_product_quantity)

    def scrapping_raw_material(self):
        self.raw_material_quantity = 0
        print('After scrapping raw material ', self.raw_material_quantity)

    def scrapping_actual_product(self):
        self.actual_product_quantity = 0
        print('After scrapping actual product quantity', self.actual_product_quantity)


def displaymenu(flag):
    print("\n[1] Enter 1 to Purchase Raw Material Product.")
    print("[2] Enter 2 Manufacture Finish Product.")
    print("[3] Enter 3 to Show Raw Material Quantity.")
    print("[4] Enter 4 to Show Actual Product Quantity.")
    print("[5] Enter 0 to Exit.")
    if flag == 1:
        print("[6] Enter 6 to scrapping the raw material product.")
        print("[7] Enter 7 to scrapping the actual product.")


manufacturing = Manufacturing('2 wheels', 2, 'bicycle')
print("Welcome")


def main(n):
    choice = ''
    while choice != '0':
        displaymenu(n)
        choice = input("\nWhat would you like to do? ")

        if choice == '1':
            raw_qty = input("Enter number of Qty for ")
            manufacturing.purchase_raw_material(raw_qty)
        elif choice == '2':
            product_qty = input("Enter no of qty to be produced for actual product ")
            manufacturing.produce(product_qty)
        elif choice == '3':
            manufacturing.display_raw_material_stock()
        elif choice == '4':
            manufacturing.display_final_product_stock()
        elif choice == '0':
            break
        elif choice == '6' and n == 1:
            # from PE2_Program2 import scrapping
            # scrapping.scrapping_raw_material() from PE2_Program2 import scrapping scrapping.scrapping_raw_material()
            manufacturing.scrapping_raw_material()
        elif choice == '7' and n == 1:
            # from PE2_Program2 import scrapping
            # scrapping.scrapping_actual_product() from PE2_Program2 import scrapping scrapping.scrapping_actual_product()
            manufacturing.scrapping_actual_product()

# main(0)
