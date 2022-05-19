from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/turnON', methods = ['POST', 'GET'])
def turnON():
    checkyel = request.form.get('checkyel')
    checkblue = request.form.get('checkblue')
    print(checkyel, checkblue)
    if checkyel == 'on' and checkblue is None:
        return render_template('turnOnYel.html')
    if checkblue == 'on' and checkyel is None:
        return render_template('turnOnBlue.html')
    if checkblue == 'on' and checkyel == 'on':
        return render_template('turnOnBoth.html')
    else:
        return render_template('index.html')
    
app.run(debug=True)