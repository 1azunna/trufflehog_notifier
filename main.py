import os
import json 
import requests

from flask import Flask, request

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Set file upload requirements here: max file size, extension types(json and txt)

app.config["ALLOWED_FILE_EXTENSIONS"] = ["json"]
app.config['MAX_CONTENT_LENGTH'] = 64 * 1024 * 1024

@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413

def allowed_file(filename):
    print (filename)
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.lower() in app.config["ALLOWED_FILE_EXTENSIONS"]:
        return True
    else:
        return False
        
def process_upload(uploaded_file):
    lines = uploaded_file.readlines()
    for line in lines:
        print (line)
        report = json.loads(line)
        text = '*Secrets Found*\n\n'
        for k in report:
            if k not in ('stringsFound', 'diff', 'printDiff'):
                text += f"*{k}:* {report[k]}\n"
        payload = {
                    "attachments": [
                        {
                            "color": "#f2c744",
                            "blocks": [
                                {
                                    "type": "section",
                                    "text": {
                                        "type": "mrkdwn",
                                        "text": text
                                    },
                                    "accessory": {
                                        "type": "image",
                                        "image_url": "https://avatars3.githubusercontent.com/u/15876092?s=280&v=4",
                                        "alt_text": "TruffleHog image"
                                    }
                                }
                            ]
                        }
                    ]
                }
        url = "Webhook Url"
        # Call webhook with payload
        requests.post(url, json=payload)


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == "POST":
        
        # check if the post request has the file part
        
        filekey = 'file'
        if filekey not in request.files:
            
            return "Unrecognized file key", 204

        uploaded_file = request.files[filekey]
        if uploaded_file.filename == '':
            
            return {
            'statusCode': 204,
            'body': json.dumps("No file uploaded")
            }

        if uploaded_file and allowed_file(uploaded_file.filename):

            process_upload(uploaded_file)
            return {
            'statusCode': 200,
            'body': json.dumps("File uploaded successfully")
            }

        else :
            return {
            'statusCode': 403,
            'body': json.dumps("That file extension is not allowed")
            }
    else :
        return {
        'statusCode': 405,
        'body': json.dumps("Method not allowed")
        }       
    