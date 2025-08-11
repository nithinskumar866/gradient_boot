from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model/gb_model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    if request.method == "POST":
        try:
            features = [float(request.form.get(f"feature{i}")) for i in range(1, 6)]
            result = model.predict([features])
            prediction = f"Predicted Genre: {result[0]}"
        except:
            prediction = "Please enter valid input values."
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
