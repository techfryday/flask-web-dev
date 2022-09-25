from app import app
from flask import render_template
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/admin/home")
def admin_home():
    return render_template("admin/admin_home.html")
