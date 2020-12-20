# trufflehog_notifier
A simple flask web app to send trufflehog scan results to slack using Amazon API Gateway and Lambda.

## Requirements
- Python3
- Serverless or Zappa
- NPM (Only when using serveless)

## Preparation
```
python3 -m venv venv
source venv/bin/activate
```
### Serveless Deploy
```
npm install 
```
### Zappa Deploy
```
pip install zappa 
pip install -r requirements.txt
```
## Deployment.
### severless
Update serverless.yml with your slack webhook url using the environment variable specified
```
sls deploy
```
### zappa
```
zappa deploy production
```
Check Deployment status

```
zappa status production
```
## Update Deployment
### serverless
```
serverless deploy function -f trufflehog-notifier-dev
```
### zappa
```
zappa update production
```
## Teardown
### serverless
```
sls remove
```
### zappa
```
zappa undeploy production
```

**zappa deployment configurations are set in zappa_settings.json**


## Update function after making code changes (Alternative)
```
zappa package production
```
Upload zip file to s3 bucket and update function

