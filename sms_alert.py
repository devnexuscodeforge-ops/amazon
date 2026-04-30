from twilio.rest import Client

account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Python",
    from_="YOUR_TWILIO_NUMBER",
    to="RECEIVER_NUMBER"
)

print(message.sid)


# if you want to send massage by another way then use this 
