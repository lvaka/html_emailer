from flask_script import Manager, Command
from html_emailer import app
import secrets

manager = Manager(app)

@manager.command
def runserver():
   """
      Runs Development Server for 
      testing purposes
   """
   app.run()

@manager.command
def generate_secret():
   """
      Generates a secret token for use 
      as SECRET_KEY
   """
   secret = secrets.token_urlsafe(20)
   print(secret)

if __name__ == '__main__':
   manager.run()
