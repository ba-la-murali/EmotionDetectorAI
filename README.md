# Emotion Detection Application

## Overview

This project is a Python-based Emotion Detection application that leverages IBM's Watson NLP library. The application analyzes text input to determine the underlying emotions and returns the results in a structured format. The project includes tasks that guide the creation, testing, packaging, and deployment of the application.
 
## Project Setup

1. **Prerequisites**:
   - Python 3.11
   - Requests library (if not installed, use `python3.11 -m pip install requests`)

2. **File Structure**:
   - `final_project/`
     - `emotion_detection.py`
     - `test_emotion_detection.py`
     - `server.py`
     - `__init__.py`
     - `templates/`
       - `index.html`
     - `static/`
       - `mywebscript.js`
 

## Application Structure

### 1. `emotion_detection.py`

This script contains the core functionality of the application. It includes the `emotion_detector` function, which sends a POST request to the Watson NLP Emotion Predict function and returns the detected emotions.

- **Function**: `emotion_detector(text_to_analyze: str) -> dict`
  - **Parameters**: 
    - `text_to_analyze` (str): The text to be analyzed.
  - **Returns**: 
    - A dictionary containing the emotion scores and the dominant emotion.

### 2. `test_emotion_detection.py`

This file includes unit tests to validate the accuracy of the emotion detection application.

### 3. `server.py`

This script is used to deploy the application as a web service using Flask. It provides a web interface for users to input text and receive emotion analysis.

## Usage

### Emotion Detection

1. **Function Call**: The `emotion_detector` function can be called from within the Python shell or another script. 

2. **Example**:
   ```python
   from final_project.emotion_detection import emotion_detector

   result = emotion_detector("I love this new technology.")
   print(result)
