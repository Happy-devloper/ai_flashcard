# Flashcard AI

A simple command-line app that generates five flashcards about a topic using the Hugging Face Inference API.

## Requirements

- Python 3.8 or later
- A Hugging Face access token with permission to use the selected model

## Setup

1. Clone this repository and open the project folder.
2. (Optional) Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install the required packages:

   ```powershell
   pip install python-dotenv huggingface_hub
   ```

4. Create a file named `.env` in the project folder and add your token:

   ```text
   HF_TOKEN=your_hugging_face_token
   ```

   Keep your token private. The `.env` file is excluded from Git.

## Run

```powershell
python app.py
```

Enter a topic when prompted. The app generates five question-and-answer flashcards. Press Enter after each question to reveal its answer.
