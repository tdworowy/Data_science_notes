import tensorflow as tf

if __name__ == "__main__":
    (train_images, train_labels), (test_images, test_labels) = (
        tf.keras.datasets.mnist.load_data()
    )
    x = tf.keras.Input(dtype=tf.float32, shape=[None, 784])
    y = tf.keras.Input(dtype=tf.float32, shape=[None, 10])

    learning_rate = 0.1
    epochs = 10
    batch_size = 100

    w_xh = tf.Variable(tf.random.normal([784, 300], stddev=0.03), name="w_xh")
    b_h = tf.Variable(tf.random.normal([300]), name="b_h")

    w_hy = tf.Variable(tf.random.normal([300, 10], stddev=0.03), name="w_hy")
    b_y = tf.Variable(tf.random.normal([10]), name="b_y")

    z1 = tf.add(tf.matmul(x, w_xh), b_h)
    a1 = tf.nn.relu(z1)
    z2 = tf.add(tf.matmul(a1, w_hy), b_y)
    yhat = tf.nn.softmax(z2)

    cross_entropy = tf.reduce_mean(
        -tf.reduce_sum(y * tf.math.log(yhat), reduction_indices=[1])
    )

    optimiser = tf.keras.optimizers.SGD(learning_rate=learning_rate).minimize(
        cross_entropy, yhat
    )

    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(yhat, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    total_batch = int(len(train_labels) / batch_size)
    for epoch in range(epochs):
        avg_cost = 0

        for i in range(total_batch):
            train_images_next_batch = 0  # TODO get next batch of training set
            cost = 0  # TODO run to get cost
            avg_cost = cost / total_batch
            print(f"Epoch: {epoch + 1} cost: {avg_cost}")

# Conclusion use keras :)
