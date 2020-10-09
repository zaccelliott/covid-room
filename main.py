# Importing Flask Render Template and JSON
from flask import Flask, render_template, request
import json

# Initiating Flask App
app = Flask(__name__)

# Reading Each JSON File and Turning into Dictionary for Each Building
with open('data/acacia_data.json') as acacia_rooms:
    acacia_dict = json.load(acacia_rooms)
with open('data/admin_data.json') as admin_rooms:
    admin_dict = json.load(admin_rooms)
with open('data/banksia_data.json') as banksia_rooms:
    banksia_dict = json.load(banksia_rooms)
with open('data/bluegum_data.json') as bluegum_rooms:
    bluegum_dict = json.load(bluegum_rooms)
with open('data/boronia_data.json') as boronia_rooms:
    boronia_dict = json.load(boronia_rooms)
with open('data/caledonia_data.json') as caledonia_rooms:
    caledonia_dict = json.load(caledonia_rooms)
with open('data/chapel_data.json') as chapel_rooms:
    chapel_dict = json.load(chapel_rooms)
with open('data/danthonia_data.json') as danthonia_rooms:
    danthonia_dict = json.load(danthonia_rooms)
with open('data/gravelia_data.json') as gravelia_rooms:
    gravelia_dict = json.load(gravelia_rooms)
with open('data/lomandra_data.json') as lomandra_rooms:
    lomandra_dict = json.load(lomandra_rooms)
with open('data/mallee_data.json') as mallee_rooms:
    mallee_dict = json.load(mallee_rooms)
with open('data/redgum_data.json') as redgum_rooms:
    redgum_dict = json.load(redgum_rooms)
with open('data/sandlewood_data.json') as sandlewood_rooms:
    sandlewood_dict = json.load(sandlewood_rooms)
with open('data/wattle_data.json') as wattle_rooms:
    wattle_dict = json.load(wattle_rooms)


# Application Routes for Each Page/Building
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/acacia', methods=['GET', 'POST'])
def acacia():
    return render_template('acacia.html', acacia_dict=acacia_dict)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html', admin_dict=admin_dict)


@app.route('/banksia', methods=['GET', 'POST'])
def banksia():
    return render_template('banksia.html', banksia_dict=banksia_dict)


@app.route('/bluegum', methods=['GET', 'POST'])
def bluegum():
    return render_template('bluegum.html', bluegum_dict=bluegum_dict)


@app.route('/boronia', methods=['GET', 'POST'])
def boronia():
    return render_template('boronia.html', boronia_dict=boronia_dict)


@app.route('/caledonia', methods=['GET', 'POST'])
def caledonia():
    return render_template('caledonia.html', caledonia_dict=caledonia_dict)


@app.route('/chapel', methods=['GET', 'POST'])
def chapel():
    return render_template('chapel.html', chapel_dict=chapel_dict)


@app.route('/danthonia', methods=['GET', 'POST'])
def danthonia():
    return render_template('danthonia.html', danthonia_dict=danthonia_dict)


@app.route('/gravelia', methods=['GET', 'POST'])
def gravelia():
    return render_template('gravelia.html', gravelia_dict=gravelia_dict)


@app.route('/lomandra', methods=['GET', 'POST'])
def lomandra():
    return render_template('lomandra.html', lomandra_dict=lomandra_dict)


@app.route('/malleelow', methods=['GET', 'POST'])
def malleelow():
    return render_template('malleelow.html', mallee_dict=mallee_dict)


@app.route('/malleeup', methods=['GET', 'POST'])
def malleeup():
    return render_template('malleeup.html', mallee_dict=mallee_dict)


@app.route('/redgum', methods=['GET', 'POST'])
def redgum():
    return render_template('redgum.html', redgum_dict=redgum_dict)


@app.route('/sandlewood', methods=['GET', 'POST'])
def sandlewood():
    return render_template('sandlewood.html', sandlewood_dict=sandlewood_dict)


@app.route('/wattle', methods=['GET', 'POST'])
def wattle():
    return render_template('wattle.html', wattle_dict=wattle_dict)
