from flask import Flask, request, render_template, Markup
from flask_wtf.csrf import CSRFProtect
from html_emailer.forms import EmailForm
import smtplib, ssl
import io
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
CSRFProtect(app)

def list_emails(email_receiver_str):
	"""
		Splits comma seperated emails
	"""
	email_list = email_receiver_str.split(',')
	return list(map(lambda email: email.strip(), email_list))

def send_mail(**kwargs):
	"""
		Generate SSL Mail
	"""
	message = MIMEMultipart("alternative")
	message["Subject"] = kwargs.get('subject')
	message["From"] = kwargs.get('email')
	message["To"] = (', ').join(kwargs.get('send_to'))

	part1 = kwargs.get('plain_template')
	part2 = kwargs.get('html_template')
	message.attach(part1)
	message.attach(part2)

	context = ssl.create_default_context()
	server = smtplib.SMTP_SSL(kwargs.get('email_host'), 
				kwargs.get('email_host_port'), 
				context=context)
	server.login(kwargs.get('email'), kwargs.get('password'))
	server.sendmail(
		kwargs.get('email'), 
		kwargs.get('send_to'), 
		message.as_string()
	)

@app.route('/', methods=['GET', 'POST'])
def index():
	"""
		Index of HTML Emailer.

		Basic One Page Form to Email
	"""
	messages = None
	errors = None
	form = EmailForm()

	if request.method == 'POST' and form.validate():

		subject = form.subject.data
		email = form.email.data
		password = form.password.data
		email_host = form.email_host.data
		email_host_port = form.email_host_port.data
		receiver_emails = list_emails(form.receiver_emails.data)
		raw_html_file = form.html_template.data.stream
		html_template = MIMEText(raw_html_file.read().decode('ascii'),'html')
		raw_html_file.close()
		raw_plain_file = form.plain_template.data.stream
		plain_template = MIMEText(raw_plain_file.read().decode('ascii'), 'plain')
		raw_plain_file.close()

		try:
			send_mail(subject=subject,
				email=email,
				send_to=receiver_emails,
				plain_template=plain_template,
				html_template=html_template,
				email_host=email_host,
				email_host_port=email_host_port,
				password=password)

			messages = ['Email Sent']

		except:
			errors = ['Server Issue.  Please try again later']

		
	return render_template('index.html', errors=errors, messages=messages)
