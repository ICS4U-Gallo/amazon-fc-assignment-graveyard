import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi




class Product:
     """
    Attrs:
         name(str): The product's name
         price(int): The product's price
         image: The product's image
         manufacturer(str): The product's manuacturer
         type: product type
         itemid(int): The product identification
         barcode(int): The product's barcode
         size(str): The product size
    """
    def __init__(self, name, price, image, manufacturer, type, itemid, barcode, size):
        """create a product object
        Args:
            name: the name of the product
            price: the price of the product
            image: the image of the product
            manufacturer: the manufacturer of the product
            type: product type
            itemid: the product identification
            barcode: the product barcode
            size: the product size
        """
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
    """
    Attrs:
         order_id(int): order identification
         date_created(str): Date manufactured
         date_shipped(str): 
         customer_name(str): Customer's name
         customer_id(str): Customer's identification
         status(str):
         shipping_id(int): Shipping identification
    """
    num_order = 0

    def __init__(self, order_id: int, itemid: int, date_created: str, date_shipped: str, customer_name: str, customer_id: str, status: str, shipping_id: int):
        """Create an order object
        Args:
            order_id: order identification
            item_id: product identification
            date_created: date of production
            date_shipped: date product was shipped
            customer_name: the name of the customer
            customer_id: the id of the customer
            status: status of order
            shipping_id: shipping identification
            quantity: product quantity
            sub_total: total price of the product
        """
        self.order_id = order_id
        self.order_num = Order.num_order
        Order.num_order += 1
        self.itemid = itemid
        self.date_created = date_created
        self.date_shipped = date_shipped
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.status = None 
        self.shipping_id = shipping_id
        self.quantity = 1
        self.sub_total = 1


    def set_status(self, status):
       self.status = status

    def get_status(self):
        return self.status
    
    def __str__(self):
        return f"{self.customer_name}, your order number {self.order_id} has been confirmed, total price: {self.sub_total}."

    def calc_price(self, product: Product):
        self.sub_total = product.price * self.quantity

class CreatePage(QDialog):
    def __init__(self):
        super(CreatePage, self).__init__()
        loadUi("create_account.ui", self)

        self.b_ok.clicked.connect(self.new_account)
    def new_account(self):
        name = self.t_name.toPlainText()
        password = self.t_password.toPlainText()
        type = self.t_type.toPlainText()
        if type == "admin":
            admin[name] = password
        if type == "customer":
            customer[name] = password
        print("Successfully created")



class LoginPage(QDialog):
    def __init__(self):
        super(LoginPage, self).__init__()
        loadUi("login.ui", self)
        self.login.clicked.connect(self.open_next)
        self.exit.clicked.connect(self.close)
        self.b_create.clicked.connect(self.create_page)

    def create_page(self):
        w = CreatePage()
        w.exec_()
    def open_next(self):
        name = self.u_input.toPlainText()
        password = self.p_input.toPlainText()
        if name in admin and admin[name] == password:
            w = Admin()
            w.exec_()
        elif name in customer and customer[name] == password:
            w = OrderMain()
            w.exec_()
        else:
            print("invalid username or password")
    def close(self):
        self.close()
        # widget = MainPage2()
        # widget.exec_()
        # widget2 = MainPage3()
        # widget2.exec_()


class OrderMain(QDialog):
    def __init__(self):
        super(OrderMain, self).__init__()
        loadUi("ORDER.ui", self)
        self.pushButton.clicked.connect(self.next)
        self.pushButton_2.clicked.connect(self.back)

    def next(self):
        self.hide()
        s = ViewOrder()
        s.exec_()

    def back(self):
        self.hide()
        l = LoginPage()
        l.exec_()


class ViewOrder(QDialog):
    def __init__(self):
        super(ViewOrder, self).__init__()
        loadUi("order1.ui", self)

        self.pushButton.clicked.connect(self.back)

    def back(self):
        self.hide()
        f = OrderMain()
        f.exec_()


class Shelf:
    shelfs = []

    def __init__(self, shelfid):
        self.shelfid = shelfid
        self.comp = {"A": [], "B": []}
        Shelf.shelfs.append(self)

    def __str__(self):
        return str(self.comp)

    def scan_in(self, item, compartment):
        self.comp[compartment].append(item)
        print("successfully put into shelf!")

    def scan_out(self, item, box):
        for c in self.comp:
            if item in self.comp[c]:
                self.comp[c].remove(item)
                print("Successfully scaned out of the shelf# {0}!".format(self.shelfid))
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
                print("successfully scan out of trolly!")


class Box:
    def __init__(self, boxid, info):
        self.boxid = boxid
        self.info = info
        self.items = []

    def get_info(self):
        return "box number {0} with {1} items".format(self.boxid, len(self.items))

    def put_in(self, item):
        self.items.append(item)


