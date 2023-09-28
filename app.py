from flask import *
import time

def generate_timestamp():
    return str(int(time.time() * 1000))

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.root_path, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/assets/style.css')
def stylesheet():
    return send_from_directory(app.root_path, 'assets/style.css', mimetype='text/css')

@app.route('/assets/script.js')
def clientscript():
    return send_from_directory(app.root_path, 'assets/script.js', mimetype='text/javascript')

@app.route("/")
def index():
    return render_template('index.html', timestamp=generate_timestamp())

@app.route("/sync")
def now():
    return Response(generate_timestamp(), mimetype='text/plain')

@app.route("/login")
def login():
    return render_template('login.html', timestamp=generate_timestamp())

@app.route("/custom", methods=["GET", "POST"])
def custom():
    if request.method == "POST":
        return render_template('custom.html', name=escape(request.form['user']))
    else:
        return render_template('custom-logged-out.html')

@app.route("/length-calc", methods=["GET", "POST"])
def lengthCalc():
    if request.method == "POST":
        return render_template('length-calc.html', text='The string "' + escape(request.form['string']) + '" has ' + str(len(request.form['string'])) + ' characters.')
    else:
        return render_template('length-calc.html', text='Enter a string in the box below to calculate the length of the string.')
