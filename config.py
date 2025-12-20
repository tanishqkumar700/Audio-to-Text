"""
Configuration file for audio transcription service
"""

# AssemblyAI API Key
API_KEY_ASSEMBLYAI = '20995fd1930d4133bccaba609f20c351'

# Flask Configuration
SECRET_KEY = 'your-secret-key-change-this-in-production'
DEBUG = True

# Upload Configuration
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'wav', 'mp3', 'mp4', 'flac', 'm4a', 'ogg', 'webm'}

# AssemblyAI Endpoints
ASSEMBLYAI_UPLOAD_ENDPOINT = "https://api.assemblyai.com/v2/upload"
ASSEMBLYAI_TRANSCRIPT_ENDPOINT = "https://api.assemblyai.com/v2/transcript"

# Audio Settings
AUDIO_CHUNK_SIZE = 5242880  # 5MB