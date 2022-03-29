## Api

Backend is created using Python with Flask and sqlalchemy. To run it you have to install Flask and sqlalchemy.
You should use:
python ./app.py

### Backend

In backend there are 3 endpoints:
- /api/events to get all events
- /api/events/{code} to get event which is connected to specified reservation code
- /api/participate you can sign up for event

I have tested it with postman.
