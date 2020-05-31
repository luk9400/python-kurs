import numpy as np


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


class NeuralNetwork:
    def __init__(self, x, y, func1, func2):
        self.input = x
        self.weights1 = np.random.rand(4, self.input.shape[1])
        self.weights2 = np.random.rand(1, 4)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = 0.5
        self.func1, self.func1_derivative = func1
        self.func2, self.func2_derivative = func2

    def feedforward(self):
        self.layer1 = self.func1(np.dot(self.input, self.weights1.T))
        self.output = self.func2(np.dot(self.layer1, self.weights2.T))

    def backprop(self):
        delta2 = (self.y - self.output) * self.func2_derivative(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)
        delta1 = self.func1_derivative(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)
        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def training(self):
        for _ in range(5000):
            self.feedforward()
            self.backprop()


def error(y, output):
    return np.linalg.norm(y - output)


def test(x, y):
    nn = NeuralNetwork(x, y, _sigmoid, _sigmoid)
    nn.training()
    
    print("sigmoid, sigmoid:")
    print("output:\n", nn.output)
    print("error:", error(y, nn.output))


    nn = NeuralNetwork(x, y, _sigmoid, _relu)
    nn.training()
    print("sigmoid, relu:")
    print("output:\n", nn.output)
    print("error:", error(y, nn.output))

    nn = NeuralNetwork(x, y, _relu, _relu)
    nn.training()
    print("relu, relu:")
    print("output:\n", nn.output)
    print("error:", error(y, nn.output))

    nn = NeuralNetwork(x, y, _relu, _sigmoid)
    nn.training()
    print("relu, sigmoid:")
    print("output:\n", nn.output)
    print("error:", error(y, nn.output))


if __name__ == "__main__":
    X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])

    print("XOR")
    y = np.array([[0], [1], [1], [0]])
    test(X, y)

    print("AND")
    y = np.array([[0], [0], [0], [1]])
    test(X, y)

    print("OR")
    y = np.array([[0], [1], [1], [1]])
    test(X, y)

# ostatnia kolumna to bias
