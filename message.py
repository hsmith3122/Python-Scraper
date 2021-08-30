from twilio.rest import Client

sid = 'ACf654ab9089758f9277afb2f9addee727'
auth = '404814a1ee603d76521917be10f463ee'
serverphone = '+15132702972'


phone_herb = '+12058088345'
phone_ahjah = '+12343001719'

phone_all = [phone_herb, phone_ahjah]

client = Client(sid, auth)

def sendText(toPhone, msg):
    if len(sid) == 0:
        print(msg)
        print("\a")     # Notification Bell on Windows/Linux
    else:
        return client.messages.create(
            body=msg,
            from_=serverphone,
            to=toPhone if isinstance(toPhone, str) else ','.join(toPhone)
    )
