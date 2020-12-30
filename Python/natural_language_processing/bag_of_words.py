import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix


def generate_corpus(data_set: pd.DataFrame, column: str, sample_size: int) -> list:
    corpus = []
    ps = PorterStemmer()
    for i in range(sample_size):
        line = re.sub('[^a-zA-Z]', ' ', data_set[column][i])
        line = line.lower()

        line = [ps.stem(word) for word in line.split() if word not in set(stopwords.words('english'))]
        line = ' '.join(line)
        corpus.append(line)
    return corpus


if __name__ == '__main__':
    nltk.download('stopwords')

    data_set = pd.read_csv("../data/reviews.tsv", delimiter='\t', quoting=3)

    corpus = generate_corpus(data_set, 'Review', sample_size=data_set.shape[0])

    cv = CountVectorizer(max_features=2000)
    x = cv.fit_transform(corpus).toarray()
    y = data_set.iloc[:, 1].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

    classifier = GaussianNB()
    classifier.fit(x_train, y_train)

    y_pred = classifier.predict(x_test)

    print(confusion_matrix(y_test, y_pred))
