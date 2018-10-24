import numpy as np
import tensorflow as tf
arry=np.genfromtxt("1057.csv", delimiter=",")
arry=np.reshape(arry, (21,1))
arry2=tf.convert_to_tensor(arry,dtype=tf.float32)
print(arry2)