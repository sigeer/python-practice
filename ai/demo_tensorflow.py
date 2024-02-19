import tensorflow as tf  
from tensorflow.keras.models import Sequential  
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten  
from tensorflow.keras.preprocessing.image import ImageDataGenerator  
import numpy as np  
import matplotlib.pyplot as plt  
import os

model_dir = "./model"
model = None
img_width, img_height = 150, 150  
train_data_dir = "./imaesData"
validation_data_dir = "./validateData"
chech_file = './check/check_file.png'

if os.path.exists(model_dir):
    model = tf.keras.models.load_model(model_dir)
else: 
    # 图像归一化  
    nb_train_samples = 2000  
    nb_validation_samples = 800  
    epochs = 10 
    batch_size = 2 
    
    if tf.keras.backend.image_data_format() == 'channels_first':  
        input_shape = (3, img_width, img_height)  
    else:  
        input_shape = (img_width, img_height, 3)  

    # 创建模型  
    model = Sequential()  
    model.add(Conv2D(32, (3, 3), input_shape=input_shape, activation='relu'))  
    model.add(MaxPooling2D(pool_size=(2, 2)))  
    model.add(Dropout(0.25))  
    model.add(Conv2D(32, (3, 3), activation='relu'))  
    model.add(MaxPooling2D(pool_size=(2, 2)))  
    model.add(Dropout(0.25))  
    model.add(Flatten())  
    model.add(Dense(64, activation='relu'))  
    model.add(Dropout(0.5))  
    model.add(Dense(4, activation='softmax'))  # 根据你的任务，可能需要更改最后一层激活函数  
    
    # 编译模型  
    model.compile(loss='categorical_crossentropy',  # 根据你的任务，可能需要更改损失函数  
                optimizer='adam',  
                metrics=['accuracy'])  
    
    # 数据增强  
    train_datagen = ImageDataGenerator(  
        rescale=1. / 255,  
        shear_range=0.2,  
        zoom_range=0.2,  
        horizontal_flip=True)  
    
    test_datagen = ImageDataGenerator(rescale=1. / 255)  
    
    train_generator = train_datagen.flow_from_directory(  
        train_data_dir,  
        target_size=(img_width, img_height),  
        batch_size=batch_size,  
        class_mode='categorical')  
    
    validation_generator = test_datagen.flow_from_directory(  
        validation_data_dir,  
        target_size=(img_width, img_height),  
        batch_size=batch_size,  
        class_mode='categorical')  
    
    # 训练模型  
    model.fit(  
        train_generator,  
        steps_per_epoch=train_generator.samples // batch_size,  
        epochs=epochs,  
        validation_data=validation_generator,  
        validation_steps=validation_generator.samples // batch_size)

    model.save(model_dir)



# 对新图像进行预测
new_image = tf.keras.preprocessing.image.load_img(chech_file, target_size=(img_width, img_height))
new_image = tf.keras.preprocessing.image.img_to_array(new_image)
new_image = new_image.reshape((1,) + new_image.shape) / 255.0

dir_list = os.listdir(train_data_dir)
print(dir_list)

# 输出预测结果
prediction = model.predict(new_image)
predicted_class = prediction.argmax(axis=-1)
print("Predicted class:", predicted_class)
print("predicted_class[0]:", predicted_class[0])
print("dir_list[predicted_class[0]]:", dir_list[predicted_class[0]])

