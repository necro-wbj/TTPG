import tensorflow as tf
import numpy as np
arry=np.genfromtxt("1057.csv", delimiter=",")
arry=np.reshape(arry, (21,1))
arry2=np.genfromtxt("1058.csv", delimiter=",")
arry2=np.reshape(arry, (21,1))
x=tf.placeholder(tf.float32, [None,1])
y=tf.placeholder(tf.float32, [None,1])
l1 = tf.layers.dense(x, 10, tf.nn.relu)          # hidden layer
output = tf.layers.dense(l1, 1)
loss = tf.losses.sparse_softmax_cross_entropy(labels=y, logits=output)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.05)
train_op = optimizer.minimize(loss)
accuracy = tf.metrics.accuracy(          # return (acc, update_op), and create 2 local variables
    labels=tf.squeeze(y), predictions=tf.argmax(output, axis=1),)[1]
sess = tf.Session()
init_op = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
sess.run(init_op)
for step in range(100):
    # train and net output
    sess.run(train_op, {x: arry, y: arry2})
    if step % 2 == 0:
        # plot and show learning process
        sess.run(loss)
print("oK")