# Import
import numpy as np
import pyswarms as ps
from sklearn.datasets import load_iris

run_NeuralNet = True
if run_NeuralNet:
    # Working with Neural Networks
    data = load_iris()
    X = data.data
    y = data.target

    n_inputs = 4
    n_hidden = 20
    n_classes = 3

    num_samples = 150

    def logits_function(p):
        # Roll-back the weights and biases
        W1 = p[0:80].reshape((n_inputs, n_hidden))
        b1 = p[80:100].reshape((n_hidden,))
        W2 = p[100:160].reshape((n_hidden, n_classes))
        b2 = p[160:163].reshape((n_classes,))

        # Perform forward propagation
        z1 = X.dot(W1) + b1
        a1 = np.tanh(z1)
        logits = a1.dot(W2) + b2
        return logits

    # Forward propagation
    def forward_prop(params):
        logits = logits_function(params)

        # Compute for the softmax of the logits
        exp_scores = np.exp(logits)
        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

        # Compute for the negative log likelihood
        corect_logprobs = -np.log(probs[range(num_samples), y])
        loss = np.sum(corect_logprobs) / num_samples
        return loss


    def f(x):
        n_particles = x.shape[0]
        j = [forward_prop(x[i]) for i in range(n_particles)]
        return np.array(j)

    # Initialize swarm
    options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}

    # Call instance of PSO
    dimensions = (n_inputs * n_hidden) + (n_hidden * n_classes) + n_hidden + n_classes
    optimizer = ps.single.GlobalBestPSO(n_particles=100, dimensions=dimensions, options=options)

    # Perform optimization
    cost, pos = optimizer.optimize(f, iters=1000)

    def predict(pos):
        """
        Use the trained weights to perform class predictions.

        Inputs
        ------
        pos: numpy.ndarray
            Position matrix found by the swarm. Will be rolled
            into weights and biases.
        """
        logits = logits_function(pos)
        y_pred = np.argmax(logits, axis=1)
        return y_pred


    print(f"Accuracy: {(predict(pos) == y).mean()}")