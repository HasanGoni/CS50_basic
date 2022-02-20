from flask import (Flask, 
                   render_template,
                   request,
                   session)
#from flask_session import Session



app = Flask(__name__)

# config Session
#app.config["SESSION_PERMANT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)

SPORTS = [
    'Basketball',
    'Football',
    'Soccer',
    'Ultimate Frisbee'
    ]

@app.route("/")
def index():
    return render_template('index.html',
                          sports=SPORTS)


@app.route("/register", methods=['POST'])
def register():
    # validate submission
    if not request.form.get("name") or request.form.get("sport") not in SPORTS:
        return render_template('failure.html')
    return render_template('success.html')