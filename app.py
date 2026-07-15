from flask import Flask, render_template, request , redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from database.models import db, User, Complaint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("home.html")

from flask import session
from werkzeug.security import check_password_hash

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            session["user_id"] = user.id
            session["user_name"] = user.fullname

            return redirect("/dashboard")

        return "Invalid Email or Password"

    return render_template("login.html")
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        fullname = request.form["fullname"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            return "Email already registered. Please use another email."

        hashed_password = generate_password_hash(password)

        user = User(
            fullname=fullname,
            email=email,
            phone=phone,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")
@app.route("/report", methods=["GET", "POST"])
def report():

    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":

        description = request.form["description"]

        complaint = Complaint(
            user_id=session["user_id"],
            description=description,
            crime_type="Pending AI Analysis",
            status="Pending"
        )

        db.session.add(complaint)
        db.session.commit()

        return redirect("/dashboard")

    return render_template("report.html")
@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/dashboard")
@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect("/login")

    return render_template(
        "dashboard.html",
        username=session["user_name"]
    )
@app.route("/awareness")
def awareness():
    return render_template("awareness.html")

@app.route("/emergency")
def emergency():
    return render_template("emergency.html")

if __name__ == "__main__":
    app.run(debug=True)