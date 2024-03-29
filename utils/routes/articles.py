import sys
sys.path.append('..')
from flask import jsonify
from utils.functions.scrap import getArticles
from utils.functions.app import app, printLog

URL = "https://www.craft.ai/blog"

def articles():
    data = getArticles(URL)
    printLog(data)
    return jsonify(data)

def article(index):
    data = getArticles(URL)
    if index >= len(data):
        return jsonify({'error': 'Index out of range'})
    return jsonify(data[index])