#!/usr/bin/python

import numpy as np
import pandas as pd


def populate_matrix(df, users, m):
    x = []
    for i in users:
        row = []
        for j in range(2, m + 2):
            j = df.loc[(df["userId"] == i) & (df["movieId"] == j)]["rating"].tolist()
            if j == []:
                row.append(0.0)
            else:
                row.append(*j)
        x.append(row)
    return np.array(x)


def main():
    df = pd.read_csv("./ml-latest-small/ratings.csv", sep=",")

    # list of users who rated ToyStory
    users = df.loc[df["movieId"] == 1]["userId"].tolist()

    # list of our users' ToyStory ratings
    tmp = df.loc[(df["userId"].isin(users)) & (df["movieId"] == 1)]["rating"].tolist()

    y = []
    for i in tmp:
        y.append([i])

    x = populate_matrix(df, users, 10)

    print(np.linalg.lstsq(x, y))


if __name__ == "__main__":
    main()
