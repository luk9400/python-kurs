# task 2 & 3

import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1.0 - x)


_sigmoid = (sigmoid, sigmoid_derivative)


def relu(x):
    return np.maximum(0, x)


def relu_derivative(x):
    return 1 * (x > 0)


_relu = (relu, relu_derivative)


def tanh(x):
    return np.tanh(x)


def tanh_derivative(x):
    return 1.0 - x ** 2


_tanh = (tanh, tanh_derivative)


class NeuralNetwork:
    def __init__(self, layers, eta, output_shape=(1, 1)):
        self.layers = []
        self.output = np.zeros(output_shape)
        self.eta = eta

        for layer, next_layer in zip(layers[0:-1], layers[1:]):
            self.layers.append(
                NetworkLayer(layer["func"], (next_layer["size"], layer["size"]))
            )

        self.layers.append(
            NetworkLayer(layers[-1]["func"], (output_shape[0], layers[-1]["size"]))
        )

    def feedforward(self, x):
        self.layers[0].values = x

        for layer, next_layer in zip(self.layers[0:-1], self.layers[1:]):
            next_layer.values = layer.func(np.dot(layer.values, layer.weights.T))
        self.output = self.layers[-1].func(
            np.dot(self.layers[-1].values, self.layers[-1].weights.T)
        )

    def backprop(self, y):
        deltas = []

        delta = (y - self.output) * self.layers[-1].func_derivative(self.output)
        deltas.append(self.eta * np.dot(delta.T, self.layers[-1].values))

        for layer, prev_layer in zip(
            reversed(self.layers[0:-1]), reversed(self.layers[1:])
        ):
            delta = layer.func_derivative(prev_layer.values) * np.dot(
                delta, prev_layer.weights
            )
            deltas.append(self.eta * np.dot(delta.T, layer.values))

        for layer, weight in zip(self.layers, reversed(deltas)):
            layer.weights += weight

    def training(self, iterations, input, expected_output):
        for _ in range(iterations):
            self.feedforward(input)
            self.backprop(expected_output)


class NetworkLayer:
    def __init__(self, func, shape):
        self.func, self.func_derivative = func
        self.weights = np.random.standard_normal(shape)
        self.values = np.zeros((shape[1]))


tests = [
    {
        "name": "Parabola, two layers",
        "layers": [{"func": _sigmoid, "size": 1}, {"func": _sigmoid, "size": 10}],
        "x": np.linspace(-50, 50, 26),
        "test_x": np.linspace(-50, 50, 100),
        "func": lambda x: x ** 2,
        "eta": 0.5,
    },
    {
        "name": "Sine, two layers",
        "layers": [{"func": _tanh, "size": 1}, {"func": _tanh, "size": 10}],
        "x": np.linspace(0, 2, 21),
        "test_x": np.linspace(0, 2, 161),
        "func": lambda x: np.sin((3 * np.pi / 2) * x),
        "eta": 0.01,
    },
    {
        "name": "Parabola, three layers",
        "layers": [
            {"func": _sigmoid, "size": 1},
            {"func": _sigmoid, "size": 10},
            {"func": _sigmoid, "size": 10},
        ],
        "x": np.linspace(-50, 50, 26),
        "test_x": np.linspace(-50, 50, 100),
        "func": lambda x: x ** 2,
        "eta": 0.1,
    },
    {
        "name": "Sine, three layers",
        "layers": [
            {"func": _tanh, "size": 1},
            {"func": _tanh, "size": 10},
            {"func": _tanh, "size": 10},
        ],
        "x": np.linspace(0, 2, 21),
        "test_x": np.linspace(0, 2, 161),
        "func": lambda x: np.sin((3 * np.pi / 2) * x),
        "eta": 0.01,
    },
]


def mse(expected, actual):
    return sum(
        [(result - actual[index]) ** 2 for index, result in enumerate(expected)]
    ) / len(expected)


def plot(test):
    nn = NeuralNetwork(test["layers"], test["eta"])
    rng = test["x"] / max(test["x"])
    img = test["func"](rng)

    X = np.reshape(rng, (len(rng), 1))
    y = np.reshape(img, (len(img), 1))

    test_x = test["test_x"] / max(test["test_x"])
    test_y = test["func"](test_x)
    test_X = np.reshape(test_x, (len(test_x), 1))

    fig = plt.figure()
    original = fig.add_subplot(2, 1, 1)
    original.set_title(test["name"])
    original.scatter(rng, y)

    new = fig.add_subplot(2, 1, 2)
    new.set_title("Aproksymacja")

    for i in range(50):
        nn.training(100, X, y)
        nn.feedforward(test_X)
        new.clear()
        new.set_xlabel(f"{i*100} iteracji\nMSE: {mse(test_y, nn.output)}")
        new.scatter(test_x, nn.output)
        plt.pause(0.01)

    plt.show()


def main():
    for test in tests:
        plot(test)


if __name__ == "__main__":
    main()

# dodanie 3 warstwy polepsza rezultaty
