import os
import numpy as np
import pandas as pd
import joblib
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Initialize the Flask app
app = Flask(__name__)

# Set up directories and allowed file extensions
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"csv"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Load the pre-trained model, scaler, and label encoders
class NetworkTrafficClassifier:
    def __init__(self):
        self.model = None
        self.scaler = None
        self.label_encoders = {}
        self.numeric_columns = None
        self.categorical_columns = ["proto", "service", "state"]

    def load_model(self):
        self.model = joblib.load("models/network_traffic_classifier.pkl")
        self.scaler = joblib.load("models/scaler.pkl")
        self.label_encoders = joblib.load("models/label_encoders.pkl")
        print("Model, Scaler, and Label Encoders loaded.")

    def preprocess_data(self, df, is_training=False):
        df = df.copy()
        columns_to_drop = ["id", "attack_cat", "is_sm_ips_ports"]
        df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

        if "label" in df.columns:
            df["label"] = pd.to_numeric(df["label"])

        # Handle categorical columns
        for col in self.categorical_columns:
            if col in df.columns:
                if is_training:
                    self.label_encoders[col] = LabelEncoder()
                    df[col] = self.label_encoders[col].fit_transform(
                        df[col].astype(str)
                    )
                else:
                    if col in self.label_encoders:
                        df[col] = df[col].astype(str)
                        known_categories = set(self.label_encoders[col].classes_)
                        df[col] = df[col].map(
                            lambda x: (
                                x
                                if x in known_categories
                                else self.label_encoders[col].classes_[0]
                            )
                        )
                        df[col] = self.label_encoders[col].transform(df[col])

        # Dynamically identify numeric columns if not already available
        if self.numeric_columns is None:
            self.numeric_columns = [
                col
                for col in df.columns
                if col not in self.categorical_columns
                and col != "label"
                and pd.api.types.is_numeric_dtype(df[col])
            ]

        for col in self.numeric_columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
        df = df.replace([np.inf, -np.inf], np.nan)
        df = df.fillna(0)

        X = df.drop("label", axis=1)

        # Scale the numeric columns
        if self.numeric_columns:
            numeric_features = X[self.numeric_columns]
            scaled_features = self.scaler.transform(numeric_features)
            X[self.numeric_columns] = scaled_features

        return X

    def predict(self, X):
        return self.model.predict(X)


# Instantiate the classifier and load the model
classifier = NetworkTrafficClassifier()
classifier.load_model()


# Check allowed file extension
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# Home route
@app.route("/")
def index():
    return render_template("index.html")


# Route for file upload and prediction
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"})
    if file and allowed_file(file.filename):
        # Secure the filename and save the file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        # Load CSV file and preprocess data
        df = pd.read_csv(filepath)
        X_processed = classifier.preprocess_data(df, is_training=False)

        # Predict using the trained model
        y_pred = classifier.predict(X_processed)

        # Generate results for display
        result = []
        for true_label, pred_label in zip(df["label"], y_pred):
            result.append(
                {
                    "True label": "Malicious" if true_label == 1 else "Normal",
                    "Predicted label": "Malicious" if pred_label == 1 else "Normal",
                }
            )

        # Return the results
        return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
