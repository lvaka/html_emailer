from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms.fields import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired

class EmailForm(FlaskForm):
	subject = StringField(u'subject', [InputRequired()])
	email = StringField(u'email', [InputRequired()])
	password = PasswordField(u'password', [InputRequired()])
	email_host = StringField(u'email_host', [InputRequired()])
	email_host_port = StringField(u'email_host_port', [InputRequired()])
	receiver_emails = TextAreaField(u'receiver_emails', [InputRequired()])
	html_template = FileField(validators=[FileRequired()])
	plain_template = FileField(validators=[FileRequired()])
