
class Product:
    def __init__(self, name, price, image, manufacturer, type, serial_number, barcode, size, shelf, comps):
        self.name = name
        self.price = price
        self.image = image
        self.manufacturer = manufacturer
        self.type = type
        self.number = serial_number
        self.barcode = barcode
        self.size = size
        self.status = None
        self.shelf = shelf
        self.comps = comps

    def get_info(self):
        return "Name: {0} Product# {1} ${2}".format(self.name, self.number, self.price)

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status


class Holder:
    def __init__(self, number, maxitem, status):
        self.number = number
        self.maxitem = maxitem
        self.hold = []
        self.status = status

    def set_status(self, status):
        self.status = status

    def place_item(self, item):
        print("Abc")
        self.hold.append(item)
        print(self.hold)

class Compartment(Holder):
    def __init__(self, number, maxitem, status, location):
        super().__init__(number, maxitem, status)
        self.location = location

    def create_shelf(self):
        for i in range(self.maxitem):
            self.hold.append(Shelf(i, 10, self.number, "comp"))

class Order:
    pass

class Shelf(Holder):
    def __init__(self, number, maxitem, comp, status):
        super().__init__(number, maxitem, status)
        self.comp = comp

    def scan_out(self, item):
        self.hold.remove(item)


class Bin(Holder):
    def __init__(self, number, maxitem, status):
        super().__init__(number, maxitem, status)

class Box(Holder):
    def __init__(self, barcode, address, number, maxitem, status):
        super().__init__(number, maxitem, status)
        self.barcode = barcode
        self.address = address

    def get_info(self):
        return "box number {0} with {1} items".format(self.number, len(self.hold))


class Warehouse:
    def get_shelf(self, shelf, comp):
        return True
        print((comp in self.comps))
        if comp in self.comps and shelf in comp:
            print("hello")
            shelf.status = "place"
            return True
        print("hi!")
        return False

    def __init__(self, name):
        self.name = name
        self.comps = []
        self.boxes = []

    def set_comps(self, nums):
        for i in range(nums):
            c = Compartment(i, 10, None, i)
            c.create_shelf()
            self.comps.append(c)

    def scan_product(self, product):
        pass

    # detail change
    def place_into_shelf(self, product):
        if self.get_shelf(product.shelf, product.comps):
            print("hello!")
            product.shelf.place_item(product)
            product.shelf.status = "comp"
            product.set_status("shelf")

    def scan_out(self, product):
        product.shelf.scan_out(product)
        product.set_status("worker")

    def abcd(self):
        for i in self.comps:
            for j in i.hold:
                print(j.hold)

    # def add_product(self, products):
    #     flag = False
    #     if len(self.warehouse) > 0:
    #         for b in self.warehouse:
    #             if b.number == products.number:
    #                 flag = True
    #
    #     if not flag:
    #         self.warehouse.append(products)
    #         return "#" + products.number + " into the warehouse"
    #     else:
    #         return "Already Exist"


if __name__ == "__main__":
    amazon = Warehouse("Amazon")
    amazon.set_comps(1)
    p = Product(1,1,1,1,1,1,1,1,amazon.comps[0],amazon.comps[0].hold[1])
    amazon.place_into_shelf(p)
    print(amazon.comps[0].hold[1].hold)

