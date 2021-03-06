import pew
from math import atan2, pi, sqrt


OFFSETS = ((0, 0), (4, 0), (0, 4), (4, 4))
PERM_MAP = {
    0: 0,
    -1: 1,
    -2: 2,
    2: 2,
    1: 3
}
PI2 = pi/2


def polar_to_permindices(r, theta):
    rperm = round(r * r * 4)
    rperm = 3 if rperm == 4 else rperm
    return rperm % 4, PERM_MAP[round(theta / PI2)]


def state_to_permindices(state):
    polarvector = ((sqrt(x * x + y * y), atan2(y, x)) for x, y in state)
    return [polar_to_permindices(r, theta) for r, theta in polarvector]


def update(values, previous):
    output = pew.Pix()
    for (x_off, y_off), (shift, rot) in zip(OFFSETS, values):
        for y in range(4):
            for x in range(4):
                a, b = x, y
                for i in range(rot):
                    a, b = 3 - b, a
                b = (b + shift) % 4
                output.pixel(a + x_off, b + y_off,
                             previous.pixel(x + x_off, y + y_off))
    return output
