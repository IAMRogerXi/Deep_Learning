import tensorflow as tf

hello = tf.constant('fuck')
sess = tf.Session()
print(sess.run(hello))