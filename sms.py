from twilio.rest import Client

account_sid = 'AC94f8b06a2617a362b8e0184d44624752'
auth_token = '84da1487b64f4b94497d62b2f97f072f'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+19704144795',
    body='I CANT BELIEVE THIS WORKS',
    to='+27767086619'
)

print(message.sid)
