'''
The observer pattern is useful for state monitoring and event handling situations. This
pattern allows a given object to be monitored by an unknown and dynamic group of
observer objects.
'''

class Inventory:
    
    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0
    
    def attach(self, observer):
        self.observers.append(observer)
    
    @property
    def product(self):
        return self._product
    
    @product.setter
    def product(self, value):
        self._product = value
        self._update_observers()

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._update_observers()
    
    def _update_observers(self):
        for observer in self.observers:
            observer(self._product, self._quantity)


class ConsoleObserver:
    
    def __init__(self):
        pass
    
    def __call__(self, product, quantity):
        print(product)
        print(quantity)

i = Inventory()
c = ConsoleObserver()

i.attach(c)
i.product = "Widget"
i.quantity = 5