# sample: create a Wide & Deep net and warm-start the wide part

import tensorflow as tf

input_shape = (10,)
input_layer = tf.keras.layers.Input(shape=input_shape)

wide_part = tf.keras.layers.Dense(64, activation="relu")(input_layer)
wide_part = tf.keras.layers.Dense(32, activation="relu")(wide_part)
wide_part = tf.keras.layers.Dense(16, activation="relu")(wide_part)

deep_part = tf.keras.layers.Dense(32, activation="relu")(input_layer)
deep_part = tf.keras.layers.Dense(64, activation="relu")(deep_part)
deep_part = tf.keras.layers.Dense(128, activation="relu")(deep_part)

combined = tf.keras.layers.concatenate([wide_part, deep_part])

output_layer = tf.keras.layers.Dense(1, activation="sigmoid")(combined)

model = tf.keras.models.Model(inputs=input_layer, outputs=output_layer)

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Pre-initialize the wide part of the network using linear regression
x_train = NotImplementedError()
y_train = NotImplementedError()

wide_part_model = tf.keras.models.Sequential(
    [tf.keras.layers.Dense(1, input_shape=(input_shape[0],), activation="linear")]
)
wide_part_model.compile(optimizer="adam", loss="mean_squared_error")
wide_part_model.fit(x_train, y_train, epochs=10)

wide_part_weights = [
    wide_part_model.layers[0].get_weights()[0],
    wide_part_model.layers[0].get_weights()[1],
]
model.layers[1].set_weights(wide_part_weights)
