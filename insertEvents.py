from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Event, Base
from datetime import datetime

engine = create_engine('sqlite:///event-collection.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
events = []
events.append(Event(title="Basketball", start_date=datetime(2020, 5, 17, 12, 0), end_date=datetime(
    2020, 5, 19, 12, 0), thumbnail='https://en.wikipedia.org/wiki/Basketball_(ball)#/media/File:Basketball.png'))
events.append(Event(title="Programming", start_date=datetime(2020, 6, 16, 17, 0), end_date=datetime(
    2020, 6, 19, 17, 0), thumbnail='https://en.wikipedia.org/wiki/NeXT_Computer#/media/File:NEXT_Cube-IMG_7154.jpg'))
events.append(Event(title="Golf", start_date=datetime(2020, 5, 10, 12, 0), end_date=datetime(
    2020, 5, 19, 23, 0), thumbnail='https://en.wikipedia.org/wiki/Golf#/media/File:Golfer_swing.jpg'))
for e in events:
    session.add(e)
    session.commit()
