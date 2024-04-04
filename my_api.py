# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 12:34:54 2024

@author: danie
"""
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"


if __name__ == "__main__":
    app.run(debug=True)