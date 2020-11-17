from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
from math import ceil
#Initialize the CNN
classifier = Sequential()
#Convolution and Max pooling
classifier.add(Conv2D(32, (3, 3), input_shape = (150, 150, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2,2)))
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2,2)))
classifier.add(Conv2D(64, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2,2)))
 
#Flatten
classifier.add(Flatten())
 
#Full connection
classifier.add(Dense(64, activation = 'relu'))
classifier.add(Dense(10, activation = 'sigmoid'))
 
#Compile classifier
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
 
#Fitting CNN to the images
train_datagen = ImageDataGenerator(rescale=1./255, rotation_range=10, zoom_range=0.1, horizontal_flip=False,fill_mode="nearest") 
test_datagen = ImageDataGenerator(rescale=1./255, rotation_range=10,zoom_range=0.1, horizontal_flip=False,fill_mode="nearest")
training_set = train_datagen.flow_from_directory('./train', target_size=(150, 150), batch_size=40, class_mode='categorical')
test_set = test_datagen.flow_from_directory('./test', target_size=(150, 150), batch_size=40, class_mode='categorical')
print(len(training_set.filenames))

classifier.fit_generator(training_set, steps_per_epoch=(ceil(len(training_set.filenames)//40)), epochs=50, validation_data=test_set, validation_steps = (ceil(len(test_set.filenames)//40)))

#save model
classifier.save('model.h5')
classifier.save_weights('weights.h5')
