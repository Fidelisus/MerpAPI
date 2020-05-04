from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Event, Participate
from flask import jsonify
import random

app = Flask(__name__)

engine = create_engine('sqlite:///event-collection.db')
Base.metadata.bind = engine


# TODO Make correct CORS
# TODO Add better error checking to all the methods (to hide how db is implemented)

def getEvents():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    events = session.query(Event).all()
    response = jsonify(events=[e.serialize for e in events])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


def getEvent(code):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    registration = session.query(Participate).filter_by(code=code).one()

    if not registration:
        return "<h1>404</h1><p>The reservation could not be found.</p>", 404

    event = session.query(Event).filter_by(
        event_id=registration.event_id).one()
    response = jsonify(Event=event.serialize)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def deleteEvent(code):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    registration = session.query(Participate).filter_by(code=code).one()

    if not registration:
        return "<h1>404</h1><p>The reservation could not be found.</p>", 404

    event = session.query(Event).filter_by(
        event_id=registration.event_id).one()

    if event.start_date < start_date - timedelta(days=2):

    response = jsonify(Event=event.serialize)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response    


# TODO make constraint that one user can't registry 2 times for the same event
def participate(event_id, user_name, user_surname):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    if not session.query(Event).filter_by(event_id=event_id).one():
        return "<h1>404</h1><p>The event could not be found.</p>", 404

    code = random.randint(0, 10**8)*10 + int(event_id)
    add_participation = Participate(
        event_id=event_id, user_name=user_name, user_surname=user_surname, code=code)
    session.add(add_participation)
    session.commit()
    response = jsonify({'reservation_number': code})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/api/events", methods=['GET'])
def showEvents():
    if request.method == 'GET':
        return getEvents()


@app.route("/api/participate/<int:code>", methods=['GET'])
def unregistrateFromEvent(code):
    if request.method == 'GET':
        return getEvent(code)


@app.route("/api/participate", methods=['POST'])
def registrateToEvent():
    if request.method == 'POST':
        event_id = request.get_json()['event_id']
        user_name = request.get_json()['user_name']
        user_surname = request.get_json()['user_surname']
        return participate(event_id, user_name, user_surname)


@app.errorhandler(404)
def pageNotFound(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
