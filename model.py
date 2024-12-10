# Importing required libs
from keras.models import load_model
# from keras.utils import img_to_array
import numpy as np
from PIL import Image
from skimage.color import rgb2lab, lab2rgb
from skimage.io._io import imsave,imshow
import tensorflow as tf
from skimage.transform import resize
# Loading model
# importing pickle
import pickle
model = load_model("C:\\Users\\Vivek\\Desktop\\College\\Minor Project\\colorization_main\\colorization_main\\colorization\\models\\model.h5",compile=False)

# Preparing and pre-processing the image
def preprocess_img(img_path,temp):
    try:
        colorizer = []
        img = tf.keras.utils.img_to_array(
                tf.keras.utils.load_img(img_path))  # importing the test data
        img = resize(img, (256, 256))  # resizing the image to 256*256
        # Save resized black and white image
        grayscale_img = rgb2lab(1.0 / 255 * img)[:, :, 0]  # extracting the grayscale part
        grayscale_img = grayscale_img.astype('uint8')  # converting to uint8 for saving
        imsave("C:\\Users\\Vivek\\Desktop\\College\\Minor Project\\colorization_main\\colorization_main\\colorization\\results\\" + temp + "_bw.png",grayscale_img)
        colorizer.append(img)
        colorizer = np.array(colorizer, dtype='uint8')
        colorizer = rgb2lab(1.0 / 255 * colorizer)[:, :, :, 0]  # storing the grayscale part in colorizer
        colorizer = colorizer.reshape(colorizer.shape + (1,))
        print(colorizer.shape)
        output = model.predict(colorizer)  # predicting the colors i.e. A and  B channels
        output = output * 128
        for i in range(len(output)):
            result = np.zeros((256, 256, 3))  # initializing empty array
            result[:, :, 0] = colorizer[i][:, :, 0]  # storing grayscale part in result's zeroth channel
            result[:, :, 1:] = output[i]  # storing A and B color channel in 1 and 2 channel respectively
            result = lab2rgb(result)
            result = (result * 255).astype('uint8')
            imsave("C:\\Users\\Vivek\\Desktop\\College\\Minor Project\\colorization_main\\colorization_main\\colorization\\results\\" + temp+str(i) + ".png", result)

    except Exception as e:
        print(f"An exception occurred: {e}")