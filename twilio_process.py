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


def convert_to_e164(raw_phone):
    """formats phone numbers to twilio format

        >>> convert_to_e164("383.239.2280")
        u'+13832392280'

        >>> convert_to_e164("(934)234-2384")
        u'+19342342384'

    """
    if not raw_phone:
        return
    if raw_phone[0] == '+':
        # Phone number may already be in E.164 format.
        parse_type = None
    else:
        # If no country code information present,
        # assume it's a US number
        parse_type = "US"

    phone_representation = phonenumbers.parse(raw_phone,
                                            parse_type)

    return phonenumbers.format_number(phone_representation,
                        phonenumbers.PhoneNumberFormat.E164)

raw_phone_number = raw_input("Enter a phone number that you would like to send a text message to: ")

phone_number = convert_to_e164(raw_phone_number)

send_text_message(phone_number)