class ViewProduct(QDialog):
    def __init__(self):
        super(ViewProduct, self).__init__()
        loadUi("view_product.ui", self)
        self.b_view.clicked.connect(self.p_product_info)

    def p_product_info(self):
        id = int(self.ID_edit.toPlainText())
        w = ProductInfo()
        w.set_info(id)
        w.exec_()


class ProductInfo(QDialog):
    def __init__(self):
        super(ProductInfo, self).__init__()
        loadUi("product_info.ui", self)

    def set_info(self, id):
        b = True
        for s in Shelf.shelfs:
            for c in s.comp:
                print(s.comp[c])
                for p in s.comp[c]:
                    print(p.itemid, id)
                    if p.itemid == id:
                        self.l_name.setText(str(p.name))
                        self.l_id.setText(str(p.itemid))
                        self.l_status.setText(str(p.status))
                        b = False
        if b:
            self.l_name.setText("Not Found")
            self.l_id.setText("Not Found")
            self.l_status.setText("Not Found")


class ScanIn(QDialog):
    def __init__(self):
        super(ScanIn, self).__init__()
        loadUi("scan_in_shelf.ui", self)
        self.okButton.clicked.connect(self.into_shelf)

    def into_shelf(self, AddProduct):
        pid = int(self.t_pid.toPlainText())
        shelfid = int(self.shelfid.toPlainText())
        compartment = self.compartment.toPlainText()
        target_p = None
        for i in t1.items:
            if i.itemid == pid:
                target_p = i
                break
        if target_p:
            t1.scan_out(target_p, shelfid, compartment)


class ScanOut(QDialog):
    def __init__(self):
        super(ScanOut, self).__init__()
        loadUi("scan_out_shelf.ui", self)
        self.ok_Button.clicked.connect(self.message)
        self.info.setText(str(Shelf.shelfs))

    def message(self):
        shelfid = int(self.ID_edit.toPlainText())
        compartment = self.Comp_edit.toPlainText()
        pid = int(self.PID_edit.toPlainText())
        bid = int(self.BID_edit.toPlainText())
        b = Box(bid, "hi")

        for s in Shelf.shelfs:
            if s.shelfid == shelfid:
                for c in s.comp:
                    for p in s.comp[c]:
                        if p.itemid == pid:
                            s.scan_out(p, b)


class ViewShelf(QDialog):
    def __init__(self):
        super(ViewShelf, self).__init__()
        loadUi("view_shelf.ui", self)
        self.b_view.clicked.connect(self.view_shelf)

    def view_shelf(self):
        shelfid = int(self.t_shelfid.toPlainText())
        target_s = None
        for s in Shelf.shelfs:
            if s.shelfid == shelfid:
                target_s = s
                break
        self.l_show.setText(str(target_s))
        self.update()

class AddProduct(QDialog):
    def __init__(self):
        super(AddProduct, self).__init__()
        loadUi("create_product.ui", self)
        self.ok_button.clicked.connect(self.create_product)

    def create_product(self):
        p_id = int(self.id_input.toPlainText())
        name = str(self.n_input.toPlainText())
        price = float(self.p_input.toPlainText())
        type = str(self.t_input.toPlainText())
        bar = int(self.b_input.toPlainText())
        p = Product(name, price, 1, 1, type, p_id, bar, 1)
        print("successfully added a product")
        t1.scan_onto(p)
        print("successfully scanned into trolly")


class Admin(QDialog):
    def __init__(self):
        super(Admin, self).__init__()
        loadUi("admin_page.ui", self)
        self.view_product.clicked.connect(self.p_in_id)
        self.scan_in_shelf.clicked.connect(self.p_scan_in)
        self.scan_out_shelf.clicked.connect(self.p_out_p)
        self.view_shelf.clicked.connect(self.p_view_shelf)
        self.add_product.clicked.connect(self.p_add)

    def p_scan_in(self):
        w = ScanIn()
        w.exec_()

    def p_in_id(self):
        w = ViewProduct()
        w.exec_()

    def p_out_p(self):
        w = ScanOut()
        w.exec_()

    def p_view_shelf(self):
        w = ViewShelf()
        w.exec_()

    def p_add(self):
        w = AddProduct()
        w.exec_()

if __name__ == "__main__":
    customer = {}
    admin = {}
    t1 = Trolly(1)
    s1 = Shelf(1)

    # p = Product(1, 1, 1, 1, 1, 123, 1, 1)
    # p2 = Product("cat", 1, 1, 1, 1, 321, 1, 1)
    # t1.scan_onto(p2)
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
    widget = LoginPage()
    widget.show()
    sys.exit(app.exec_())


