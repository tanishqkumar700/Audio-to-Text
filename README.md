# Audio-to-Text

A Python-based audio transcription tool that converts audio files to text using the AssemblyAI API.

## Features

- **Audio File Upload**: Upload audio files to AssemblyAI for processing
- **Speech-to-Text Conversion**: Convert speech in audio files to accurate text transcripts
- **Automatic Polling**: Monitor transcription progress and automatically retrieve results
- **Text File Output**: Save transcripts as text files with the same name as the audio file
- **Command Line Interface**: Simple CLI for easy integration into workflows

## Requirements

- Python 3.6 or higher
- `requests` library for HTTP API calls
- AssemblyAI API key

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tanishqkumar700/Audio-to-Text.git
   cd Audio-to-Text
   ```

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or manually install:
   ```bash
   pip install requests
   ```

3. **Set up your AssemblyAI API key**:
   - Sign up for a free account at [AssemblyAI](https://www.assemblyai.com/)
   - Get your API key from the dashboard
   - **Important**: For security, you should use environment variables instead of hardcoding the API key
   - Either:
     - Update `api_secrets.py` with your API key (not recommended for production)
     - Or better: Use environment variables by modifying the code to use `os.environ.get('ASSEMBLYAI_API_KEY')`

## Usage

### Basic Usage

Run the script with an audio file as an argument:

```bash
python main.py your_audio_file.wav
```

### Example

```bash
python main.py tanishq.wav
```

This will:
1. Upload `tanishq.wav` to AssemblyAI
2. Start the transcription process
3. Poll for completion (checking every 10 seconds)
4. Save the transcript to `tanishq.wav.txt`

### Supported Audio Formats

AssemblyAI supports many audio formats including:
- WAV
- MP3
- MP4
- M4A
- FLAC
- And many others

## File Structure

```
Audio-to-Text/
├── main.py                 # Entry point - handles command line arguments
├── api_communication.py    # Core API functions (upload, transcribe, poll, save)
├── api_secrets.py         # API key configuration
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules (protects API keys)
├── tanishq.wav            # Example audio file
├── tanishq.wav.txt        # Example transcript output
└── README.md              # This file
```

## How It Works

1. **Upload**: The audio file is uploaded to AssemblyAI's servers using their upload endpoint
2. **Transcribe**: A transcription job is started with the uploaded audio URL
3. **Poll**: The script checks every 10 seconds to see if transcription is complete
4. **Save**: Once complete, the transcript text is saved to a `.txt` file

## Security Note

⚠️ **Important**: The current implementation has the API key hardcoded in `api_secrets.py`. For production use, consider:

- Using environment variables
- Adding `api_secrets.py` to `.gitignore`
- Using a configuration file that's not tracked in version control

Example environment variable approach:
```python
import os
API_KEY_ASSEMBLYAI = os.environ.get('ASSEMBLYAI_API_KEY')
```

## Error Handling

The script includes basic error handling:
- Checks for transcription completion vs. error status
- Displays error messages if transcription fails
- Saves successful transcripts and notifies the user

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request

## License

This project is open source. Please check the repository for license details.

## Acknowledgments

- [AssemblyAI](https://www.assemblyai.com/) for providing the speech-to-text API
- Built for educational and practical transcription purposes