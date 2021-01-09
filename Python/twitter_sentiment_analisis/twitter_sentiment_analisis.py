import tweepy, json, time, yaml
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def extract_tweets(sources: tuple, api: tweepy.API, count=100) -> pd.DataFrame:
    array_sentiments = []

    for user in sources:
        count_tweet = count
        print("Start tweets from %s" % user)
        for x in range(count//20):
            public_tweets = api.user_timeline(user, page=x)

            for tweet in public_tweets:
                compound = analyzer.polarity_scores(tweet["text"])["compound"]
                pos = analyzer.polarity_scores(tweet["text"])["pos"]
                neu = analyzer.polarity_scores(tweet["text"])["neu"]
                neg = analyzer.polarity_scores(tweet["text"])["neg"]

                array_sentiments.append({"Media": user,
                                         "Tweet Text": tweet["text"],
                                         "Compound": compound,
                                         "Positive": pos,
                                         "Negative": neg,
                                         "Neutral": neu,
                                         "Date": tweet["created_at"],
                                         "Tweets Ago": count_tweet})

                count_tweet -= 1

    print("DONE")

    sentiments_df = pd.DataFrame.from_dict(array_sentiments)
    sentiments_df['Media'] = sentiments_df['Media'].map(lambda x: x.lstrip('@'))
    sentiments_df = sentiments_df[
        ["Media", "Date", "Tweet Text", "Compound", "Positive", "Negative", "Neutral", "Tweets Ago"]]
    sentiments_df.to_csv("mySentimentAnalysis.csv")
    return sentiments_df


def visualize_sentiment(colors: tuple, sentiments_df: pd.DataFrame):
    source = sentiments_df["Media"].unique()
    media_colors_map = {key: value for key, value in zip(source, colors)}
    for media in source:
        mydf = sentiments_df[sentiments_df["Media"] == media]
        plt.scatter(mydf["Tweets Ago"], mydf["Compound"], marker="o", linewidth=0, alpha=0.8, label=media,
                    facecolors=mydf.Media.map(media_colors_map))

    plt.legend(bbox_to_anchor=(1, 1), title="Media Sources")
    plt.title("Sentiment Analysis of Media Tweets (%s)" % (time.strftime("%x")), fontsize=14)
    plt.xlabel("Tweets Ago")
    plt.ylabel("Tweet Polarity")
    plt.xlim(max(sentiments_df["Tweets Ago"])+1, 0)
    plt.ylim(-1, 1)
    plt.grid(True)
    plt.savefig("Sentiment Analysis of Media Tweets.png", bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    analyzer = SentimentIntensityAnalyzer()

    with open('auth.yml') as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)
    api_key = conf.get('api_key')
    api_secret = conf.get('api_secret')
    token = conf.get('token')

    auth = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_secret)
    api = tweepy.API(auth_handler=auth, parser=tweepy.parsers.JSONParser())

    sources = ("@BBC", "@ctvnews", "@CNN", "@FoxNews", "@dawn_com")

    sentiments_df = extract_tweets(sources=sources, api=api, count=300)

    colors = ('pink', 'purple', 'red', "blue", 'green')
    visualize_sentiment(colors=colors, sentiments_df=sentiments_df)

    means_media_trends = sentiments_df.groupby("Media").mean()["Compound"].to_frame()
    means_media_trends.reset_index(inplace=True)

    print(means_media_trends)