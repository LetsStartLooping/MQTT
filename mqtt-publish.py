# Import MQTT package
import paho.mqtt.client as mqtt 

# IP Address of the MQTT Broker
mqtt_broker ="X.X.X.X" 

# We can either put IP address of the Broker in the above line, or use can enter it during run-time
if mqtt_broker == "X.X.X.X":
    mqtt_broker = input("Please enter the address of the MQTT Broker: ")

# Create new instance of the MQTT client
# Any name can be used here
client = mqtt.Client("Test-MQTT") 

# Check with user if MQTT Broker requires User ID/Password
protected_broker = input("Is your MQTT client requires User ID/Password? (Y/n) :")

if protected_broker == 'Y' or protected_broker == 'y':
    user_name = input("Please Enter User ID: ")
    password = input("Password for the MQTT client: ")

    # Set user name and password if MQTT client is set-up with one
    # Else following line of code is not required
    client.username_pw_set(user_name, password)


# Connect the client to the broker
client.connect(mqtt_broker) #connect to broker

## MQTT Topic to be publish to
mqtt_topic = input("Please enter MQTT Topic name to which you want to publish a message: ")

## Message to be publis
mqtt_message = input(f"Please entere a message for topic {mqtt_topic}: ")

# Publish MQTT message to the topic
client.publish(mqtt_topic, mqtt_message)
print("Message published")
