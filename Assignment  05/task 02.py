import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,root_mean_squared_error
from sklearn.model_selection import train_test_split


df = pd.read_csv("50_Startups.csv",delimiter=',')


print(f'{df} {df.dtypes}')

sns.heatmap(df.select_dtypes(include="number").corr(), annot=True, fmt=".2f")
plt.show()



plt.subplot(1,2,1)
plt.scatter(df['R&D Spend'],df['Profit'])
plt.xlabel('Spend on R&D')
plt.ylabel('Profit')

plt.subplot(1,2,2)
plt.scatter(df['Marketing Spend'],df['Profit'])
plt.xlabel('Spend on Marketing')
plt.ylabel('Profit')
plt.show()


x = df[['R&D Spend','Marketing Spend']]
y = df['Profit']

x_train, x_test, y_train,y_test = train_test_split(x,y, random_state=5 , test_size=0.4)



lm = LinearRegression()
lm.fit(x_train,y_train)
y_train_predict = lm.predict(x_train)
y_test_predict = lm.predict(x_test)



rmse_train = root_mean_squared_error(y_train, y_train_predict)
rmse_test  = root_mean_squared_error(y_test,  y_test_predict)
r2_train   = r2_score(y_train, y_train_predict)
r2_test   = r2_score(y_test,  y_test_predict)
print(f'The value of RMSE Train is {rmse_train}')
print(f'The value of RMSE Test is {rmse_test}')
print(f'The value of R2 Train is {r2_train}')
print(f'The value of R2 Test is {r2_test}')


# FINDINGS:
# The value of Train RMSE  is 10421.578538827369
# The value of Test RMSE  is 5901.149215894105
# The value of Train R2 is 0.924881963476002
# The value of Test R2 is 0.9798413266958587
#
# Explanation:
# On the training data, the model explains 92.48% of the variation in profit. That means it learned the main patterns pretty well. The average prediction error is 10421.57.
# On the test data the model does even better as 97.98% of the variation with an average error of only 5901.14.
# So, as a conclusion the model is clearly handling the relationship between the R&D spending, marketinga nd profit and its not overfitting means good at predicting.

