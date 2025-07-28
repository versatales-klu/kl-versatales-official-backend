from flask import Blueprint, jsonify

app = Blueprint("app", __name__)

@app.route("/")
def home():
    return "Versatales Backend"