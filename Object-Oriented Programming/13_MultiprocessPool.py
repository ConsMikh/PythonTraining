import random
from multiprocessing.pool import Pool


def prime_factor(value):
    factors = []
    for divisor in range(2, value - 1):
        quotient, remainder = divmod(value, divisor)
        if not remainder:
            factors.extend(prime_factor(divisor))
            factors.extend(prime_factor(quotient))
            break
    else:
        factors = [value]
    return factors


if __name__ == "__main__":
    pool = Pool()
    to_factor = [random.randint(100000, 50000000) for i in range(20)]
    results = pool.map(prime_factor, to_factor)
    for value, factors in zip(to_factor, results):
        print("The factors of {} are {}".format(value, factors))

'''
The  map  method accepts a function and an iterable. The pool pickles each of the values in
the iterable and passes it into an available process, which executes the function on it. When
that process is finished doing its work, it pickles the resulting list of factors and passes it
back to the pool. Then, if the pool has more work available, it takes on the next job.
Once all the pools are finished processing work (which could take some time), the results
list is passed back to the original process, which has been waiting patiently for all this work
to complete.
'''