from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# configure your database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri'