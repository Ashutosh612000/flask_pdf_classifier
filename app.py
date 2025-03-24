from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import torch
import os
import pickle
from model import SimpleNN
from process_pdf import extract_text_from_pdf
from process_text import transform_text
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  
app.config['UPLOAD_FOLDER'] = './uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


if not os.path.exists('vectorizer.pkl'):
    raise FileNotFoundError('Vectorizer file not found. Please provide vectorizer.pkl')

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

model = SimpleNN(input_size=71)

if not os.path.exists('model.pth'):
    raise FileNotFoundError('Model file not found. Please provide model.pth')

model.load_state_dict(torch.load('model.pth'))
model.eval()

categories = ['Science', 'Financial', 'Sports']

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if not file.filename.lower().endswith('.pdf'):
        return jsonify({"error": "Invalid file type. Please upload a PDF file."}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    extracted_text = extract_text_from_pdf(file_path)

    if not extracted_text.strip():
        return jsonify({"error": "No text found in the PDF. It may be scanned images only."}), 400

    vector = transform_text(extracted_text, vectorizer)

    with torch.no_grad():
        output = model(vector)
        probabilities = torch.softmax(output, dim=1)
        confidence, predicted = torch.max(probabilities, 1)
        category = categories[predicted.item()]

    return jsonify({
        "classification": category,
        "confidence": round(confidence.item() * 100, 2),
        "message": "File successfully uploaded"
    })

if __name__ == '__main__':
    app.run(debug=True)
