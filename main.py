import os
import json 
import requests

from flask_lambda import FlaskLambda

from flask import request

app = FlaskLambda(__name__)

# Set file upload requirements here: max file size, extension types(json and txt)

app.config["ALLOWED_FILE_EXTENSIONS"] = ["json"]
app.config['MAX_CONTENT_LENGTH'] = 64 * 1024 * 1024

@app.errorhandler(413)
def too_large(e):
    return (
            json.dumps('File is too large'),
            413,
            {'Content-Type': 'application/json'}
        )

def allowed_file(filename):
    print (filename, 'Uploaded Successfully')
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.lower() in app.config["ALLOWED_FILE_EXTENSIONS"]:
        return True
    else:
        return False
<<<<<<< HEAD
        
def process_upload(uploaded_file):
=======
      

def process_upload(uploaded_file, project):
>>>>>>> 4543a73... Added serverless deployment
    lines = uploaded_file.readlines()
    for line in lines:
        report = json.loads(line)
<<<<<<< HEAD
        text = '*Secrets Found*\n\n'
=======
        text = '*Secrets Found*\n\n*Project:* ' + project + '\n'
>>>>>>> 4543a73... Added serverless deployment
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
<<<<<<< HEAD
        url = "Webhook Url"
        # Call webhook with payload
        requests.post(url, json=payload)


@app.route('/', methods=['POST'])
=======
        url = os.environ['WEBHOOK_URL']
        # Call webhook with payload
        requests.post(url, json=payload)

@app.route('/')
def healthcheck():
    return (
        json.dumps('TruffleHog Notifier'),
        200,
        {'Content-Type': 'application/json'}
    )

@app.route('/upload', methods=['POST'])      
>>>>>>> 4543a73... Added serverless deployment
def upload_file():
    if request.method == "POST":
        
        # check if the post request has the file part
<<<<<<< HEAD
        
=======
        default_project = 'Not Specified'
        project = request.form.get('project', default_project)
>>>>>>> 4543a73... Added serverless deployment
        filekey = 'file'

        if filekey not in request.files:          
            return (
                json.dumps('Unrecognized file key'),
                400,
                {'Content-Type': 'application/json'}
            )

        uploaded_file = request.files[filekey]

        if uploaded_file.filename != '':  
            if uploaded_file and allowed_file(uploaded_file.filename):

<<<<<<< HEAD
            process_upload(uploaded_file)
            return {
            'statusCode': 200,
            'body': json.dumps("File uploaded successfully")
            }
=======
                process_upload(uploaded_file, project)
                return (
                    json.dumps('File Uploaded successfully'),
                    200,
                    {'Content-Type': 'application/json'}
                )
>>>>>>> 4543a73... Added serverless deployment

            else :
                return (
                    json.dumps('That file extension is not allowed. JSON only'),
                    403,
                    {'Content-Type': 'application/json'}
                )
        else:   
            return (
                json.dumps('No file uploaded'),
                400,
                {'Content-Type': 'application/json'}
            )
        
        
    else :
        return (
            json.dumps('Method not allowed'),
            405,
            {'Content-Type': 'application/json'}
        )      
    
if __name__ == '__main__':
    app.run()