from flask import Blueprint, jsonify
from app.models import ClubRoleRegistration

app = Blueprint("app", __name__)

@app.route("/")
def home():
    # from models import 
    return "Versatales Backend"

@app.route("/server-status")
def server_status():
    return jsonify( { "status": True } )
