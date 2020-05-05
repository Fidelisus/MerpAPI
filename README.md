## Api

Backend is created using Python with Flask and sqlalchemy. To run it you have to install Flask and sqlalchemy.
You should use:
python ./app.py

I have marked some TODO- these are things I didn't have time to finish.

### Backend

In backend there are 3 endpoints:
- /api/events to get all events
- /api/events/{code} to get event which is connected to specified reservation code
- /api/participate you can sign up for event

I have tested it with postman.

### Frontend

Unfortunately, I didn't have time to finish CORS policy. I run it using XAMPP. Unfortunatelly, requests don't work.

# EDIT (After deadline)
### By mistake I have deleted one line before last commit- that is why there is a problem with compilation. You can just delete the whole deleteEvent method (at line 40) and it will compile. Also, to populate the db you can run insertEvents.py.
