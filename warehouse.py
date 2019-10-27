import sys

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class Product:
    def __init__(self, name, price, image, manufacturer, type, itemid, barcode, size):
        self.name = name
        self.price = price
        self.image = image
        self.manufacturer = manufacturer
        self.type = type
        self.itemid = itemid
        self.barcode = barcode
        self.size = size
        self.status = None

    def __repr__(self):
        return self.get_info()

    def get_info(self):
        return "Name: {0} Product# {1} ${2}".format(self.name, self.itemid, self.price)

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

class Order:
    pass

class Shelf:
    shelfs = []
    def __init__(self, shelfid):
        self.shelfid = shelfid
        self.comp = {"A": [], "B": []}
        Shelf.shelfs.append(self)

    def scan_in(self, item, compartment):
        self.comp[compartment].append(item)

    def scan_out(self, item, box):
        for c in self.comp:
            if item in self.comp[c]:
                self.comp[c].remove(item)
                box.put_in(item)
                item.set_status("Box#: {0}".format(box.boxid))
                break

    def show_comp(self, compartment):
        return self.comp[compartment]

class Trolly:
    def __init__(self, trollyid):
        self.trollyid = trollyid
        self.items = []

    def scan_onto(self, item):
        self.items.append(item)

    def scan_out(self, item, shelfid, compartment):
        self.items.remove(item)
        for s in Shelf.shelfs:
            if s.shelfid == shelfid:
                s.scan_in(item, compartment)
                item.set_status("Shelf#: {0}; Compartment#: {1}.".format(shelfid, compartment))

class Box:
    def __init__(self, boxid, info):
        self.boxid = boxid
        self.info = info
        self.items = []

    def get_info(self):
        return "box number {0} with {1} items".format(self.boxid, len(self.items))

    def put_in(self, item):
        self.items.append(item)


# if __name__ == "__main__":
#     s1 = Shelf(1)
#     t1 = Trolly(1)
#     p = Product(1,1,1,1,1,123,1,1)
#
#     t1.scan_onto(p)
#     print(t1.items)
#     t1.scan_out(p, 1, "A")
#     print(s1.comp)
#     print(t1.items)
#     print(p.get_status())
#     print(s1.show_comp("A"))
#     print()
#     b1 = Box(1,"asdf")
#     s1.scan_out(p, b1)
#     print(s1.comp)
#     print(p.get_status())
#     print(b1.items)
class MainPage2(QDialog):
    def __init__(self):
        super(MainPage2, self).__init__()
        loadUi("test.ui", self)


class MainPage(QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi("scan_in_shelf.ui", self)
        self.okButton.clicked.connect(self.asdf)
        self.backButton.clicked.connect(self.new)

    def asdf(self):
        shelfid = self.shelfid.toPlainText()
        compartment = self.compartment.toPlainText()
        t1.scan_out(p, shelfid, compartment)

    def new(self):
        widget = MainPage2()
        widget.exec_()


if __name__ == "__main__":
    s1 = Shelf(1)
    t1 = Trolly(1)
    p = Product(1, 1, 1, 1, 1, 123, 1, 1)

    t1.scan_onto(p)
    #    print(t1.items)
    #    t1.scan_out(p, 1, "A")
    #    print(s1.comp)
    #    print(t1.items)
    #    print(p.get_status())
    #    print(s1.show_comp("A"))
    #    print()
    #    b1 = Box(1,"asdf")
    #    s1.scan_out(p, b1)
    #    print(s1.comp)
    #    print(p.get_status())
    #    print(b1.items)

    app = QApplication(sys.argv)
    widget = MainPage()
    widget.show()
    sys.exit(app.exec_())


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




