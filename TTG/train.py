import cupy as cp
cp.cuda.Memory(6553600000)


def TTTG_Network(inputs, weight, baise, weight2, baise2, weight3, baise3, weight4, baise4, L, answers, train, print_result=False):
    hidden = inputs.dot(weight) + baise
    hidden = cp.reciprocal(1 + cp.exp(-hidden))  # sigmoid
    hidden2 = hidden.dot(weight2) + baise2
    hidden2 = cp.reciprocal(1 + cp.exp(-hidden2))  # sigmoid
    hidden3 = hidden2.dot(weight3) + baise3
    hidden3 = cp.reciprocal(1 + cp.exp(-hidden3))  # sigmoid
    # hidden = hidden / (1 + cp.absolute(hidden))  # TanH
    output = hidden3.dot(weight4) + baise4
    output = cp.reciprocal(1 + cp.exp(-output))  # sigmoid
    # output = output / (1 + cp.absolute(output))  # TanH
    # Relu
    # hidden = inputs.dot(weight.T) + baise
    # hidden = cp.maximum(hidden, 0)
    # output = hidden.dot(weight2.T)
    # output = cp.maximum(output, 0)
    # print(hidden)
    Error = cp.square(answers - output).sum()
    if train:
        # print("weight:")
        # print(weight)
        # print("weight2:")
        # print(weight2)
        weight4, baise4, weight3, baise3, weight2, baise2, weight, baise = training(
            answers, weight, output, weight2, weight3, weight4, inputs, hidden, hidden2, hidden3, baise, baise2, baise3, baise4, L)
        # output[output >= 0.5] = 1  # AND閘最佳化
        # output[output < 0.5] = 0  # AND閘最佳化
    # return Error.tolist(), output.tolist(), output.tolist()  # AND閘返回結果
    return Error, cp.argmax(output, 1), output


def training(answers, weight, output, weight2, weight3, weight4, inputs, hidden, hidden2, hidden3, baise, baise2, baise3, baise4, L):
    # sigmoid
    E = (answers - output) * output * (1 - output)
    E2 = hidden3 * (1 - hidden3) * E.dot(weight4.T)
    E3 = hidden2 * (1 - hidden2) * E2.dot(weight3.T)
    E4 = hidden * (1 - hidden) * E3.dot(weight2.T)
    weight4 += L * hidden3.T.dot(E)
    baise4 += L * E.sum()
    weight3 += hidden2.T.dot(E2) * L
    baise3 += L * E2.sum()
    weight2 += hidden.T.dot(E3) * L
    baise2 += L * E3.sum()
    weight += inputs.T.dot(E4) * L
    baise += L * E4.sum()
    return weight4, baise4, weight3, baise3, weight2, baise2, weight, baise
    # Softsign...............................
    # E = (answers - output) * 1 / cp.square(1 + (1.0 - cp.absolute(output)))
    # E2 = 1 / cp.square(1 + (1.0 - cp.absolute(hidden))) * E.dot(weight2.T)
    # weight2 += hidden.T.dot(E) * L
    # weight += inputs.T.dot(E2) * L
    # baise += E2.T.dot(cp.ones((train_datas))) * L
    # Relu
    # E = 2.0 * (answers - output)
    # for i in range(E.size):
    #     weight2[i] += L * hidden * E[i]
    # E2 = E.dot(weight2)
    # E2[hidden < 0] = 0
    # for i in range(E2.size):
    #     weight += L * inputs * E2[i]
    # baise += L * E2
