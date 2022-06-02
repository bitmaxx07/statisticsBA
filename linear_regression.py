import matplotlib.pyplot as plt
import pandas as pd
import sklearn.linear_model

data = pd.read_excel("arellano_data.xlsx")
data.to_csv("res.csv")

# correlation from here

df = pd.DataFrame(data)
print("Correlation coefficient between educ and skills: " + str(df["skills"].corr(df["educ"])))

######################

# linear regression education and large firm
# read x and y data
print("largefirm regression: ")
x = data.educ.values
y = data.largefirm.values

length = len(df.index)
x = x.reshape(length, 1)
y = y.reshape(length, 1)

regr = sklearn.linear_model.LinearRegression()
regr.fit(x, y)
plt.scatter(x, y, color="black")
plt.plot(x, regr.predict(x), color="blue", linewidth=3)
plt.xticks()
plt.xlabel("educ")
plt.yticks()
plt.ylabel("largefirm")
plt.show()
res = "Regression result: y = " + str(regr.coef_) + "x + " + str(regr.intercept_)
print(res)

########################
# linear regression education, skills and large firm
print("regression education & skills vs. large firm")
x_edu_skills = df[['educ', 'skills']]
# x_edu_skills = x_edu_skills.reshape(length, 1)
y_edu_skills = df['largefirm']

regr_edu_skills = sklearn.linear_model.LinearRegression()
regr_edu_skills.fit(x_edu_skills, y_edu_skills)
# plt.scatter(x_edu_skills, y_edu_skills, color="red")
# plt.plot(x_edu_skills, regr_edu_skills.predict(x_edu_skills), color="yellow", linewidth=3)
# plt.xticks()
# plt.xlabel("edu & skills")
# plt.yticks()
# plt.ylabel("large firm")
# plt.show()
res_edu_skills = "Regression result: y = " + str(regr_edu_skills.coef_) + "x + " + str(regr_edu_skills.intercept_)
print(res_edu_skills)


# linear regression for workers in Europe
print("workers regression: ")
df_new = df.loc[df['europe'] == 1]
y_eu = df_new.largefirm.values
x_eu = df_new.educ.values
len_eu = len(df_new.index)

y_eu = y_eu.reshape(len_eu, 1)
x_eu = x_eu.reshape(len_eu, 1)
regr_eu = sklearn.linear_model.LinearRegression()
regr_eu.fit(x_eu, y_eu)
plt.scatter(x_eu, y_eu, color="pink")
plt.plot(x_eu, regr.predict(x_eu), color="green", linewidth=5)
plt.xticks()
plt.xlabel("educ")
plt.yticks()
plt.ylabel("skill")
plt.show()
res_eu = "Regression result : y = " + str(regr_eu.coef_) + "x + " + str(regr_eu.intercept_)
print(res_eu)
