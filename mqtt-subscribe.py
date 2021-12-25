# Import MQTT package
import paho.mqtt.client as mqtt 
from time import sleep

# This function gets called when we try to connect to MQTT Broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        # Connection Successful
        print("Successfully Connected!\n")
        # At this point we can subscribe to the topics
        # Subscribe to the MQTT topic
        client.subscribe(mqtt_topic)
    else:
        print('Not Able to connect!')
        client.loop_stop()

# This function gets called when cleint receives an MQTT message for a topic client is subscribed to
def on_message(client, userdata, message):
    print("Message Received: ", str(message.payload.decode("utf-8")), " for topic: ", str(message.topic))

# IP Address of the MQTT Broker
mqtt_broker ="X.X.X.X" 

# We can either put IP address of the Broker in the above line, or use can enter it during run-time
if mqtt_broker == "X.X.X.X":
    mqtt_broker = input("Please enter the address of the MQTT Broker: ")

# Create new instance of the MQTT client
# Any name can be used here - But each client should have a unique name
client = mqtt.Client("Test-MQTT") 

client.on_connect = on_connect
client.on_message = on_message

# Check with user if MQTT Broker requires User ID/Password
protected_broker = input("Is your MQTT client requires User ID/Password? (Y/n) :")

if protected_broker == 'Y' or protected_broker == 'y':
    user_name = input("Please Enter User ID: ")
    password = input("Password for the MQTT client: ")

    # Set user name and password if MQTT client is set-up with one
    # Else following line of code is not required
    client.username_pw_set(user_name, password)


## MQTT Topic to be Subscribe to
mqtt_topic = input("Please enter MQTT Topic name to which you want to Subscribe to: ")

# Connect the client to the broker
client.connect(mqtt_broker) #connect to broker

client.loop_forever()





# Run a loop and check through coming MQTT messages for the topic