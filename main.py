import os
import json 

from flask import Flask, flash, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Set file upload requirements here: max file size, extension types(json and txt)

app.config["ALLOWED_FILE_EXTENSIONS"] = ["json", "txt"]
app.config['MAX_CONTENT_LENGTH'] = 64 * 1024 * 1024

@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413

def allowed_file(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config["ALLOWED_FILE_EXTENSIONS"]:
        return True
    else:
        return False

@app.route('/', methods=['POST'])
def upload_file():
    if request.method == "POST":
        
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "No file uploaded"

        uploaded_file = request.files['file']
        if uploaded_file.filename == '':
            flash('No uploaded file')
            return "No file uploaded"

        if uploaded_file and allowed_file(uploaded_file.filename):
            filename = secure_filename(file.filename)
            contents = file.read()
            data = json.load(contents)

     
        
        return {
            'statusCode': 200,
            'body': json.dumps('File uploaded successfully')
        }
    


# def lambda_handler(event, context):
#     # TODO implement
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda!')
#     }

    # response.headers['Content-Security-Policy'] = "default-src 'self'"
    # response.headers['X-Content-Type-Options'] = 'nosniff'
    # response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    # response.headers['X-XSS-Protection'] = '1; mode=block'
    # response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'