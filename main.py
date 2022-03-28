from pushsafer import Client

client = Client("KeyValue")
"""
client.send_message(
                    "Message",
                    "Title",
                    "Device or Device Group ID",
                    "Icon",
                    "Sound",
                    "Vibration"
"""
resp = client.send_message("this is a message", "Push Notitification", "a", "1", "3", "2")
print(resp)