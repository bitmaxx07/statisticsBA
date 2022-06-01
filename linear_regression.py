import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn.linear_model
from sklearn.linear_model import LinearRegression

data = pd.read_excel("arellano_data.xlsx")

# read x and y data
x = data.skills.values
y = data.educ.values

length = 4820
x = np.arange(length, dtype=float).reshape((length, 1))
y = y.reshape(length, 1)

regr = sklearn.linear_model.LinearRegression()
regr.fit(x, y)
plt.scatter(x, y, color="black")
plt.plot(x, regr.predict(x), color="blue", linewidth=3)
plt.xticks()
plt.yticks()
plt.show()
