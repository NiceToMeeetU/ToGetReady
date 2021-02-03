# coding   : utf-8 
# @Time    : 21/02/02 10:32
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : demo_deepforest.py
# @Software: PyCharm


from deepforest import CascadeForestClassifier

# Load utils
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data
X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

model = CascadeForestClassifier(random_state=1)

# Train
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred) * 100

print("Testing Accuracy: {:.3f} %".format(acc))