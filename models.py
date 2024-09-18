# Coffee class
class Coffee:
    def __init__(self, name):
        self._name = None
        self.name = name
        self._orders = []


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be of type str.")
        if not (1 <= len(new_name) <= 15):
            raise ValueError("Name must be between 1 and 15 characters.")
        self._name = new_name

    def orders(self):
        return self._orders
    
    def add_order(self, order):
        if not isinstance(order, Order):
            raise TypeError('Order must be an instance of Order')
        self._orders.append(order)

    def coffees(self):
        return list(set([order.coffee for order in self._orders]))

    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        coffee._orders.append(new_order)
        return new_order
    
# Customer class
class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
        
   
    @property
    def name(self):
        return self._name
    
    @name.setter
            

    def name(self, value):
        if not isinstance(value, str):
            raise Exception('Name must be a string')
        if not (1<= len(value) <= 15):
            raise Exception('Name must be between 1 to 15 characters long')
        self._name = value
 
    def orders(self):
        return self._orders
    
    def add_order(self, order):
        if not isinstance(order, Order):
            raise TypeError('Order must be an instance of Order')
        self._orders.append(order)
    
    def coffees(self):
        coffee_orders = {order.coffee for order in self._orders if isinstance(order.coffee, Coffee)}
        return list(coffee_orders)
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        total_price = sum([order.price for order in self._orders])
        return total_price / len(self._orders)
    
    
# Order Class

class Order:
    
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = None
        self.price = price
        
        coffee.add_order(self)
        customer.add_order(self)
        Order.all.append(self)
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, amount):
        if hasattr(self, '_price') and self._price is not None:
            raise Exception('Amount cannot be changed once set')
        
        if not isinstance(amount, float):
            raise Exception('Price must be into float format')
        
        if not (1.0<= amount <=10.0):
            raise Exception('Number must be between 1.0 and 10.0')
        
        self._price = amount
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, related_to_customer):
        if not isinstance(related_to_customer, Customer):
            raise Exception('Customer must be a type Customer.')
        self._customer = related_to_customer
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, related_to_coffee):
        if not isinstance(related_to_coffee, Coffee):
            raise Exception('Coffee must be of type Coffee.')
        self._coffee = related_to_coffee    