''' https://raw.githubusercontent.com/PacktPublishing/40-Algorithms-Every-Programmer-Should-Know/master/Chapter07
/Social_Network_Ads.csv '''

import pandas as pd
from sklearn.preprocessing import OneHotEncoder


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