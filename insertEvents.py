from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Event, Base
from datetime import datetime

engine = create_engine('sqlite:///event-collection.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
events = []
events.append(Event(title = "Basketball", start_date=datetime(2020, 5, 17, 12, 0), end_date=datetime(2020, 5, 19, 12, 0), thumbnail = 'https://en.wikipedia.org/wiki/Basketball_(ball)#/media/File:Basketball.png'))
for e in events:
    session.add(e)
    session.commit()
