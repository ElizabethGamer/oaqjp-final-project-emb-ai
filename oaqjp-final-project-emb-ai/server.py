""" b"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

""" """
@app.route("/emotionDetector")
def emotions():
    text = request.args.get('textToAnalyze')
    response = emotion_detector(text)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    resp = "For the given statement, the system response is "

    for emotion in response:
        if emotion != "dominant_emotion":
            added = "\'" + emotion + "\': " + str(response[emotion]) + ", "
            resp += added

    resp += "and the dominant emotion is " + response["dominant_emotion"] + "."

    return resp


""" b """
@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
