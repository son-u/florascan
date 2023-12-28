from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
from keras.preprocessing import image

app = Flask(__name__)


model = tf.keras.models.load_model('flower_model.h5')

# Function to preprocess uploaded image
def preprocess_image(image_path):
    test_image = image.load_img(image_path, target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    return test_image


@app.route('/')
def index():
    return render_template('index.html')

# Predict function
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img_path = 'static/temp.jpg' 
        file.save(img_path)
        processed_image = preprocess_image(img_path)
        result = model.predict(processed_image)

        flower_labels = {
            0: 'Daisy',
            1: 'Lotus',
            2: 'Orchid',
            3: 'Sunflower',
            4: 'Tulip'
        }
        
        predicted_label = flower_labels[np.argmax(result)]
        
        return render_template('pp.html', prediction=predicted_label)

if __name__ == '__main__':
    app.run(debug=True)