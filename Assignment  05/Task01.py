import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,root_mean_squared_error
from sklearn.model_selection import train_test_split


data = load_diabetes(as_frame= True)
df = data['frame']


sns.heatmap(data=df.corr().round(2),annot= True)
plt.show()

plt.subplot(1,2,1)
plt.scatter(df['bmi'],df['target'])
plt.xlabel('BMI')
plt.ylabel('Target')

plt.subplot(1,2,2)
plt.scatter(df['s5'],df['target'])
plt.xlabel('s5')
plt.ylabel('Target')
plt.show()

x= pd.DataFrame(df[['bmi','s5']],columns = ['bmi','s5'])
y = df['target']

x_train, x_test, y_train,y_test = train_test_split(x,y, random_state=5 , test_size=0.2)
lm = LinearRegression()
lm.fit(x_train,y_train)
y_train_predict = lm.predict(x_train)
y_test_predict = lm.predict(x_test)

rmse_train_base = root_mean_squared_error(y_train, y_train_predict)
rmse_test_base  = root_mean_squared_error(y_test,  y_test_predict)
r2_train_base   = r2_score(y_train, y_train_predict)
r2_test_base    = r2_score(y_test,  y_test_predict)



x_bp = df[['bmi', 's5', 'bp']].copy()
x_trainBp, x_testBp, y_trainBp, y_testBp = train_test_split(x_bp, y, test_size=0.2, random_state=5)

lmBp = LinearRegression()
lmBp.fit(x_trainBp, y_trainBp)

y_trainBp_predict = lmBp.predict(x_trainBp)
y_testBp_predict  = lmBp.predict(x_testBp)

rmse_train_bp = root_mean_squared_error(y_trainBp, y_trainBp_predict)
rmse_test_bp  = root_mean_squared_error(y_testBp,  y_testBp_predict)
r2_train_bp   = r2_score(y_trainBp, y_trainBp_predict)
r2_test_bp    = r2_score(y_testBp,  y_testBp_predict)



x_bp_s4 = df[['bmi', 's5', 'bp', 's4']].copy()
x_trainBpS4, x_testBpS4, y_trainBpS4, y_testBpS4 = train_test_split(x_bp_s4, y, test_size=0.2, random_state=5)

lmBpS4 = LinearRegression()
lmBpS4.fit(x_trainBpS4, y_trainBpS4)

y_trainBpS4_predict = lmBpS4.predict(x_trainBpS4)
y_testBpS4_predict  = lmBpS4.predict(x_testBpS4)

rmse_train_bpS4 = root_mean_squared_error(y_trainBpS4, y_trainBpS4_predict)
rmse_test_bpS4  = root_mean_squared_error(y_testBpS4,  y_testBpS4_predict)
r2_train_bpS4   = r2_score(y_trainBpS4, y_trainBpS4_predict)
r2_test_bpS4    = r2_score(y_testBpS4,  y_testBpS4_predict)

print("TRAIN metrics")

print("Feature      base(bmi+s5) +bp    +bp+s4")

print(f"R2          {r2_train_base:8.3f} {r2_train_bp:8.3f} {r2_train_bpS4:8.3f}")
print(f"RMSE         {rmse_train_base:8.3f} {rmse_train_bp:8.3f} {rmse_train_bpS4:8.3f}")


print("TEST metrics")

print("Feature      base(bmi+s5)  +bp   +bp+s4")

print(f"R2           {r2_test_base:8.3f} {r2_test_bp:8.3f} {r2_test_bpS4:8.3f}")
print(f"RMSE         {rmse_test_base:8.3f} {rmse_test_bp:8.3f} {rmse_test_bpS4:8.3f}")