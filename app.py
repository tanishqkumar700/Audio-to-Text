#!/usr/bin/env python3
"""
Simple Audio Transcription Web Application
Upload audio files and get transcriptions using AssemblyAI
"""
from flask import Flask
from config import SECRET_KEY, DEBUG
from routes import setup_routes


def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max file size
    
    # Setup routes
    setup_routes(app)
    
    return app


if __name__ == '__main__':
    app = create_app()
    
    print("=" * 60)
    print("🎙️  Audio Transcription Server Starting...")
    print("=" * 60)
    print("🌐 Server running at: http://localhost:5000")
    print("📊 Debug mode:", DEBUG)
    print("=" * 60)
    print("\nPress CTRL+C to stop the server\n")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=DEBUG
    )