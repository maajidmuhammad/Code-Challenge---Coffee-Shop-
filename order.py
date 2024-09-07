class Order:
    _all = []

    def __init__(self, customer, coffee, price):
        if isinstance(customer, Customer) and isinstance(coffee, Coffee):
            self._customer = customer
            self._coffee = coffee
        else:
            raise ValueError("Invalid customer or coffee.")
        
        if isinstance(price, (float, int)) and 1.0 <= price <= 10.0:
            self._price = float(price)
            Order._all.append(self)
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")
    
    @property
    def customer(self):
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee
    
    @property
    def price(self):
        return self._price
