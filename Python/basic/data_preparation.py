''' https://raw.githubusercontent.com/PacktPublishing/40-Algorithms-Every-Programmer-Should-Know/master/Chapter07
/Social_Network_Ads.csv
'https://raw.githubusercontent.com/PacktPublishing/40-Algorithms-Every-Programmer-Should-Know/master/Chapter07/auto.csv
https://github.com/PacktPublishing/40-Algorithms-Every-Programmer-Should-Know/blob/master/Chapter07/weather.csv'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.preprocessing import LabelEncoder
from os import path

data_file_classification = path.join(path.dirname(path.abspath(__file__)), '../data/Social_Network_Ads.csv')
data_file_regression = path.join(path.dirname(path.abspath(__file__)), '../data/auto.csv')
data_file_weather = path.join(path.dirname(path.abspath(__file__)), '../data/weather.csv')


def feature_to_one_hot(data_set: pd.DataFrame, column: str) -> pd.DataFrame:
    column = data_set[column].to_numpy().reshape(-1, 1)

    one_hot_encoder = OneHotEncoder()
    one_hot_encoder.fit(column)
    one_hot_labels = one_hot_encoder.transform(column).toarray()
    return one_hot_labels


def get_data_classification() -> tuple:
    data_set = pd.read_csv(data_file_classification)
    data_set = data_set.drop(columns=['User ID'])  # remove user id column

    labels = feature_to_one_hot(data_set, 'Gender')
    genders = pd.DataFrame({'Female': labels[:, 0], 'Male': labels[:, 1]})

    data_set = pd.concat([genders, data_set.iloc[:, 1:]], axis=1, sort=False)
    y = data_set['Purchased']
    x = data_set.drop(columns='Purchased')

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

    standard_scalar = StandardScaler()
    x_train = standard_scalar.fit_transform(x_train)
    x_test = standard_scalar.fit_transform(x_test)
    return x_train, x_test, y_train, y_test


def get_data_regression() -> tuple:
    data_set = pd.read_csv(data_file_regression)
    data_set = data_set.drop(columns=['NAME'])  # remove name column

    data_set = data_set.apply(pd.to_numeric, errors='coerce')
    data_set.fillna(0, inplace=True)
    y = data_set['MPG']
    x = data_set.drop(columns=['MPG'])
    return train_test_split(x, y, test_size=0.25, random_state=0)


def get_data_weather() -> tuple:
    data_set = pd.read_csv(data_file_weather)
    data_set['RainToday'] = data_set['RainToday'].apply(lambda x: 1 if x == "Yes" else 0)
    data_set['RainTomorrow'] = data_set['RainTomorrow'].apply(lambda x: 1 if x == "Yes" else 0)

    le = LabelEncoder()
    data_set = data_set.dropna()
    data_set.WindGustDir = le.fit_transform(data_set.WindGustDir)
    data_set.WindDir3pm = le.fit_transform(data_set.WindDir3pm)
    data_set.WindDir9am = le.fit_transform(data_set.WindDir9am)

    x = data_set.drop(['Date', 'RainTomorrow'], axis=1)
    y = data_set['RainTomorrow']
    return train_test_split(x,y , test_size = 0.2,random_state = 2)






