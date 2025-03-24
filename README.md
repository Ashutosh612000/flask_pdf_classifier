<<<<<<< HEAD
📚 PDF Classification Flask App

A simple Flask application that classifies uploaded PDFs into categories using a trained PyTorch model.


🚀 Features

✅ Upload and classify PDFs into categories: Science, Financial, and Sports.

📄 Supports text-based PDFs (Scanned images in PDFs will return an error).

📂 Efficiently handles large PDFs (e.g., 100 pages).

📦 Model and Vectorizer loading handled in a separate file for cleaner structure.

📄 Returns meaningful error messages for various test cases.



📦 Installation


1. Clone the repository

    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name

2. Install Python 3.10 (If not already installed)

    sudo apt update
    sudo apt install python3.10 python3.10-venv python3.10-dev

3. Create a virtual environment

    python3.10 -m venv env
    source env/bin/activate  

4. Check CUDA Version:

    nvidia-smi

    #The CUDA version will be displayed in the output. Ensure it's compatible with the PyTorch version you will install.
    #Example (for CUDA 12.2):
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

5. Install Remaining Dependencies

    pip install -r requirements.txt



📂 How To Run The Project

1. Start the Application

    python3 app.py

    The application will run at: http://127.0.0.1:5000/

2. Request using curl:

    curl -X POST -F "file=@/path/to/your/test.pdf" http://127.0.0.1:5000/upload


    Response:
        {
        "classification": "Science",
        "confidence": "78.23%",
        "message": "File successfully uploaded"
        }



=======
# flask_pdf_classifier
>>>>>>> 75d270c2221288c2fd48555807c87aeaa9921dad
