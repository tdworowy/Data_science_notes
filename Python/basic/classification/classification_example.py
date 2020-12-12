''' https://raw.githubusercontent.com/PacktPublishing/40-Algorithms-Every-Programmer-Should-Know/master/Chapter07
/Social_Network_Ads.csv '''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def feature_to_one_hot(data_set: pd.DataFrame, column: str) -> pd.DataFrame:
    column = data_set[column].to_numpy().reshape(-1, 1)

    one_hot_encoder = OneHotEncoder()
    one_hot_encoder.fit(column)
    one_hot_labels = one_hot_encoder.transform(column).toarray()
    return one_hot_labels


if __name__ == '__main__':
    data_set = pd.read_csv('../../data/Social_Network_Ads.csv')

    '''Feature engendering'''
    data_set = data_set.drop(columns=['User ID'])  # remove user id column

    labels = feature_to_one_hot(data_set, 'Gender')
    genders = pd.DataFrame({'Female': labels[:, 0], 'Male': labels[:, 1]})

    data_set = pd.concat([genders, data_set.iloc[:, 1:]], axis=1, sort=False)
    print(data_set.head(6))

    y = data_set['Purchased']
    x = data_set.drop(columns='Purchased')

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

    '''Feature normalization (scaling)'''
    standard_scalar = StandardScaler()
    x_train = standard_scalar.fit_transform(x_train)
    x_test = standard_scalar.fit(x_test)

    print(x_train)