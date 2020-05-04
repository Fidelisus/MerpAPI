from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Event
from flask import jsonify

app = Flask(__name__)

engine = create_engine('sqlite:///event-collection.db')
Base.metadata.bind = engine



if __name__ == '__main__':
   app.debug = True
   app.run(host='0.0.0.0', port=5000)