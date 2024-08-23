import numpy as np
import sklearn
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from Pre_processing import *

data = pd.read_csv("the_trang_linear_regression.csv").values

min_max_scaler = MinMaxScaler()
data_norm = min_max_scaler.fit_transform(data)

model = LinearRegression()
model.fit(data_norm[:, 0].reshape(-1, 1), data_norm[:, 1])

wx = model.coef_

w0 = model.intercept_

w = np.array([w0, wx[0]])

x_draw = np.array([0.0, 1.0])
y_draw = w[0] + w[1] * x_draw

draw_x(data_norm[:, 0], data_norm[:, 1])
draw_line(x_draw, y_draw)
draw_show("Linear Regression", "ChieuCao", "CanNang")
