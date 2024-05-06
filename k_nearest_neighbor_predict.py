import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from pprint import pprint

seeds = pd.read_csv('TAS2R38_dataset_normalized.csv')

data = seeds.iloc[:, 0:7]
labels = seeds.iloc[:, 7]
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.4, random_state=1)

knn = KNeighborsClassifier(n_neighbors=30)

knn.fit(x_train, y_train)

y_pred = knn.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='micro')
recall = recall_score(y_test, y_pred, average='micro')

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
