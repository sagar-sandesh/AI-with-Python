import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


df = pd.read_csv("iris.csv")

X = df.drop("species", axis=1)
y = df["species"]


x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training data shape:", x_train.shape)
print("Testing data shape:", x_test.shape)


log_model = LogisticRegression(max_iter=200)
log_model.fit(x_train, y_train)
y_pred_log = log_model.predict(x_test)


classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)
y_pred_knn = classifier.predict(x_test)

print("Logistic Regression Report:")
print(classification_report(y_test, y_pred_log))


print(" Classification Report:")
print(classification_report(y_test, y_pred_knn))


metrics.ConfusionMatrixDisplay.from_estimator(log_model, x_test, y_test)
plt.title("Logistic Regression Confusion Matrix")
plt.show()


metrics.ConfusionMatrixDisplay.from_estimator(classifier, x_test, y_test)
plt.title("Confusion Matrix")
plt.show()

print (classification_report(y_test, y_train))

error =[]
for k in range(1,20):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    error.append(np.mean(y_pred != y_test))

plt.plot(range(1,20), error, marker='o', markersize=10)
plt.xlabel("k")
plt.ylabel("Mean error")
plt.show()