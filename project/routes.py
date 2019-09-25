from flask import Flask, redirect, render_template, request, url_for
from server import app, user_input

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", testing="random string")

@app.route("/search", methods=["GET", "POST"])
def search():
    return render_template("search.html", testing="Motor Crash Search")
