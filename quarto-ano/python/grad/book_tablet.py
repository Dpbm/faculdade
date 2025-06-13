import numpy as np

# [ rectangular, words, buttons ]

features = [
    np.matrix([ [1], [1], [0] ]), # book
    np.matrix([ [0], [1], [1] ]), # tablet
    np.matrix([ [1], [1], [1] ]), # tablet
    np.matrix([ [0], [1], [0] ])  # book
]

labels = [
    np.matrix([ [1], [0] ]),
    np.matrix([ [0], [1] ]),
    np.matrix([ [0], [1] ]),
    np.matrix([ [1], [0] ])
]

weights = np.random.random(size=(2,3))

def softmax(z):
    # from https://www.pinecone.io/learn/softmax-activation/
    exp_z = np.exp(z)
    total = exp_z.sum()
    softmax_z = np.round(exp_z/total,3)
    return softmax_z

get_loss = lambda y : y[0][0] ** 2 + y[1][0] ** 2
learning_rate = 0.01

for feature,label in zip(features, labels):
    error = np.matrix([[0], [0]])   

    while not(error[0][0] == label[0][0] and error[1][0] == label[1][0]):

        pred = np.dot(weights, feature)
        pred = softmax(pred)
        error = np.abs(pred - label)

        loss = get_loss(error)


        print(loss)


    print("=====")