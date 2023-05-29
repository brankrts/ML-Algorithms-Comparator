from sklearn import datasets 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score



class Models : 

    def __init__(self):

        self.svm = SVC()
        self.knn = KNeighborsClassifier()
        self.bayes = GaussianNB()
        self.tree = DecisionTreeClassifier()
        self.forest =RandomForestClassifier()
        self.logistic = LogisticRegression()
    
    def all_models (self):
        return[self.svm ,self.logistic, self.knn , self.tree, self.forest , self.bayes]


class ModelProvider:

    def __init__(self,models=Models().all_models()) -> None:

        self.data = datasets.load_digits()
        self.X  = self.data.data
        self.y = self.data.target
        self.models = models

    def classify(self) :

        model_acc = dict()
        for model in self.models: 

            X_train, X_test, y_train, y_test = train_test_split(self.X,self.y, test_size=0.2, random_state=42)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            model_acc[model.__class__.__name__] = accuracy

        return model_acc

 
   


