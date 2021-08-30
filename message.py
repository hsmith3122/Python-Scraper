from twilio.rest import Client

sid = ''
auth = ''
serverphone = ''

subscribers = []

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
