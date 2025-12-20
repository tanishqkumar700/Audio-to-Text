"""
File-based transcription service for uploaded audio files
"""
import requests
import time
import os
from config import (
    API_KEY_ASSEMBLYAI,
    ASSEMBLYAI_UPLOAD_ENDPOINT,
    ASSEMBLYAI_TRANSCRIPT_ENDPOINT,
    AUDIO_CHUNK_SIZE
)


class FileTranscriptionService:
    """Handles file upload and transcription"""
    
    def __init__(self):
        self.headers = {'Authorization': API_KEY_ASSEMBLYAI}
    
    def upload_file(self, filename):
        """
        Upload audio file to AssemblyAI
        Returns: audio_url (str)
        """
        def read_file(filename, chunk_size=AUDIO_CHUNK_SIZE):
            """Generator to read file in chunks"""
            with open(filename, 'rb') as _file:
                while True:
                    data = _file.read(chunk_size)
                    if not data:
                        break
                    yield data
        
        try:
            upload_response = requests.post(
                ASSEMBLYAI_UPLOAD_ENDPOINT,
                headers=self.headers,
                data=read_file(filename)
            )
            
            upload_response.raise_for_status()
            audio_url = upload_response.json()['upload_url']
            print(f"File uploaded successfully: {audio_url}")
            return audio_url
            
        except requests.exceptions.RequestException as e:
            print(f"Upload error: {e}")
            raise Exception(f"Failed to upload file: {str(e)}")
    
    def request_transcription(self, audio_url):
        """
        Request transcription from AssemblyAI
        Returns: job_id (str)
        """
        try:
            transcript_request = {"audio_url": audio_url}
            transcript_response = requests.post(
                ASSEMBLYAI_TRANSCRIPT_ENDPOINT,
                json=transcript_request,
                headers=self.headers
            )
            
            transcript_response.raise_for_status()
            job_id = transcript_response.json()['id']
            print(f"Transcription job created: {job_id}")
            return job_id
            
        except requests.exceptions.RequestException as e:
            print(f"Transcription request error: {e}")
            raise Exception(f"Failed to request transcription: {str(e)}")
    
    def poll_transcription(self, transcript_id):
        """
        Poll transcription status
        Returns: dict with transcription data
        """
        try:
            polling_endpoint = f"{ASSEMBLYAI_TRANSCRIPT_ENDPOINT}/{transcript_id}"
            polling_response = requests.get(polling_endpoint, headers=self.headers)
            polling_response.raise_for_status()
            return polling_response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Polling error: {e}")
            raise Exception(f"Failed to poll transcription: {str(e)}")
    
    def get_transcription_result(self, audio_url, callback=None):
        """
        Get final transcription result by polling
        Returns: (data, error)
        callback: optional function to call with progress updates
        """
        try:
            transcript_id = self.request_transcription(audio_url)
            
            while True:
                data = self.poll_transcription(transcript_id)
                status = data['status']
                
                if callback:
                    callback(status)
                
                if status == 'completed':
                    print("Transcription completed successfully")
                    return data, None
                    
                elif status == 'error':
                    error_msg = data.get('error', 'Unknown error')
                    print(f"Transcription error: {error_msg}")
                    return data, error_msg
                
                print(f"Status: {status} - waiting 10 seconds...")
                time.sleep(10)
                
        except Exception as e:
            print(f"Get transcription result error: {e}")
            return None, str(e)
    
    def save_transcript(self, audio_url, output_filename, callback=None):
        """
        Complete transcription workflow: upload, transcribe, and save
        Returns: (success: bool, output_path: str or error_msg: str)
        """
        try:
            data, error = self.get_transcription_result(audio_url, callback)
            
            if data and data.get('text'):
                # Ensure output filename has .txt extension
                if not output_filename.endswith('.txt'):
                    output_filename += '.txt'
                
                # Save transcription to file
                with open(output_filename, 'w', encoding='utf-8') as f:
                    f.write(data['text'])
                
                print(f"Transcription saved to: {output_filename}")
                return True, output_filename
                
            elif error:
                print(f"Transcription failed: {error}")
                return False, error
            else:
                return False, "No transcription text received"
                
        except Exception as e:
            print(f"Save transcript error: {e}")
            return False, str(e)
    
    def transcribe_file(self, filepath):
        """
        Complete transcription workflow for a file
        Returns: (success: bool, result: dict or error_msg: str)
        """
        try:
            # Upload file
            audio_url = self.upload_file(filepath)
            
            # Get transcription
            data, error = self.get_transcription_result(audio_url)
            
            if data and not error:
                return True, {
                    'text': data.get('text', ''),
                    'id': data.get('id', ''),
                    'status': data.get('status', '')
                }
            else:
                return False, error or "Unknown error occurred"
                
        except Exception as e:
            return False, str(e)