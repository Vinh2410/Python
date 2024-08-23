import pandas as pd
from matplotlib import pyplot as plt


def get_data():
    data = pd.read_csv("the_trang_linear_regression.csv")
    X = data[["ChieuCao"]].values
    y = data[["CanNang"]].values
    return X, y


def draw_x(x, y):
    plt.scatter(x, y)


def draw_line(x, y):
    plt.plot(x, y, "r")


def draw_show(title="", xlabel="", ylabel=""):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


X, y = get_data()
