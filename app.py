from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Event, Participate
from flask import jsonify
import random

app = Flask(__name__)

engine = create_engine('sqlite:///event-collection.db')
Base.metadata.bind = engine


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
    return jsonify(Event=event.serialize)

# TODO check errors and make constraint that one user can't registry 2 times for the same event
def participate(event_id, user_name, user_surname):
    code = random.randint(0, 10**8)*10 + int(event_id)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    if not session.query(Event).filter_by(event_id=event_id).one():
        return "<h1>404</h1><p>The event could not be found.</p>", 404

    add_participation = Participate(
        event_id=event_id, user_name=user_name, user_surname=user_surname, code=code)
    session.add(add_participation)
    session.commit()
    return jsonify({'reservation_number': code})


@app.route("/api/events", methods=['GET'])
def show_events():
    if request.method == 'GET':
        return getEvents()


@app.route("/api/participate/<int:code>", methods=['GET'])
def unregistrate_from_event(code):
    if request.method == 'GET':
        return getEvent(code)


@app.route("/api/participate", methods=['POST'])
def registrate_to_event():
    if request.method == 'POST':
        event_id = request.get_json()['event_id']
        user_name = request.get_json()['user_name']
        user_surname = request.get_json()['user_surname']
        return participate(event_id, user_name, user_surname)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
