from warehouse import *

def test_Product():
    pass


def test_Order():
    books = Order(105, 300, "October 10th", "October 31", "Christian", 102983, 105020, 5)
    assert books.order_id == 105
    assert books.date_created == "October 10th"
    assert books.quantity == 5

    printer = Order(320, 607, "July 31th", "October 31", "Jessica", 401950, 398510, 1)
    assert printer.date_shipped == "October 31"
    assert printer.customer_name == "Jessica"
    assert printer.customer_id == "401950"


def test_Shelf():
    pass


def test_Trolly():
    trolly = Trolly(103040)
    assert trolly.trollyid == 103040

    trolly = Trolly(5123)
    assert trolly.trollyid == 5123

def test_Box():
    pass


def test_Warehouse():
    pass
