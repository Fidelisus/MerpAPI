from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Event
from flask import jsonify

app = Flask(__name__)

engine = create_engine('sqlite:///event-collection.db')
Base.metadata.bind = engine

def get_session():
    DBSession = sessionmaker(bind=engine)
    return DBSession()

def getEvents():
    session = get_session()
    events = session.query(Event).all()
    response =  jsonify(events= [e.serialize for e in events])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/api/events", methods = ['GET'])
def show_events():
    if request.method == 'GET':
        return getEvents()

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == '__main__':
   app.debug = True
   app.run(host='0.0.0.0', port=5000)