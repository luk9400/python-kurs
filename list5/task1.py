#!/usr/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def get_X(df, users, m):
    X_data = df.loc[
        (df.userId.isin(users)) & (df.movieId > 1) & (df.movieId <= m),
        ["userId", "movieId", "rating"],
    ].to_numpy()

    X = np.zeros((len(users), m))
    for userId, movieId, rating in X_data:
        index = np.where(users == userId)[0][0]
        X[index, int(movieId) - 2] = rating

    return X


def get_Y(df, users, m):
    return df.loc[
        (df["userId"].isin(users)) & (df["movieId"] == 1), ["rating"]
    ].to_numpy()


def first(df, users):
    for m in [10, 100, 10000]:
        y = get_Y(df, users, m)
        x = get_X(df, users, m)

        model = LinearRegression().fit(x, y)

        predicted = plt.scatter(
            [i for i in range(len(users))],
            [model.predict([x[i]]) for i in range(len(users))],
            alpha=0.5,
            c="b",
        )
        real = plt.scatter(
            [i for i in range(len(users))],
            [y[i] for i in range(len(users))],
            alpha=0.5,
            c="r",
        )

        plt.legend((predicted, real), ["Predicted", "Real"])
        plt.title(f"Predictions for {m} movies")
        plt.show()


def second(df, users):
    for m in [10, 100, 200, 500, 1000, 10000]:
        x = get_X(df, users, m)
        y = get_Y(df, users, m)

        test_x = x[:200]
        test_y = y[:200]

        model = LinearRegression().fit(test_x, test_y)

        print("Prediction for", m, "movies:")
        for i in range(200, 215):
            print(i + 1, ":", *model.predict([x[i]]), "vs", y[i])


def main():
    df = pd.read_csv("./ml-latest-small/ratings.csv", sep=",")

    # list of users who rated ToyStory
    users = df.loc[df["movieId"] == 1]["userId"].tolist()

    first(df, users)
    second(df, users)


if __name__ == "__main__":
    main()
