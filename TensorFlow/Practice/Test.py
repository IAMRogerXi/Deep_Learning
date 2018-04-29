import pandas as pd
import tensorflow as tf

hello = tf.constant('fuck')
sess = tf.Session()
print(sess.run(hello))
a = tf.constant(20)
b = tf.constant(22)
print('a + b = {0}'.format(sess.run(a + b)))

anotherConstant = tf.constant(1, tf.int32, shape=[1, 2, 1])
print(sess.run(anotherConstant))