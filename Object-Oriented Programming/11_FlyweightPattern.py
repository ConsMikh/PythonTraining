'''
The flyweight pattern is a memory optimization pattern. The flyweight pattern ensures that objects 
that share a state can use the same memory for that shared state. 
It is normally implemented only after a program has demonstrated
memory problems. It may make sense to design an optimal configuration from the
beginning in some situations, but bear in mind that premature optimization is the most
effective way to create a program that is too complicated to maintain.
'''

'''
Think of an inventory system for car sales. Each individual car has a specific serial number
and is a specific color. But most of the details about that car are the same for all cars of a
particular model. For example, the Honda Fit DX model is a bare-bones car with few
features. The LX model has A/C, tilt, cruise, and power windows and locks. The Sport
model has fancy wheels, a USB charger, and a spoiler. Without the flyweight pattern, each
individual car object would have to store a long list of which features it did and did not
have. Considering the number of cars Honda sells in a year, this would add up to a huge
amount of wasted memory.
Using the flyweight pattern, we can instead have shared objects for the list of features
associated with a model, and then simply reference that model, along with a serial number
and color, for individual vehicles.
'''

import weakref

class CarModel:
    _models = weakref.WeakValueDictionary()
    
    def __new__(cls, model_name, *args, **kwargs):
        model = cls._models.get(model_name)
        if not model:
            model = super().__new__(cls)
            cls._models[model_name] = model
        return model

    def __init__(
        self,
        model_name,
        air=False,
        tilt=False,
        cruise_control=False,
        power_locks=False,
        alloy_wheels=False,
        usb_charger=False,
    ):
        if not hasattr(self, "initted"):
            self.model_name = model_name
            self.air = air
            self.tilt = tilt
            self.cruise_control = cruise_control
            self.power_locks = power_locks
            self.alloy_wheels = alloy_wheels
            self.usb_charger = usb_charger
            self.initted = True

        def check_serial(self, serial_number):
            print(
                "Sorry, we are unable to check "
                "the serial number {0} on the {1} "
                "at this time".format(serial_number, self.model_name)
            )

class Car:
    def __init__(self, model, color, serial):
        self.model = model
        self.color = color
        self.serial = serial
    def check_serial(self):
        return self.model.check_serial(self.serial)

dx = CarModel("FIT DX")
lx = CarModel("FIT LX", air=True, cruise_control=True, power_locks=True, tilt=True)
car1 = Car(dx, "blue", "12345")
car2 = Car(dx, "black", "12346")
car3 = Car(lx, "red", "12347")

print(id(lx))
del lx
del car3
import gc
gc.collect()

lx = CarModel("FIT LX", air=True, cruise_control=True, power_locks=True, tilt=True)
print(id(lx))
lx = CarModel("FIT LX")
print(id(lx))
print(lx.air)

'''
The  id  function tells us the unique identifier for an object. When we call it a second time,
after deleting all references to the LX model and forcing garbage collection, we see that the
ID has changed. The value in the  CarModel __new__  factory dictionary was deleted and a
fresh one was created. If we then try to construct a second  CarModel  instance, however, it
returns the same object (the IDs are the same), and, even though we did not supply any
arguments in the second call, the  air  variable is still set to  True . This means the object was
not initialized the second time, just as we designed.
'''