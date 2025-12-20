# Audio Transcription Service

A simple, fast, and reliable web application that converts audio files to text using AssemblyAI's speech recognition API.

## Overview

This application lets you upload common audio files, transcribes them using AssemblyAI, and provides a clean web interface to view and download the results.

## Supported Audio Formats

| Format | Extension | Max Size |
|--------|-----------|----------|
| WAV    | `.wav`    | 100MB    |
| MP3    | `.mp3`    | 100MB    |
| FLAC   | `.flac`   | 100MB    |
| MP4    | `.mp4`    | 100MB    |
| M4A    | `.m4a`    | 100MB    |
| OGG    | `.ogg`    | 100MB    |
| WebM   | `.webm`   | 100MB    |

## Setup and Run

Requirements: Python 3.7+, an AssemblyAI API key, and internet access.

Install the two dependencies, set your API key in `config.py`, and start the server:

```bash
pip install flask requests
python3 app.py
```

Open `http://localhost:5000` in your browser.

## Usage

Upload an audio file from the homepage, start transcription, then review or download the resulting text.

## Project Structure

```
11Speech Recognition/
├── app.py                  # Main Flask application
├── config.py              # Configuration settings & API key
├── routes.py              # Web routes and request handlers
├── file_transcription.py  # AssemblyAI integration service
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── .gitignore             # Git ignore rules
├── templates/
│   └── index.html         # Main web interface
├── uploads/               # Temporary audio file storage
│   └── .gitkeep           # Keep directory in version control
└── .vscode/               # VS Code settings
    └── settings.json      # Python interpreter configuration
```

## Dependencies

This project uses minimal dependencies for maximum compatibility:

| Package | Version | Purpose |
|---------|---------|---------|
| Flask   | 3.0.0+  | Web framework for the application |
| Requests| 2.31.0+ | HTTP client for AssemblyAI API calls |

**No virtual environment required** - works with global Python installation!

## Configuration Options

Edit `config.py` to customize your setup:

```python
# API Configuration
ASSEMBLYAI_API_KEY = "your_api_key_here"
ASSEMBLYAI_UPLOAD_URL = "https://api.assemblyai.com/v2/upload"
ASSEMBLYAI_TRANSCRIPT_URL = "https://api.assemblyai.com/v2/transcript"
```

## Customization

- Change the recognizer to use other APIs (Google, Sphinx, etc.)
- Extend for batch processing or longer audio files
- Save output to a text file

## Contributing

Pull requests and suggestions are welcome! Feel free to open an issue for bugs or feature requests.

---

*Happy transcribing!*

Made with Flask and AssemblyAI • © 2025