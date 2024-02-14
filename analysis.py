import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("los_angeles_house_shooting.csv")

# Create a function to calculate the Pearson correlation coefficient
def pearson_corr(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum([xi*yi for xi,yi in zip(x,y)])
    sum_x2 = sum([xi**2 for xi in x])
    sum_y2 = sum([yi**2 for yi in y])
    numerator = n*sum_xy - sum_x*sum_y
    denominator = math.sqrt((n*sum_x2 - sum_x**2)*(n*sum_y2 - sum_y**2))
    return numerator/denominator

df["shooting_num"] = df["shooting_num"].astype(float)
df['Price'] = df['Price'].apply(lambda x: x.replace('$', ''))
df['Price'] = df['Price'].apply(lambda x: x.replace(',', ''))
df["Price"] = df["Price"].astype(float)
corr = pearson_corr(df["shooting_num"], df["Price"])
# p_value = 2 * (1 - math.erf(abs(corr) / math.sqrt(2 * len(df))))

print("Pearson correlation coefficient:", corr)
# print("p-value:", p_value)
x = df["shooting_num"]
y = df["Price"]
m, b = np.polyfit(x, y, 1)

# Fit the data using np.polyfit
coefficients = np.polyfit(x, y, 1)
# Calculate the predicted values based on these coefficients
predicted = np.polyval(coefficients, x)
# Calculate the difference between the predicted values and the true values
error = y - predicted
# Print the mean squared error
print("Mean squared error:", np.mean(error**2))
plt.scatter(x, y)
plt.plot(x, m*x + b, color='red')
plt.xlabel("Shooting Num")
plt.ylabel("Price")
plt.title("Scatter Plot of Price and Shooting Num")
plt.savefig("scatter_plot.png")
# plt.show()