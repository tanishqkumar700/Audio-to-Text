"""
Flask routes for file-based audio transcription
"""
import os
from flask import render_template, request, jsonify
from werkzeug.utils import secure_filename
from file_transcription import FileTranscriptionService
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS


# Initialize services
file_service = None


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def setup_routes(app):
    """Setup all Flask routes"""
    global file_service
    
    # Initialize services
    file_service = FileTranscriptionService()
    
    # Ensure upload folder exists
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    
    @app.route('/')
    def index():
        """Render main page"""
        return render_template('index.html')
    
    @app.route('/upload', methods=['POST'])
    def upload_file():
        """Handle file upload for audio transcription"""
        try:
            print("Upload request received")
            
            # Check if file is present
            if 'file' not in request.files:
                return jsonify({'error': 'No file uploaded'}), 400
            
            file = request.files['file']
            print(f"File received: {file.filename}")
            
            # Check if file is selected
            if file.filename == '':
                return jsonify({'error': 'No file selected'}), 400
            
            # Check if file type is allowed
            if not allowed_file(file.filename):
                return jsonify({'error': f'File type not supported. Allowed types: {", ".join(ALLOWED_EXTENSIONS)}'}), 400
            
            # Save the file
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            
            print(f"File saved: {file_path}")
            
            # Transcribe the file
            success, result = file_service.transcribe_file(file_path)
            
            if success:
                print("Transcription successful")
                return jsonify({
                    'transcription': result['text'],
                    'filename': filename,
                    'id': result['id']
                })
            else:
                print(f"Transcription failed: {result}")
                return jsonify({'error': f'Transcription failed: {result}'}), 500
                
        except Exception as e:
            print(f"Upload error: {e}")
            return jsonify({'error': str(e)}), 500