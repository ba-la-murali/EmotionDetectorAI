from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    """
    Analyze the user-provided text for emotions and return the result.

    Returns:
        str: JSON response with emotion detection results or an error message.
    """
    text_to_detect = request.args.get('textToAnalyze', '').strip()

    if not text_to_detect:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    response = emotion_detector(text_to_detect)

    # Check if there was an error or invalid response
    if 'error' in response or response['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    return jsonify({
        'anger': response['anger'],
        'disgust': response['disgust'],
        'fear': response['fear'],
        'joy': response['joy'],
        'sadness': response['sadness'],
        'dominant_emotion': response['dominant_emotion']
    })

@app.route("/")
def render_index_page():
    """
    Render the main application page.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')

def run_emotion_detection():
    """
    Main function to run the Emotion Detection application.

    Runs the Flask application on the specified host and port.
    """
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    run_emotion_detection()
