#Applying different algorithms on Wine predictor dataset.
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

def MarvellousWinePredictor(data_path):
    # step1:load data
    data = pd.read_csv(data_path, index_col=0)
    print("size of actual dataset is", len(data))

    # step2:Clean,Prepare& Manipulate the data
    df = pd.DataFrame(data)
    print(df)

    feature_names = df[["Alcohol","Malic acid","Ash","Alcalinity of ash","Magnesium","Total phenols","Flavanoids","Nonflavanoid phenols","Proanthocyanins","Color intensity","Hue","OD280/OD315 of diluted wines","Proline"]]
    print("Names of features:")
    print(feature_names)

    label=df["Class"]
    print("label:")
    print(label)

    #vs=sns.heatmap(df.corr()) #for checking if 2 variables y & xi's are related or not.
    #plt.show()

    cleaned_data=df.drop(["Malic acid","Ash","Magnesium","Nonflavanoid phenols"], axis=1)
    print(cleaned_data)

    # Combining into single list of tuples
    #features = list(zip("Alcohol","Malic acid","Ash","Alcalinity of ash","Magnesium","Total phenols","Flavanoids","Nonflavanoid phenols","Proanthocyanins","Color intensity","Hue","OD280/OD315 of diluted wines","Proline"))
    #print(features)

    MarvellousWinePredictor.Data_train, MarvellousWinePredictor.Data_test, MarvellousWinePredictor.Target_train, MarvellousWinePredictor.Target_test = train_test_split(feature_names, label, test_size=0.2)

def MarvellousKNN(data_path):
    MarvellousWinePredictor(data_path)
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(MarvellousWinePredictor.Data_train, MarvellousWinePredictor.Target_train)

    predicted = model.predict(MarvellousWinePredictor.Data_test)
    print("predicted:",predicted)

    Accuracy = accuracy_score(MarvellousWinePredictor.Target_test, predicted)
    return Accuracy


def MarvellousSVM(data_path):
    MarvellousWinePredictor(data_path)
    model=svm.SVC()
    model.fit(MarvellousWinePredictor.Data_train,MarvellousWinePredictor.Target_train)

    predicted=model.predict(MarvellousWinePredictor.Data_test)
    print(predicted)

    Accuracy = accuracy_score(MarvellousWinePredictor.Target_test, predicted)
    return Accuracy

def MarvellousDecisionTreeClassifier(data_path):
    MarvellousWinePredictor(data_path)
    Classifier = DecisionTreeClassifier()
    Classifier.fit(MarvellousWinePredictor.Data_train, MarvellousWinePredictor.Target_train)
    Predictions = Classifier.predict(MarvellousWinePredictor.Data_test)
    Accuracy = accuracy_score(MarvellousWinePredictor.Target_test, Predictions)
    return Accuracy

def MarvellousRandomForest(data_path):
    MarvellousWinePredictor(data_path)
    model=RandomForestClassifier()
    model.fit(MarvellousWinePredictor.Data_train, MarvellousWinePredictor.Target_train)
    Predictions=model.predict(MarvellousWinePredictor.Data_test)

    Accuracy=accuracy_score(MarvellousWinePredictor.Target_test,Predictions)
    return Accuracy


def main():
    print("Machine Learning Application")
    w=MarvellousKNN("WinePredictor (1).csv")
    x=MarvellousSVM("WinePredictor (1).csv")
    y=MarvellousDecisionTreeClassifier("WinePredictor (1).csv")
    z=MarvellousRandomForest("WinePredictor (1).csv")
    print("Accuracy of WinePredictor with KNN is ", w * 100)
    print("Accuracy of WinePredictor with SVM is ", x * 100)
    print("Accuracy of WinePredictor with Decision Tree Classifier is ", y * 100)
    print("Accuracy of WinePredictor with Random Forest is ", z * 100)

if __name__ == "__main__":
    main()

