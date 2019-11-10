import tensorflow as tf

# Define a placeholder for input values
x = tf.placeholder(tf.float32, [None], name='x')

# Define a constant value used to shift input values
shift = tf.constant(10.0, dtype=tf.float32, name="shift")

# Compute shifted values
y = tf.add(x, shift, name="y")

# Initialize TensorFlow session
with tf.Session() as sess:

    # Specify values to feed into placeholder 'x'
    fd = { x : [1.,2.,3.] }

    # Run operation 'tf.add'
    y_vals = sess.run(y, feed_dict=fd)
