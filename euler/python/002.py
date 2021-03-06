"""
Project Euler Problem 2
=======================

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

                  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not
exceed four million.
"""


def fibonacci(limit):
    def fibonacci_acc(sequence, limit):
        if sequence[-1] + sequence[-2] <= limit:
            sequence.append(sequence[-1] + sequence[-2])
            return fibonacci_acc(sequence, limit)
        else:
            return sequence

    return fibonacci_acc([1, 2], limit)


sum_of_fibonaccis = sum([n for n in fibonacci(4000000) if n % 2 == 0])
print(sum_of_fibonaccis)
