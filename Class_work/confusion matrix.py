import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import seaborn as sns

df= pd.read_csv("exams.csv", skiprows=0, delimiter =",")
print(df)

X = df.iloc[:, 0:2]
y = df.iloc[:, -1]


admit_yes =df.loc[y==1]
admit_no = df.loc[y==0]


plt.scatter(admit_no.iloc[:,0], admit_no.iloc[:,1], label="No admission")
plt.scatter(admit_yes.iloc[:,0], admit_yes.iloc[:,1], label="Got admission")
plt.xlabel("Result of Exam 1")
plt.ylabel("Result of Exam 2")
plt.legend()
plt.show()


x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(x_train.shape)
model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
metrics.ConfusionMatrixDisplay.from_estimator(model, x_test, y_test)
plt.show()

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print(cnf_matrix)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Precision:", metrics.precision_score(y_test, y_pred))
print("Recall:", metrics.recall_score(y_test, y_pred))

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

print("Predicted Yes, Correct (TP):", tp)
print("Predicted Yes, Incorrect (FP):", fp)
print("Predicted No, Correct (TN):", tn)
print("Predicted No, Incorrect (FN):", fn)

# cm = [[tn, fp],
#       [fn, tp]]
#
# labels = [
#     [f"TN\nCorrect No = {tn}", f"FP\nIncorrect Yes = {fp}"],
#     [f"FN\nIncorrect No = {fn}", f"TP\nCorrect Yes = {tp}"]
# ]
# plt.figure(figsize=(6, 5))
# sns.heatmap(cm, annot=labels, fmt="", cmap="Blues", cbar=False,
#             xticklabels=["Predicted No", "Predicted Yes"],
#             yticklabels=["Actual No", "Actual Yes"])
#
# plt.title("Confusion Matrix with TP/TN/FP/FN")
# plt.ylabel("Actual")
# plt.xlabel("Predicted")
# plt.show()



plt.scatter(x_test[(y_test==1) & (y_pred==1)].iloc[:,0],
            x_test[(y_test==1) & (y_pred==1)].iloc[:,1],
            c="green", marker="o", label="TP (pred yes correct)")


plt.scatter(x_test[(y_test==0) & (y_pred==1)].iloc[:,0],
            x_test[(y_test==0) & (y_pred==1)].iloc[:,1],
            c="red", marker="*", label="FP (pred yes incorrect)")


plt.scatter(x_test[(y_test==0) & (y_pred==0)].iloc[:,0],
            x_test[(y_test==0) & (y_pred==0)].iloc[:,1],
            c="blue", marker="^", label="TN (pred no correct)")


plt.scatter(x_test[(y_test==1) & (y_pred==0)].iloc[:,0],
            x_test[(y_test==1) & (y_pred==0)].iloc[:,1],
            c="orange", marker="s", label="FN (pred no incorrect)")

plt.xlabel("Exam 1 Score")
plt.ylabel("Exam 2 Score")
plt.title("Scatter Plot of Predictions")
plt.legend()
plt.show()