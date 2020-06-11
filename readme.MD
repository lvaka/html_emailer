# HTML Email App 
 
This is a simple Flask App to send HTML Emails written in Python3.  Set up a virtual environment with a Python3 interpreter.  Install dependencies with pip install -r requirements.txt.  Copy config.py.example into a new config.py file.  
 
Use python manage.py generate_secret to generate a new secret.  Set SECRET_KEY in config.py to this newly generated key, or any other key you want.  It's used as salt to generate the csrf token.  
 
To run the app locally, run python manage.py runserver and view on 127.0.0.1:5000