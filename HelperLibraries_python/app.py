from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "  "

# Your Auth Token from twilio.com/console
auth_token = " "

client = Client(account_sid,auth_token)

message = client.messages.create(
          to = '+918464056887',
          from_= " +17627877482",
            body = "Hello message from Python"
)

print(f"Created a new message:{message.sid}")

# when yo want to delete all the messages
#for messg in client.messages.list():
#    print(f"Deleting {messg.body}")
#    messg.delete()
