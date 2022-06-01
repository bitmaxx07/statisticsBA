import matplotlib.pyplot as plt
import pandas as pd
import sklearn.linear_model

data = pd.read_excel("arellano_data.xlsx")

# read x and y data
x = data.skills.values
y = data.educ.values

length = 4820
x = x.reshape(length, 1)
y = y.reshape(length, 1)

regr = sklearn.linear_model.LinearRegression()
regr.fit(x, y)
plt.scatter(x, y, color="black")
plt.plot(x, regr.predict(x), color="blue", linewidth=3)
plt.xticks()
plt.xlabel("skill")
plt.yticks()
plt.ylabel("educ")
plt.show()
res = "Regression result: y = " + str(regr.coef_) + "x + " + str(regr.intercept_)
print(res)
