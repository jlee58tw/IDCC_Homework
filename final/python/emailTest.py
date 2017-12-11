import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__)+'../', 'web'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
from django.conf import settings
from mailqueue.models import MailerMessage

new_message = MailerMessage()
new_message.subject = "My Subject"
new_message.to_address = "ba911y2@gmail.com"
new_message.bcc_address = ""
new_message.from_address = "hihiticket@gmail.com"
new_message.content = "Mail content"
new_message.html_content = "<h1>Mail Content</h1>"
new_message.app = "Name of your App that is sending the email."
new_message.save()
