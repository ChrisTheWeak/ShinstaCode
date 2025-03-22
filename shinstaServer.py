from flask import Flask, redirect, url_for, request, render_template
from shinstaCode import *
import webbrowser
import threading
import logging
import os
import signal
import time
app=Flask(__name__, template_folder="templates")
last_request_time=time.time()
def shutdown_server():
    os.kill(os.getpid(), signal.SIGTERM)
@app.route('/')
def index():
    value=""
    return render_template('index.html', data=value)
@app.route('/shutdown',methods=['POST'])
def shutdown():
    shutdown_server()
    return "Server shutting down"
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")
@app.route('/encode',methods=['POST','GET'])
def encodeCall():
    message=request.form['encodeMessage']
    value=encodeMessage(message)
    return render_template('index.html', data=value)
@app.route('/decode',methods=['POST','GET'])
def decodeCall():
    message=request.form['decodeMessage']
    value=decodeMessage(message)
    return render_template('index.html', data=value)
def check_inactivity():
    global last_request_time
    while True:
        time.sleep(60)
        if time.time()-last_request_time > 600:
            shutdown_server()
            break
threading.Thread(target=check_inactivity, daemon=True).start()
if __name__ == "__main__":
    threading.Timer(1.25, open_browser).start()
    app.run(debug=False, port=5000, use_reloader=False)
    