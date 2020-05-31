import tensorflow as tf

a = tf.constant(5)
b = tf.constant(54)
c = tf.multiply(a, b)
d = tf.add(a, b)
f = tf.multiply(c, d)

print(f)
