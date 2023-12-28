import numpy as np
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

def display_predictions(test_dir, model_path):
    # Assuming categories is a list containing class names
    categories = ['Daisy', 'Dandelion', 'Rose', 'Sunflower', 'Tulip']

    # Load your trained model
    cnn = tf.keras.models.load_model(model_path)

    # Load and preprocess the test data using ImageDataGenerator
    test_datagen = ImageDataGenerator(rescale=1./255)
    test_set = test_datagen.flow_from_directory(
        test_dir,
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical',
        shuffle=False
    )

    # Get true labels from the test set
    y_test = test_set.classes

    # Make predictions on the test set
    predictions = cnn.predict(test_set)

    # Display only predictions for the 'Rose' class
    plt.figure(figsize=(9, 9))
    count = 0
    for i, (img, label) in enumerate(test_set):
        if np.argmax(label[0]) == categories.index('Rose'):
            plt.subplot(3, 3, count + 1)
            plt.imshow(img[0])
            plt.xlabel('Actual:' + categories[np.argmax(label[0])] + '\n' + 'Predicted:' + categories[np.argmax(predictions[i])])
            plt.xticks([])
            plt.yticks([])
            count += 1
            if count == 9:
                break

    plt.tight_layout()
    plt.show()

# Usage example:
# Replace 'test_set' with your test set directory and 'flower_model.h5' with your model path
display_predictions('test_set', 'flower_model.h5')
