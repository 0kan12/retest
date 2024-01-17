from flask import Flask,request,redirect
import requests
app=Flask(__name__)


@app.before_request
def before_request():
    blobid=request.path
    print(blobid)
    url=f"https://jsonblob.com/api/{blobid}"
    response=requests.get(url).json()['content']
    return f"<img src='data:image/png;base64,{response}'>"
app.run()