# -*- coding: utf-8 -*-


def f1(x):
    return x ** 2 - 1


def f2(x):
    return 2 ** x - 1


def f3(x):
    pass


def derivative(f, x, h):  # !!! Här betyder h derivatans exakthet
    # Bryter upp formeln för förstaderivatan i tre delar:
    c = 1.0 / (2 * h)
    x1 = f(x - h)
    x2 = f(x + h)
    return c * (x2 - x1)


def eqsolver(f, x0, h):  # !!! Här betyder h ekvationslösningens exakthet
    x1 = x0
    x2 = (
        x0 + 2 * h
    )  # Man hade även kunnat ha ett annat ursprungsavstånd mellan punkterna.
    while not ((-h < x2 - x1 < h) or (-h < x2 + x1 < h)):
        x2 = x1
        x1 = x1 - f(x1) / derivative(f, x1, 0.01)
    return x2


print(eqsolver(f2, 100, 0.01))
