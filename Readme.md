===============================================================================
                      Flower Recognition System using ML
===============================================================================

Welcome to the Flower Recognition System! This project utilizes machine learning techniques to classify various types of flowers based on images.

===============================================================================
                           Project Setup Instructions
===============================================================================

Prerequisites:
- Python 3.x
- Jupyter Notebook
- Flask

Installation Steps:

1. Clone this repository to your local machine:

    git clone https://github.com/your-username/flower-recognition.git

2. Navigate to the project directory:

    cd flower-recognition

3. Set up a virtual environment (recommended):

    python -m venv .venv

4. Activate the virtual environment:
   - On Windows:

    .venv\Scripts\activate

   - On macOS/Linux:

    source .venv/bin/activate

5. Install the required dependencies:

    pip install -r requirements.txt

===============================================================================
                             Running the Flask App
===============================================================================

Follow these steps to start the Flask server:

1. Start the Jupyter Notebook environment:

    jupyter notebook

2. Activate the virtual environment (if not already activated):

    .venv\Scripts\activate   # For Windows
    # or
    source .venv/bin/activate   # For macOS/Linux

3. Run the Flask App:

    python -m flask --app .\app.py run

4. Once the server starts successfully, navigate to http://localhost:5000 in your web browser to access the Flower Recognition System.

===============================================================================
                                    Usage
===============================================================================

- Upload an image of a flower to the web application.
- The system will process the image and provide the predicted species of the flower.

===============================================================================
                                   Credits
===============================================================================

This project was developed by SONU SHARMA during the submission of  minor project  MCA 2023.

===============================================================================
                                   License
===============================================================================

This project is licensed under the [License Type] License - see the LICENSE file for details.
