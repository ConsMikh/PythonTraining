'''Создание data class
Преимущество в том, что он создается в 1 строку
К двум объектам data class можно применить операцию сравнения

 Dataclasses are not iterable, so you can't loop over or unpack their values
'''

from dataclasses import make_dataclass
Stock = make_dataclass("Stock", ["symbol", "current", "high", "low"])
stock = Stock("FB", 177.46, high=178.67, low=175.79)

print(stock)
print(stock.current)
stock.current=178.25
print(stock)
stock.unexpected_attribute = 'allowed'
print(stock.unexpected_attribute)

stock2 = Stock("FB", 178.25, 178.67, 175.79)
print(stock==stock2)

# Создание data class через декоратор
# Если использовать (order=True), то порядок аргументов закрепляется и можно использовать операции сравнения
# При равенстве первой пары аргументов сравнивается следующая пара
from dataclasses import dataclass
@dataclass(order=True)
class StockDefaults:
    name: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0

stock3 = StockDefaults('FB', current= 100.0)
stock4 = StockDefaults('FB', current= 200.0)
print(stock4 > stock3)

