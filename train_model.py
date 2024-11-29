import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load the Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Train a decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Save the model
model_filename = "iris_model.pkl"
joblib.dump(clf, model_filename)
print(f"Model saved to {model_filename}")
