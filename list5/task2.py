#!/usr/bin/python

import numpy as np
import pandas as pd


def recommendation(x, y):
    z = np.dot(x / np.linalg.norm(x, axis=0), y / np.linalg.norm(y))

    X = x / np.linalg.norm(x, axis=0)
    Z = z / np.linalg.norm(z)

    return np.dot(X.T, Z)


def main():
    df = pd.read_csv("./ml-latest-small/ratings.csv", sep=",")
    df = df.loc[df["movieId"] < 10000]


    my_ratings = np.zeros((9019, 1))
    my_ratings[2571] = 5      # 2571 - Matrix
    my_ratings[32] = 4        # 32 - Twelve Monkeys
    my_ratings[260] = 5       # 260 - Star Wars IV
    my_ratings[1097] = 4


    x = np.array([[5, 0, 2, 5], [4, 1, 2, 5]]).T
    y = np.array([[4], [3]])
    print(recommendation(x, y))


if __name__ == "__main__":
    main()
