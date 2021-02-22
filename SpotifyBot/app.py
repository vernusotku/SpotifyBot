import os
import json
from flask import Flask, session, request, redirect, jsonify
from flask_session import Session
from extensions import db, initDb
from SpotifyBot import *

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(64)

    register_extensions(app)
    register_blueprint(app)

    Session(app)
    return app

def register_blueprint(app):
    app.register_blueprint(api_blueprint, url_prefix='/api')

def register_extensions(app):
    db.create_connection(DATABASE_CONNECT["SERVER"], DATABASE_CONNECT["USER"], DATABASE_CONNECT["PASSWORD"], DATABASE_CONNECT["DATABASE"])
    initDb(db)
