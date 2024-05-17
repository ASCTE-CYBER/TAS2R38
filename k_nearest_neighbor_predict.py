import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

### Objective: Predict the phenotype of a person based on genetic input data
### using a K-Nearest Neighbors classifier.

# Read the dataset from the CSV file
seeds = pd.read_csv('TAS2R38_dataset_normalized.csv')

# Split the dataset into data and labels
data = seeds.iloc[:, 0:7]
labels = seeds.iloc[:, 7]

# Split the dataset into training and testing sets - 60% training, 40% testing
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.4, random_state=1)

# Create a K-Nearest Neighbors classifier with 30 neighbors
knn = KNeighborsClassifier(n_neighbors=30)

# Train the classifier
knn.fit(x_train, y_train)

# Run the predictions on the test set
y_pred = knn.predict(x_test)

# Calculate the accuracy, precision, and recall
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='micro')
recall = recall_score(y_test, y_pred, average='micro')

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
