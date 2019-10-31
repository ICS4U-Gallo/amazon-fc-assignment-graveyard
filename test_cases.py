from warehouse import *

def test_Product():
    screwdriver = Product("Flat Tip Screwdriver", 5.99, "image", "Craftsman", "Screwdriver", 11223344, "barcode", "3x4x1")
    assert screwdriver.get_info() == "Name: Flat Tip Screwdriver Product# 11223344 $5.99"
    assert screwdriver.get_status() == None
    assert screwdriver.manufacturer == "Craftsman"
    screwdriver.set_status("purchased")
    assert screwdriver.get_status() == "purchased"

    phone = Product("Cordless Phone", 29.99, "image", "Panasonic", "Home Phone", 56764523, "barcode", "5x5x5")
    assert phone.get_info() == "Name: Cordless Phone Product# 56764523 $29.99"
    assert phone.get_status() == None
    assert phone.manufacturer == "Panasonic"
    phone.set_status("in progress")
    assert phone.get_status() == "in progress"


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
    shelf_10 = Shelf("10")
    shelf_10.scan_in("screwdriver", "A")
    shelf_10.scan_in("phone", "A")
    assert shelf_10.show_comp("A") == ['screwdriver', 'phone']

    shelf_2 = Shelf("2")
    shelf_2.scan_in("phone", "B")
    assert shelf_2.show_comp("B") == ['phone']


def test_Trolly():
    trolly = Trolly(103040)
    assert trolly.trollyid == 103040

    trolly = Trolly(5123)
    assert trolly.trollyid == 5123

def test_Box():box_2297 = Box(2297, "medium size")
    assert box_2297.get_info() == "box number 2297 with 0 items"
    assert box_2297.boxid == 2297
    box_2297.put_in("screwdriver")
    assert box_2297.items == ["screwdriver"]
    assert box_2297.get_info() == "box number 2297 with 1 items"

    box_7890 = Box(7890, "large size")
    assert box_7890.get_info() == "box number 7890 with 0 items"
    assert box_7890.info == "large size"
    box_7890.put_in(phone)
    box_7890.put_in(screwdriver)
    assert box_7890.get_info() == "box number 7890 with 2 items"


def test_Warehouse():
    pass
