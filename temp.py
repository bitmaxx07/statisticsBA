from statistics import median
from numpy import quantile
from matplotlib import pyplot

items = []
items_x = []

for i in range(1, 101):
    items_x.append(i)

for i in range(1, 41):
    items.append(10)
for i in range(1, 31):
    items.append(12)
for i in range(1, 21):
    items.append(15)
for i in range(1, 11):
    items.append(18)
print(sum(items) / len(items))
print(median(items))
print(quantile(items, 0.4))

pyplot.boxplot(items)

pyplot.show()
