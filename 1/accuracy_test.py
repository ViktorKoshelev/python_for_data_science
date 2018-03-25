from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

clf = tree.DecisionTreeClassifier()
neighbour = KNeighborsClassifier(n_neighbors = 3)
regression = LogisticRegression()
forest = RandomForestClassifier(n_estimators=2)
gaussian = GaussianNB()

def accuracy_test(clf, algorithm):
	global X
	global Y
	global test
	global y_test

	clf = clf.fit(X, Y)
	prediction = clf.predict(test)
	print(algorithm, prediction)

	right = 0

	for i in range(0, len(test)):
		if (prediction[i] == y_test[i]):
			right += 1

	print('accuracy ' + algorithm, int(float(right)/len(test)*100))


X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
	[190, 90, 47], [175, 64, 39], [177, 70, 40]]

test = [[159, 55, 37], [171, 75, 42], [181, 85, 43], [180, 60, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female']

y_test = ['female', 'male', 'male', 'male']

accuracy_test(clf, 'tree')
accuracy_test(neighbour, 'neighbours')
accuracy_test(regression, 'regression')
accuracy_test(forest, 'forest')
accuracy_test(gaussian, 'gaussian')