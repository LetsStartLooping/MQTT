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

# Connect the client to the broker
client.connect(mqtt_broker) #connect to broker

## MQTT Topic to be Subscribe to
mqtt_topic = input("Please enter MQTT Topic name to which you want to Subscribe to: ")

# Subscribe to the MQTT topic
client.subscribe(mqtt_topic)

# Run a loop and check through coming MQTT messages for the topic