'''


@author: Necro
'''
import tensorflow as tf
import numpy as np
xdata = np.random.rand(100).astype(np.float32)
ydata=0.3*xdata+0.1

weight=tf.Variable([0.])
bias=tf.Variable([0.])
y=weight*xdata+bias

#loss=tf.reduce_mean(tf.square(y-ydata))
loss=tf.losses.mean_squared_error(y, ydata)
# optimizer=tf.train.GradientDescentOptimizer(0.1)
optimizer=tf.train.AdamOptimizer(1)
train=optimizer.minimize(loss)

init=tf.global_variables_initializer()
sess=tf.Session()
sess.run(init)

R=100
print(sess.run(weight),sess.run(bias))
for step in range(R) :
    sess.run(train)
    if step % 50 == 0:
        print(sess.run(weight),sess.run(bias))

# 
# for step in range(R) :
#     sess.run(optimizer.minimize(tf.losses.absolute_difference(y, ydata)))
# 
# print(sess.run(weight),sess.run(bias))
# 
# for step in range(R) :
#     sess.run(optimizer.minimize(tf.losses.compute_weighted_loss(y, ydata)))
# 
# print(sess.run(weight),sess.run(bias))
# 
# for step in range(R) :
#     sess.run(optimizer.minimize(tf.losses.hinge_loss(y, ydata)))
# 
# print(sess.run(weight),sess.run(bias))
# 
# for step in range(R) :
#     sess.run(optimizer.minimize(tf.losses.huber_loss(y, ydata)))
# 
# print(sess.run(weight),sess.run(bias))
# 
# for step in range(R) :
#     sess.run(optimizer.minimize(tf.losses.log_loss(y, ydata)))
# 
# print(sess.run(weight),sess.run(bias))
# 
# for step in range(R) :
#     sess.run(optimizer.minimize(tf.losses.mean_pairwise_squared_error(y, ydata)))
# 
# print(sess.run(weight),sess.run(bias))
# 
# for step in range(R) :
#     sess.run(optimizer.minimize(tf.losses.sigmoid_cross_entropy(y, ydata)))
# 
# print(sess.run(weight),sess.run(bias))