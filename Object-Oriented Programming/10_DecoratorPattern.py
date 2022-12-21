import time

def log_calls(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        print(
            "Calling {0} with {1} and {2}".format(
                func.__name__, args, kwargs
            )
            )
        return_value = func(*args, **kwargs)
        print(
            "Executed {0} in {1}ms".format(
                func.__name__, time.time() - now
            )
        )
        return return_value
    return wrapper

@log_calls
def test1(a, b, c):
    print("\ttest1 called")

@log_calls
def test2(a, b):
    print("\ttest2 called")

@log_calls
def test3(a, b):
    print("\ttest3 called")
    time.sleep(1)

test1(1, 2, 3)
test2(4, b=5)
test3(6, 7)

print('*'*20)

# Decorator with parameter
'''
Функция might_fail теперь декорируется с помощью вызова функции вида @retry(2).
Вызов retry(2) приводит к тому, что вызывается функция retry, которая и возвращает реальный декоратор.
В итоге функция might_fail декорируется с помощью retry_decorator, так как именно эта функция представляет собой результат вызова функции retry(2).
'''
def retry(max_retries):
    def retry_decorator(func):
        def _wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    func(*args, **kwargs)
                except:
                    time.sleep(1)
        return _wrapper
    return retry_decorator


@retry(2)
def might_fail():
    print("might_fail")
    raise Exception


might_fail()

print('*'*20)

v = True

def verbose(v):
    def verbose_decorator(func):
        def _wrapper(*args, **kwargs):
            if v:
                print(f"logger: {[*args]}")
                func(*args, **kwargs)
            else:
                func(*args, **kwargs)
        return _wrapper
    return verbose_decorator


@verbose(v)
def summer(a,b):
    c = a+b
    print(c)

summer(2,3)
'''
Поведение декоратора определяется с помощью переменной. Если переменная True, то подключается вывод лога
'''

print('*'*20)

# Decorator timer

import functools
import time

def timer(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} took {runtime:.4f} secs")
        return result
    return _wrapper

@timer
def complex_calculation():
    """Some complex calculation."""
    time.sleep(0.5)
    return 42

print(complex_calculation())

'''
Так как декоратор @timer может быть представлен как complex_calculation = timer(complex_calculation), 
он обязательно изменяет функцию complex_calculation. В частности, он меняет некоторые из отражённых магических методов:
__module__
__name__
__qualname__
__doc__
__annotations__
При использовании декоратора @functools.wraps эти атрибуты возвращаются к их исходному состоянию.
'''

# Class decorator
@timer
class MyClass:
    def complex_calculation(self):
        time.sleep(1)
        return 42

my_obj = MyClass()
my_obj.complex_calculation()
'''
Декоратор вызывается только когда «вызывают» класс. «Вызов» класса — это создание его экземпляра. Получается, 
что timer вызывается лишь при выполнении строки кода my_obj = MyClass().
При декорировании класса методы этого класса не подвергаются автоматическому декорированию. 
Проще говоря — использование обычного декоратора для декорирования обычного класса приводит лишь 
к декорированию конструктора (метод __init__) этого класса.
'''
print('*'*20)

# Class decorator

class MyDecorator:
    def __init__(self, function):
        self.function = function
        self.counter = 0
    
    def __call__(self, *args, **kwargs):
        print(self.function(*args, **kwargs))
        self.counter+=1
        print(f"Called {self.counter} times")

@MyDecorator
def some_function():
    return 42

some_function()
some_function()
some_function()
'''
Функция __init__ вызывается при декорировании some_function. Тут, снова, не забываем о том, 
что использование декоратора — это аналог конструкции some_function = MyDecorator(some_function).
Функция __call__ вызывается при использовании экземпляра класса, например — при вызове функции. 
Функция some_function — это теперь экземпляр класса MyDecorator, но использовать мы её при этом планируем как функцию. 
За это отвечает магический метод __call__, в имени которого используются два символа подчёркивания.
'''