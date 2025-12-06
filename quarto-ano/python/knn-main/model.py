import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
data = pd.read_table('Fruits_Data.txt')
data.head()
# calculate the correlation
corr = data.corr()
# plot the heatmap
sns.heatmap(corr, cmap="Blues", annot=True)

X = data[['mass', 'width', 'height']]
y = data['fruit_label']

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.20, random_state=3)
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train,y_train)
scr=knn.score(X_test,y_test)
print("Score for your model is ",scr)

#1: 'apple', 2: 'mandarin', 3: 'orange', 4: 'lemon'
res=knn.predict([[120,6.0,8.4]])
if res==1:
    print("Apple")
elif res==2:
    print("Mandarin")
elif res==3:
    print("Orange")
else:
    print("Lemon")
		


#Find best K value
k_range = range(1,20)
scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X_train, y_train)
    scores.append(knn.score(X_test, y_test))

plt.figure()
plt.xlabel('K')
plt.ylabel('Accuracy')
plt.scatter(k_range, scores)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]);
