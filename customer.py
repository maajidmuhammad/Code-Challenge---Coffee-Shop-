class Customer:
    _all = []

    def __init__(self, name):
        self.name = name
        Customer._all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")
    
    def orders(self):
        return [order for order in Order._all if order.customer == self]
    
    def coffees(self):
        return list(set(order.coffee for order in self.orders()))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        customers = {}
        for order in Order._all:
            if order.coffee == coffee:
                if order.customer in customers:
                    customers[order.customer] += order.price
                else:
                    customers[order.customer] = order.price
        if customers:
            return max(customers, key=customers.get)
        return None
