AI Text Summarizer (Full-Stack Application)

This is a full-stack web application that allows users to summarize long pieces of text using an AI model.

The frontend is a responsive HTML, CSS, and JavaScript page that provides a clean user interface. The backend is a high-performance Python API built with FastAPI that serves a pre-trained Hugging Face transformers model.

Core Technologies Used:

Backend: Python, FastAPI, Uvicorn

AI/NLP: Hugging Face transformers (using the sshleifer/distilbart-cnn-12-6 model)

Frontend: HTML, Tailwind CSS, JavaScript (with asynchronous fetch)

Environment: venv (Virtual Environment)

How to Run This Project Locally

1. Clone the Repository

git clone [https://github.com/YOUR_USERNAME/ai-text-summarizer.git](https://github.com/YOUR_USERNAME/ai-text-summarizer.git)
cd ai-text-summarizer


(Replace "YOUR_USERNAME" with your GitHub username)

2. Set Up the Backend (Python)

# Create a virtual environment
python -m venv venv

# Activate the environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install the required libraries
pip install fastapi "uvicorn[standard]" transformers torch

# Run the FastAPI server
# This will start the backend "kitchen"
uvicorn main:app --reload


You will see Uvicorn running on http://127.0.0.1:8000.

3. Run the Frontend (HTML)

Keep the uvicorn terminal running.

In a separate program (like the "Go Live" extension in VS Code), open the index.html file in your browser.

The webpage will now be able to successfully connect to the running server.
