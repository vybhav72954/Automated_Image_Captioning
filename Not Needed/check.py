import tensorflow as tf
with tf.device('/gpu:0'):

    print(tf.__version__)

    # Construct a `Session` to execute the graph.
    with tf.compat.v1.Session() as sess:
        # Build a dataflow graph.
        c = tf.constant([[1.0, 2.0], [3.0, 4.0]])
        d = tf.constant([[1.0, 1.0], [0.0, 1.0]])
        e = tf.matmul(c, d)

        # Execute the graph and store the value that `e` represents in `result`.
        result = sess.run(e)
        print(result)
