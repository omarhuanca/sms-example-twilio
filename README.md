Sending a Text Message - Twilio
-------------------------------


**Description**

A script that ask for a phone number and sends a text message to that number


**How it works**

Using [Twilio](https://www.twilio.com/)'s python wrapper and API, the script ask the user for their phone number and send a text message to that number.   

Step-by-step guide on how the script works and connecting it to Twilio by [chatasweetie](https://chatasweetie.com/) on the post:[Twilio - 2 Ways of Sending Text Message](http://chatasweetie.com/2016/12/19/twilio-2-ways-of-sending-text-message)


### Technology Stack

Python, Twilio


### Screenshot

**Script being run**

<img src="img/script.png">


### How to run Script locally

Create a virtual environment 

```
> virtualenv env
> source env/bin/activate
```

Install the dependencies

```
> pip install -r requirements.txt
```

Source twilio keys
```
> source keys.sh
```

Run script
```
> python twilio_process.py
```


Note: The messaging functionality requires that you have a [Twilio](https://www.twilio.com/) account id, authorization token and phone number set as local environment variables:

```
TWILIO_ACCOUNT_SID
TWILIO_AUTH_TOKEN
TWILIO_NUMBER
```

### About the Developer    
Jessica Dene Earley    
[Bio](https://chatasweetie.com/about-me/)   
[Linkedin](https://www.linkedin.com/in/jessicaearley)    
[Blog](https://chatasweetie.com/)    
