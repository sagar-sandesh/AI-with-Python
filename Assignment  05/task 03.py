import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv('Auto.csv')

X = df[['cylinders','displacement','horsepower','weight','year','acceleration']]
y = df['mpg']

X_train,X_test,y_train,y_test = train_test_split(X,y, random_state = 5, test_size = 0.2)
alphas = np.linspace(0.001,80,500)
r2ValuesRidge = []
r2ValuesLasso = []

for alp in alphas:
    rr = linear_model.Ridge(alpha = alp)
    rr.fit(X_train,y_train)
    r2_testRidge = r2_score(y_test,rr.predict(X_test))
    r2ValuesRidge.append(r2_testRidge)

    lr = linear_model.Lasso(alpha = alp)
    lr.fit(X_train, y_train)
    r2_testLasso = r2_score(y_test, lr.predict(X_test))
    r2ValuesLasso.append(r2_testLasso)

best_r2Ridge = max(r2ValuesRidge)
idxRidge = r2ValuesRidge.index(best_r2Ridge)
best_alphaRidge = alphas[idxRidge]

best_r2Lasso = max(r2ValuesLasso)
idxLasso = r2ValuesLasso.index(best_r2Lasso)
best_alphaLasso = alphas[idxLasso]


print(f'Best r2: Ridge Value {best_r2Ridge:2f}    Lasso Value {best_r2Lasso:2f}')
print(f'Best alpha: Ridge Value {best_alphaRidge:2f}     Lasso Value{best_alphaLasso:2f}')



plt.subplot(1,2,1)
plt.plot(alphas,r2ValuesRidge)
plt.title('Ridge regression')
plt.xlabel('alpha')
plt.ylabel('r2')

plt.subplot(1,2,2)
plt.plot(alphas,r2ValuesLasso)
plt.title('Lasso regression')
plt.xlabel('alpha')
plt.ylabel('r2')
plt.show()