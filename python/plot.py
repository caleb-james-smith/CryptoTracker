# plot.py

import matplotlib.pyplot as plt

def plot_scatter(x_values, y_values, title, x_label, y_label):
    plt.scatter(x_values, y_values)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


