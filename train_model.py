import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.inspection import permutation_importance
import seaborn as sns
import joblib
 
# Step 1: Load the Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target
 
# Step 2: Visualize the dataset - Feature Pair Plot
sns.pairplot(pd.concat([X, pd.DataFrame({'target': y})], axis=1), hue='target', diag_kind="kde", markers=["o", "s", "D"])
plt.savefig("feature_pair_plot.png")
plt.close()
print("Feature pair plot saved as feature_pair_plot.png")
 
# Step 3: Train a Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)
 
# Step 4: Visualize the decision tree structure
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.savefig("decision_tree_structure.png")
plt.close()
print("Decision tree structure plot saved as decision_tree_structure.png")
 
# Step 5: Feature importance plot
importance = clf.feature_importances_
plt.barh(iris.feature_names, importance, color="teal")
plt.xlabel("Feature Importance")
plt.title("Feature Importance of Decision Tree")
plt.savefig("feature_importance_plot.png")
plt.close()
print("Feature importance plot saved as feature_importance_plot.png")
 
# Step 6: Save the trained model
model_filename = "iris_model.pkl"
joblib.dump(clf, model_filename)
print(f"Model saved to {model_filename}")
