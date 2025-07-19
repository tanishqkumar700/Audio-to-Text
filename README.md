# Audio-to-Text

Convert audio files into text using Python!

## Overview

**Audio-to-Text** is a simple Python project for converting audio files (such as WAV, MP3, etc.) into written text using popular speech recognition libraries. It’s ideal for transcription tasks, voice note conversion, or basic speech-to-text automation.

## Features

- Converts audio files to text
- Supports common audio formats (WAV, MP3, etc.)
- Uses Python and open-source speech recognition libraries
- Easy to run and extend

## Requirements

- Python 3.7+
- [speech_recognition](https://pypi.org/project/SpeechRecognition/)
- [pydub](https://pypi.org/project/pydub/) *(for MP3 support)*
- [ffmpeg](https://ffmpeg.org/) *(if handling non-WAV formats)*

Install dependencies:
```bash
pip install SpeechRecognition pydub
```
For MP3 support, ensure `ffmpeg` is installed and available in your system path.

## Usage

1. Place your audio file in the project directory.
2. Run the main script (e.g., `main.py`):

```bash
python main.py input_audio.wav
```

3. The transcribed text will be output to the console or saved to a file, depending on implementation.

## Example

```python
import speech_recognition as sr

recognizer = sr.Recognizer()
audio_file = 'input_audio.wav'

with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data)
    print(text)
```

## Customization

- Change the recognizer to use other APIs (Google, Sphinx, etc.)
- Extend for batch processing or longer audio files
- Save output to a text file

## Contributing

Pull requests and suggestions are welcome! Feel free to open an issue for bugs or feature requests.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [SpeechRecognition](https://github.com/Uberi/speech_recognition)
- [PyDub](https://github.com/jiaaro/pydub)
- [FFmpeg](https://ffmpeg.org/)

---

*Happy transcribing!*
