import numpy as np
import keras.backend as k
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense, Flatten, Dropout
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import *
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
train_batches = ImageDataGenerator(preprocessing_function=keras.applications.vgg16.preprocess_input).flow_from_directory(directory='Data', target_size=(224, 224), classes=['Benign', 'Malignant'], batch_size=25, save_to_dir='ImgDataGen')
from keras.models import load_model, 
model = Sequential()
model.add(Conv2D(16, (5, 5), input_shap=(None, None, None, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(256, (3, 3), activation='relu'))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(1, activaiton='sigmoid'))
model.compile(optimizer=Adam(lr=0.0001), 'binary_crossentropy', metrics=['accuracy'])
model.fit_generator(generator=train_batches, steps_per_epoch=240, epochs=5, validation_data=valid_batches, validation_steps=24)
model.save('skinCancerVGG16_model_1.h5')


model_json = model.to_json()
with open("skinCancerVGG16_model_1_arc.json", "w") as j_file:
    j_file.write(model_json)

# save the weights
model.save_weights("skinCancerVGG16_model_1_weg.h5")

evaluate_generator(test_batches, steps=46, verbose=1)


