# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:29:28 2024

@author: Utilisateur
"""

from flask import Flask, jsonify, request
from routes import init_app

app = Flask(__name__)

# Initialisation des routes
init_app(app)

if __name__ == '__main__':
    app.run(port=5000)