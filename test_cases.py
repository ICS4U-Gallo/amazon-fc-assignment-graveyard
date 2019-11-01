from warehouse import *
import unittest
# import HtmlTestRunner


class TestWarehouse(unittest.TestCase):

    def test_Product(self):
        screwdriver = Product("Flat Tip Screwdriver", 5.99, "image", "Craftsman", "Screwdriver", 11223344, "barcode",
                              "3x4x1")
        self.assertEqual(screwdriver.get_info(), "Name: Flat Tip Screwdriver Product# 11223344 $5.99")
        self.assertEqual(screwdriver.get_status(), None)

        self.assertEqual(screwdriver.manufacturer, "Craftsman")
        screwdriver.set_status("purchased")
        self.assertEqual(screwdriver.get_status(), "purchased")

        phone = Product("Cordless Phone", 29.99, "image", "Panasonic", "Home Phone", 56764523, "barcode", "5x5x5")
        self.assertEqual(phone.get_info(), "Name: Cordless Phone Product# 56764523 $29.99")
        self.assertEqual(phone.get_status(), None)
        self.assertEqual(phone.manufacturer, "Panasonic")
        phone.set_status("in progress")
        self.assertEqual(phone.get_status(), "in progress")

    def test_Order(self):
        books = Order(105, 300, "October 10th", "October 31", "Christian", "102983", "105020", 1)
        self.assertEqual(books.order_id, 105)
        self.assertEqual(books.date_created, "October 10th")
        self.assertEqual(books.quantity, 1)

        printer = Order(320, 607, "July 31th", "October 31", "Jessica", "401950", "398510", 1)
        self.assertEqual(printer.date_shipped, "October 31")
        self.assertEqual(printer.customer_name, "Jessica")
        self.assertEqual(printer.customer_id, "401950")
        self.assertEqual(printer.shipping_id, 1)


    def test_Shelf(self):
        shelf_10 = Shelf("10")
        shelf_10.scan_in("screwdriver", "A")
        shelf_10.scan_in("phone", "A")
        self.assertEqual(shelf_10.show_comp("A"), ['screwdriver', 'phone'])

        shelf_2 = Shelf("2")
        shelf_2.scan_in("phone", "B")
        self.assertEqual(shelf_2.show_comp("B"), ['phone'])

    def test_Trolly(self):
        trolly = Trolly(103040)
        self.assertEqual(trolly.trollyid, 103040)

        trolly = Trolly(5123)
        self.assertEqual(trolly.trollyid, 5123)

    def test_Box(self):
        box_2297 = Box(2297, "medium size")
        self.assertEqual(box_2297.get_info(), "box number 2297 with 0 items")
        self.assertEqual(box_2297.boxid, 2297)
        box_2297.put_in("screwdriver")
        self.assertEqual(box_2297.items, ["screwdriver"])
        self.assertEqual(box_2297.get_info(), "box number 2297 with 1 items")

        box_7890 = Box(7890, "large size")
        self.assertEqual(box_7890.get_info(), "box number 7890 with 0 items")
        self.assertEqual(box_7890.info, "large size")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestWarehouse('test_Product'))
    suite.addTest(TestWarehouse('test_Order'))
    suite.addTest(TestWarehouse('test_Shelf'))
    suite.addTest(TestWarehouse('test_Trolly'))
    suite.addTest(TestWarehouse('test_Box'))

    # testRunner = HtmlTestRunner.HTMLTestRunner()
    # testRunner.run(suite)
    unittest.main()


