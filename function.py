from typing import Optional

from sympy import *
import math
import numpy as np


class Function:
    functions = []

    def __init__(self):
        self.functions = self.choose_function()

    def print_function(self) -> str:
        s = ''
        for i, f in enumerate(self.functions):
            if i != len(self.functions) - 1:
                s += f'({f}) +'
            else:
                s += f'({f})'
        return s

    def get_list_of_derivative_n_order(self, n) -> list:
        x = Symbol("x")

        func_derivative_n_order = []
        for f in self.functions:
            func_derivative_n_order.append(diff(f, x, n))

        return func_derivative_n_order

    def get_value(self, point) -> Optional[float]:
        x = Symbol("x")

        values = []
        for f in self.functions:
            f = diff(f, x, 0)
            value = f.subs({x: point})
            values.append(value)

        return sum(values)

    def get_value_in_nth_derivative(self, n, point) -> float:
        x = Symbol("x")

        values = []
        for f in self.functions:
            func_der_n = diff(f, x, n)
            value = func_der_n.subs({x: point})
            values.append(value)

        return sum(values)

    def get_max_value_in_range_nth_derivative(self, n, a, b) -> float:
        res = -math.inf
        x_dots = np.arange(a, b + 0.01, 0.01)
        for x in x_dots:
            res = max(res, self.get_value_in_nth_derivative(n, x))

        return res


    def get_value_integrate(self, left, right) -> float:
        res = 0
        x = symbols('x')
        for f in self.functions:
            f = diff(f, x, 0)
            res += integrate(f, (x, left, right))

        return res
