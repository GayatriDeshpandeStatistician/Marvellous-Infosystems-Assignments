#Play predictor case study

import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def MarvellousPlayPredictor(data_path):
    # step1:load data
    data = pd.read_csv(data_path, index_col=0)

    print("size of actual dataset is", len(data))

    # step2:Clean,Prepare& Manipulate the data
    feature_names = ["Whether", "Temperature"]

    print("Names of features", feature_names)
    whether = data.Whether
    temperature = data.Temperature
    play = data.Play

    # Creating label encoder
    le = preprocessing.LabelEncoder()

    # Converting string labels to numbers
    whether_encoded = le.fit_transform(whether)
    print(whether_encoded)

    # converting xi's sting to numbers
    temp_encoded = le.fit_transform(temperature)
    label = le.fit_transform(play)
    print(temp_encoded)
    print(label)

    # Combining Weather & temperature into single list of tuples
    features = list(zip(whether_encoded, temp_encoded))

    Data_train, Data_test, Target_train, Target_test = train_test_split(features, label, test_size=0.2)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(Data_train, Target_train)

    predicted = model.predict(Data_test)
    print("predicted:",predicted)

    Accuracy = accuracy_score(Target_test, predicted)

    return Accuracy


def main():
    print("Machine Learning Application")
    Ret=MarvellousPlayPredictor("C:\\Users\\admin\\Downloads\\PlayPredictor.csv")
    print("Accuracy of PlayPredictor with KNN is ", Ret * 100)


if __name__ == "__main__":
    main()
