import pandas as pd


def generate_recommendation(
    movie_matrix: pd.DataFrame, movie_title: str, year: str
) -> pd.DataFrame:
    user_rating = movie_matrix[f"{movie_title} ({year})"]
    user_rating = user_rating.dropna()

    similar = movie_matrix.corrwith(user_rating)
    corr = pd.DataFrame(similar, columns=["correlation"])

    corr.dropna(inplace=True)
    return corr


if __name__ == "__main__":
    reviews = pd.read_csv("../data/user_movie_reviews.csv")
    movie_titles = pd.read_csv("../data/movies_recommendation.csv", index_col=False)

    data_set = pd.merge(reviews, movie_titles, on="movieId")

    movie_matrix = data_set.pivot_table(
        index="userId", columns="title", values="rating"
    )

    corr = generate_recommendation(movie_matrix, "Avatar", "2009")

    df_ratings = pd.DataFrame(data_set.groupby("title")["rating"].mean())
    df_ratings["number_of_ratings"] = data_set.groupby("title")["rating"].count()

    corr = corr.join(df_ratings["number_of_ratings"])
    corr_10_best = (
        corr[df_ratings["number_of_ratings"] > 100]
        .sort_values(by="correlation", ascending=False)
        .head(10)
    )
    print(corr_10_best)
