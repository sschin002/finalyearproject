import tensorflow as tf
from tensorflow.keras.applications.vgg16 import preprocess_input
import os
from PIL import Image
import numpy as np

# Load pre-trained ViT model
model = tf.keras.applications.VGG16(weights='imagenet', include_top=False)

# Define image directory
image_directory = 'new'

# Define image target size
target_size = (224, 224)

# Function to preprocess an image
def preprocess_image(image_path):
    # Load and preprocess the image
    image = Image.open(image_path)
    image = image.resize(target_size)
    image_array = np.array(image)
    image_array = preprocess_input(image_array)
    
    # Reshape the image array
    image_array = image_array.reshape((1, image_array.shape[0], image_array.shape[1], image_array.shape[2]))
    
    return image_array

# Process images in the directory
preprocessed_images = []
for image_filename in os.listdir(image_directory):
    if image_filename.endswith('.jpg') or image_filename.endswith('.png'):
        image_path = os.path.join(image_directory, image_filename)
        preprocessed_image = preprocess_image(image_path)
        preprocessed_images.append(preprocessed_image)

# Convert the list of preprocessed images to a single array
input_images = np.concatenate(preprocessed_images, axis=0)

# Use the preprocessed images as input to the pre-trained ViT model
features = model.predict(input_images)

# 'features' now contains the extracted features from the pre-trained model
print("Features shape:", features.shape)
