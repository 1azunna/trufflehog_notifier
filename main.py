import sys, os
import json 

from flask import Flask, request

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = file_mb_max * 64 * 64

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensions

@app.route('/', methods=['POST'])
def upload_file():
    if request.is_json: 
        req = request.get_json()
        
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
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
