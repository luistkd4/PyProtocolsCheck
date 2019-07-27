import imaplib
import poplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class protocolsTest:
	__user = str()
	__password = str()
	__server = str()

	def imapTest(self, user, password, server):
		self.user = user
		self.password = password
		self.server = server
		if server == None:
			server = 'imap.umbler.com'
		result = []
		try:
			M = imaplib.IMAP4_SSL(host=server)
			M.login(user, password)
			M.select
			for i in M.list()[1]:
				result.append(str(i))					
			M.close
			M.logout
			return result
		except Exception as error:			
			return "Error to get e-mails, check user and password. If error persist call e-mail team"

	def popTest(self, user, password, server):
		self.user = user
		self.password = password
		self.server = server
		if server == None:
			server = 'pop.umbler.com'
		result = []
		try:
			M = poplib.POP3_SSL(host=server)
			M.user(user)
			M.pass_(password)
			for i in M.list()[1]:
				result.append(str(i))
			M.quit
			return result
		except Exception as error:
			return "Error to get e-mails, check user and password. If error persist call e-mail team"
	
	def smtpTest(self, user, password, recipient, server):
		self.user = user
		self.password = password
		self.recipient = recipient
		self.server = server
		if server == None:
			server = 'smtp.umbler.com'
		try:
			msg = MIMEMultipart()
			message = 'Test message by umbler team'
			msg['From'] = user
			msg['To'] = recipient
			msg['Reply-to'] = 'friends@umbler.com'
			msg['Subject'] = "Test message by your umbler friend"
			msg.attach(MIMEText(message,'plain'))
			server = smtplib.SMTP(server, 587)
			server.starttls
			server.login(user,password)
			server.sendmail(msg['From'],msg['To'],msg.as_string())
			server.quit
			return "Message was sent"
		except Exception as error:
			return "Error to send message, check user and password. If error persist call e-mail team"