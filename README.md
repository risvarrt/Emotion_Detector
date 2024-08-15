Here's an updated version of the README file with additional details about the CNN architecture built using Keras:

```markdown
# Emotion Detector

This project is an Emotion Detection web application built using Flask and a Convolutional Neural Network (CNN) implemented with Keras. The application is capable of identifying human emotions from images, such as happy, sad, angry, surprised, and more.

## Project Links

- **Repository**: [Emotion Detector](https://github.com/risvarrt/Emotion_Detector/tree/main)

## Features

- **Emotion Detection**: Detects emotions from images uploaded by the user.
- **Real-Time Detection**: Capable of processing live camera input to detect emotions in real-time.
- **User-Friendly Interface**: Simple and intuitive web interface built using Flask.


## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/risvarrt/Emotion_Detector.git
   ```
2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Flask application**:
   ```bash
   python app.py
   ```
4. **Open your web browser and go to** `http://127.0.0.1:5000/` **to use the application**.

## Technical Details

### Tech Stack

- **Flask**: A micro web framework for Python used to build the web application.
- **Keras with TensorFlow Backend**: Used for building and training the Convolutional Neural Network (CNN) model.
- **OpenCV**: Used for image processing and real-time video capture.
- **HTML/CSS**: For the frontend design of the web interface.

### Project Structure

- **app.py**: The main Flask application file that handles routing and emotion detection logic.
- **model.h5**: The pre-trained CNN model used for emotion detection.
- **static/**: Contains static files like CSS and images used in the web application.
- **templates/**: Contains HTML templates for the web pages.
- **assets/**: This folder contains the images and other assets used in the project.

### CNN Model Overview

The Emotion Detector uses a Convolutional Neural Network (CNN) trained on a dataset of facial expressions to classify emotions. The model is implemented using **Keras** with a TensorFlow backend.

#### CNN Architecture:

- **Input Layer**: Accepts input images resized to 48x48 pixels in grayscale.
- **Convolutional Layers**: Multiple convolutional layers with ReLU activation are used to extract features from the input images. Each convolutional layer is followed by a pooling layer.
- **Pooling Layers**: Max pooling layers are used to downsample the feature maps, reducing the spatial dimensions and controlling overfitting.
- **Dropout Layers**: Dropout is applied to prevent overfitting by randomly setting a fraction of input units to 0 at each update during training.
- **Fully Connected Layers**: The flattened output from the convolutional layers is fed into fully connected (dense) layers.
- **Output Layer**: The final output layer uses a softmax activation function to classify the input into one of the emotion categories.

### How it Works:

1. **Image Input**: The user can upload an image or use their webcam to capture a real-time image.
2. **Preprocessing**: The input image is processed to fit the model's input requirements (e.g., resizing to 48x48 pixels, grayscale conversion).
3. **Emotion Detection**: The processed image is fed into the CNN model, which predicts the emotion.
4. **Result Display**: The predicted emotion is displayed on the web interface.

### Key Functions

- **load_model()**: Loads the pre-trained CNN model from the `model.h5` file.
- **preprocess_image(image)**: Preprocesses the input image for the CNN model, including resizing and grayscale conversion.
- **predict_emotion(image)**: Predicts the emotion from the processed image using the CNN model.

## Model Training

The CNN model was trained using the **FER-2013** dataset, which contains labeled images of facial expressions across several emotion categories. The training process involved the following steps:

1. **Data Augmentation**: To improve the model's generalization, data augmentation techniques like rotation, zoom, and horizontal flipping were applied to the training images.
2. **Model Compilation**: The model was compiled using the Adam optimizer with categorical cross-entropy as the loss function, which is standard for multi-class classification problems.
3. **Training**: The model was trained over multiple epochs, with the training and validation accuracy monitored to avoid overfitting.
4. **Model Evaluation**: The model was evaluated on a validation set to ensure its accuracy and robustness.
