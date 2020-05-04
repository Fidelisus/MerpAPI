import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

dbRoute = 'sqlite:///event-collection.db'

class Event(Base):
    __tablename__ = 'event'

    event_id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    start_date = Column(TIMESTAMP)
    end_date = Column(TIMESTAMP)
    thumbnail = Column(String(250))

    @property
    def serialize(self):
        return {
        'event_id': self.event_id,
        'title': self.title,
        'start_date': self.start_date,
        'end_date': self.end_date,
        'thumbnail': self.thumbnail,
        }

class Participate(Base):
    __tablename__ = 'participate'

    code = Column(Integer, primary_key=True)
    event_id = Column(Integer, primary_key=True)
    user_name = Column(String(20), nullable=False)
    user_surname = Column(String(20), nullable=False)

    @property
    def serialize(self):
        return {
        'code': self.code,
        'event_id': self.event_id,
        'user_name': self.user_name,
        'user_surname': self.user_surname,
        }

engine = create_engine(dbRoute)
Base.metadata.create_all(engine)