import sendgrid
import os
from sendgrid.helpers.mail import *
#sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
sg = sendgrid.SendGridAPIClient(api_key=os.environ.get())
from_mail = Email("deepavenkatesan002@gmail.com")
to_email = To("reshmakarunanidhi@gmail.com")
subject = "Sending the Customers Report"
content = Content("text/plain", "Monthly expenses tracking report till december")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())

print(response.status_code)
print(response.body)
print(response.header)
