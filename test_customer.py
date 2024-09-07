import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("John")
        self.customer2 = Customer("Alice")
        self.coffee1 = Coffee("Latte")
        self.coffee2 = Coffee("Espresso")
    
    def test_create_order(self):
        order1 = self.customer1.create_order(self.coffee1, 5.0)
        self.assertIsInstance(order1, Order)
        self.assertEqual(order1.customer, self.customer1)
        self.assertEqual(order1.coffee, self.coffee1)
        self.assertEqual(order1.price, 5.0)

    def test_most_aficionado(self):
        self.customer1.create_order(self.coffee1, 5.0)
        self.customer1.create_order(self.coffee1, 4.0)
        self.customer2.create_order(self.coffee1, 8.0)
        aficionado = Customer.most_aficionado(self.coffee1)
        self.assertEqual(aficionado, self.customer1)

if __name__ == '__main__':
    unittest.main()
