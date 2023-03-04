import control
import numpy as np
import matplotlib.pyplot as plt


def step(G, t=np.linspace(0, 10, 1000)):
    t, y = control.step_response(G, t)
    return t, y

