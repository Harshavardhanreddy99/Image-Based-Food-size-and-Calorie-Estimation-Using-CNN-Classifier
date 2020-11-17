


class CNN:
    def detect(tagetimage):

        import numpy as np
        import operator

        from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
        from keras.models import Sequential, load_model
        from keras.preprocessing import image
        #load model

        #Prediction on a new picture
        from keras.preprocessing import image as image_utils

        from PIL import Image, ImageTk
        import tensorflow as tf
        from keras import backend as K 



        tf.keras.backend.clear_session()
        
        
        
        model_path = 'C:\\Users\\14694\\Desktop\\django\\FoodCalorie\\webapp\\model.h5'
        model_weights_path = 'C:\\Users\\14694\\Desktop\\django\\FoodCalorie\\webapp\\weights.h5'
        model = load_model(model_path)
        model.load_weights(model_weights_path)

        
        class_labels = ['beignets', 'chicken_wings', 'french_fries', 'fried_rice', 'macarons', 'mussels', 'eggs_benedict', 'pancakes', 'pizza', 'steak']
        test_image = image.load_img(tagetimage, target_size = (150, 150))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
    
        
        test_image /= 255
        result = model.predict(test_image)
        decoded_predictions = dict(zip(class_labels, result[0]))
        decoded_predictions = sorted(decoded_predictions.items(), key=operator.itemgetter(1), reverse=True)

        
        
        count = 1
        food=""
        for key, value in decoded_predictions[:10]:
            #print("{}. {}: {:8f}%".format(count, key, value*100))
            print(key)
            food=key

            break
            count+=1
        del model
        K.clear_session()

        return food

"""if __name__ == '__main__':
    c=CNN()
    tagetimage='44.jpg'
    print(c.detect(tagetimage),'----------')
   
"""
