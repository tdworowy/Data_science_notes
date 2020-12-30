import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report


def remove_white_spaces(data_set: pd.DataFrame):
    blanks = []
    for i, lb, rv in data_set.itertuples():
        if rv.isspace():
            blanks.append(i)
    data_set.drop(blanks, inplace=True)


if __name__ == '__main__':
    data_set = pd.read_csv("../data/movies.tsv", delimiter='\t', quoting=3)
    data_set.dropna(inplace=True) # remove NAs

    remove_white_spaces(data_set)

    x = data_set['review']
    y = data_set['label']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

    text_clf_nb = Pipeline([('tfidf', TfidfVectorizer()),
                            ('clf', MultinomialNB()),
                            ])
    text_clf_nb.fit(x_train, y_train)
    
    y_pred = text_clf_nb.predict(x_test)

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test,y_pred))
