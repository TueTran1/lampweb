import re
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
#import RPi.GPIO as GPIO
import time
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(17, GPIO.OUT)
# GPIO.setup(18, GPIO.OUT)

app = Flask(__name__)


@app.route('/')
def index():
    # GPIO.output(17, GPIO.LOW)
    # GPIO.output(18, GPIO.LOW)
    return render_template('index.html')


@app.route('/turnON', methods = ['POST', 'GET'])
def turnON():
    checkyel = request.form.get('checkyel')
    checkblue = request.form.get('checkblue')
    checknn = request.form.get('nn')

    def handler(checkblue,checkyel):
        if checkblue == 'on' or checkyel == 'on':
            checknn = None

    print(checkyel, checkblue, checknn)
    if checkyel == 'on' and checkblue is None and checknn is None:
        # GPIO.output(17, GPIO.HIGH)
        # GPIO.output(18, GPIO.LOW)
        return render_template('turnOnYel.html')
    if checkblue == 'on' and checkyel is None and checknn is None:
        # GPIO.output(17, GPIO.LOW)
        # GPIO.output(18, GPIO.HIGH)
        return render_template('turnOnBlue.html')
    if checkblue == 'on' and checkyel == 'on' and checknn is None:
        # GPIO.output(17, GPIO.HIGH)
        # GPIO.output(18, GPIO.HIGH)
        return render_template('turnOnBoth.html')
    if checknn == 'on' and checkblue is None and checkyel is None :
        # while checknn == 'on':
        #     GPIO.output(17, True)
        #     GPIO.output(18, True)
        #     time.sleep(0.5)
        #     GPIO.output(17,False)
        #     GPIO.output(18,False)
        #     time.sleep(0.5)
        #     handler(checkblue,checkyel)
        return render_template('flash.html')
    else:
        # GPIO.output(17, GPIO.LOW)
        # GPIO.output(18, GPIO.LOW)
        return render_template('index.html')
    
app.run(debug=True)