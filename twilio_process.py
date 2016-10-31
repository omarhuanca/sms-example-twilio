# Sends a text message using Twilio
import twilio
from twilio.rest import TwilioRestClient
import os

# Twilio Account Information
TWILIO_ACCOUNT_SID=os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN=os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER=os.environ.get("TWILIO_NUMBER")


def send_text_message(phone):
    """sends a text message to the phone number"""

    print 'sending text message'

    try:
        client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages.create(
            body="Your a kickass programmer",
            to=phone,
            from_=TWILIO_NUMBER
        )
    except twilio.TwilioRestException as e:
        print e


phone_number = raw_input("Enter a phone number that you would like to send a text message to: ")

send_text_message(phone_number)
