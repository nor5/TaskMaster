from flask import jsonify

def get_home():
    return jsonify({"message": "Welcome to the home page!"})