
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score
print("ML Model Starting...")
df = pd.read_csv('creditcard.csv')
X = df.drop('Class', axis=1)
y = df['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = XGBClassifier()
model.fit(X_train, y_train)
print("ROC-AUC:", roc_auc_score(y_test, model.predict_proba(X_test)[:,1]))
print("SUCCESS! ML Project Ready!")
