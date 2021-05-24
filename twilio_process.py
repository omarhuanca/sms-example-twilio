# Sends a text message using Twilio
import twilio
from twilio.rest import Client
import phonenumbers

# Twilio Account Information
TWILIO_ACCOUNT_SID="AC21508f4563959ebe831d5d269b2c67a0"
TWILIO_AUTH_TOKEN="1f1299710c185e146239ec2891ededea"
TWILIO_NUMBER="+19792014980"


def send_text_message(phone):
    """sends a text message to the phone number"""

    print('sending text message')

    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages.create(
            body="Hello from flask application",
            to=phone,
            from_=TWILIO_NUMBER
        )
    except twilio.TwilioRestException as e:
        print(e)


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
        parse_type = "BO"

    phone_representation = phonenumbers.parse(raw_phone,
                                            parse_type)

    return phonenumbers.format_number(phone_representation,
                        phonenumbers.PhoneNumberFormat.E164)

raw_phone_number = input("Enter a phone number that you would like to send a text message to: ")

phone_number = convert_to_e164(raw_phone_number)

send_text_message(phone_number)
