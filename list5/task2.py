#!/usr/bin/python

import numpy as np
import pandas as pd

np.seterr(invalid="ignore")


def get_recommendation(x, y):
    z = np.dot(
        np.nan_to_num(x / np.linalg.norm(x, axis=0)),
        np.nan_to_num(y / np.linalg.norm(y)),
    )

    X = np.nan_to_num(x / np.linalg.norm(x, axis=0))
    Z = np.nan_to_num(z / np.linalg.norm(z))

    return np.dot(X.T, Z)


def get_ratings(df):
    ratings_data = df.loc[
        df["movieId"] < 10000, ["userId", "movieId", "rating"]
    ].to_numpy()

    ratings = np.zeros((611, 9019))
    for data in ratings_data:
        ratings[int(data[0]), int(data[1])] = data[2]
    return ratings


def get_movies(df):
    return df.loc[df["movieId"] < 10000, ["movieId", "title"]].to_numpy()


def main():
    df = pd.read_csv("./ml-latest-small/ratings.csv", sep=",")
    movies_df = pd.read_csv("./ml-latest-small/movies.csv", sep=",")

    ratings = get_ratings(df)
    movies = get_movies(movies_df)

    my_ratings = np.zeros((9019, 1))
    my_ratings[2571] = 5
    my_ratings[32] = 4
    my_ratings[260] = 5
    my_ratings[1097] = 4

    recommendations = get_recommendation(ratings, my_ratings)

    recommended_movies = []
    for movie in movies:
        recommended_movies.append((recommendations[movie[0]][0], movie[1]))

    recommended_movies = sorted(recommended_movies, key=lambda x: x[0], reverse=True)

    for rec in recommended_movies[:10]:
        print(rec[0], "\t", rec[1])


if __name__ == "__main__":
    main()
