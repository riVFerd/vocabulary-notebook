from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import requests


app = Flask(__name__)

client = MongoClient('Mongo DB connection string')
db = client.dbsparta_plus_week2


@app.route('/')
def main():
    # This route should fetch all of 
    # the words from the database and 
    # pass them on to the HTML template
    return render_template("index.html")


@app.route('/detail/<keyword>')
def detail(keyword):
    # This handler should find the 
    # requested word through the dictionary 
    # API and pass the data for that word onto 
    # the template
    return render_template("detail.html", word=keyword)


@app.route('/api/save_word', methods=['POST'])
def save_word():
    #  This handler should save the word in the database
    return jsonify({'result': 'success', 'msg': 'word saved'})


@app.route('/api/delete_word', methods=['POST'])
def delete_word():
    #  This handler should delete the word from the database
    return jsonify({'result': 'success', 'msg': 'word deleted'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)