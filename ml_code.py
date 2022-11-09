import numpy
import keras.datasets.mnist
import keras.optimizers
import keras.models
import keras.layers

# Source - https://www.tensorflow.org/datasets/catalog/mnist
(x_train, y_train), (x_validation, y_validation) = keras.datasets.mnist.load_data()

# Followed this tutorial to implement our project
# https://www.tensorflow.org/quantum/tutorials/mnist
x_train = x_train.reshape(60000, 784)
x_validation = x_validation.reshape(10000, 784)
x_train = x_train.astype('float32') / 255
x_validation = x_validation.astype('float32') / 255

# Followed this source for training and prediction of the given MNIST dataset
# https://www.analyticsvidhya.com/blog/2021/06/mnist-dataset-prediction-using-keras/
y_train = keras.utils.to_categorical(y_train, 10)
y_validation = keras.utils.to_categorical(y_validation, 10)

# Used this source also for training dataset
# https://keras.io/api/layers/regularization_layers/dropout/
model = keras.models.Sequential()
model.add(keras.layers.Dense(512, activation='relu', input_shape=(784,)))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(512, activation='relu'))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer=keras.optimizers.RMSprop(),
              metrics=['accuracy'])

history = model.fit(x_train, y_train,
                    batch_size=128,
                    epochs=20,
                    verbose=1,
                    validation_data=(x_validation, y_validation))

score = model.evaluate(x_validation, y_validation, verbose=0)
print('Model accuracy:', score[1])

# Link used to save the model as HDF5 file
# Source - https://www.tensorflow.org/guide/keras/save_and_serialize
model.save(r"C:\Users\pkbhat\Downloads\CSE_535_MC\MLModel\model.h5")
# C:\Users\pkbhat\Downloads\CSE_535_MC\MLModel

ml_model = keras.models.load_model(r"C:\Users\pkbhat\Downloads\CSE_535_MC\MLModel\model.h5")
predicted_digit = ml_model.predict(numpy.array([x_validation[9, :]]) > 0.5).astype('int32')[0]
# print(predicted_label)
ans = 0
for i in range(len(predicted_digit)):
    if predicted_digit[i] == 1:
        ans = i
print(ans)
