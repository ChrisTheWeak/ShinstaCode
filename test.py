from flask import Flask, redirect, url_for, request, render_template
from shinstaCode import *
app=Flask(__name__)
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