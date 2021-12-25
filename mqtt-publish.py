# Import MQTT package
import paho.mqtt.client as mqtt 
from time import sleep


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        # Connection Successful
        print("Successfully Connected!\n")
        # At this point we can subscribe to the topics
    else:
        print('Not Able to connect!')
        client.loop_stop()


# IP Address of the MQTT Broker
mqtt_broker ="X.X.X.X" 

# We can either put IP address of the Broker in the above line, or use can enter it during run-time
if mqtt_broker == "X.X.X.X":
    mqtt_broker = input("Please enter the address of the MQTT Broker: ")

# Create new instance of the MQTT client
# Any name can be used here - But each client should have a unique name
client = mqtt.Client("Test-MQTT") 

client.on_connect = on_connect

# Check with user if MQTT Broker requires User ID/Password
protected_broker = input("Is your MQTT client requires User ID/Password? (Y/n) :")

if protected_broker == 'Y' or protected_broker == 'y':
    user_name = input("Please Enter User ID: ")
    password = input("Password for the MQTT client: ")

    # Set user name and password if MQTT client is set-up with one
    # Else following line of code is not required
    client.username_pw_set(user_name, password)


# MQTT Topic to be publish to
mqtt_topic = input("Please enter MQTT Topic name to which you want to publish a message: ")

## Message to be publis
mqtt_message = input(f"Please entere a message for topic {mqtt_topic}: ")

# Connect the client to the broker
client.connect(mqtt_broker) #connect to broker

client.loop_start()
sleep(1)

# Publish MQTT message to the topic
client.publish(mqtt_topic, mqtt_message)
print("Message published")
