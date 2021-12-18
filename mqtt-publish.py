# Import MQTT package
import paho.mqtt.client as mqtt 

# IP Address of the MQTT Broker
mqtt_broker ="3.138.55.46" 

# Create new instance of the MQTT client
# Any name can be used here
client = mqtt.Client("Test-MQTT") 

# Connect the client to the broker
client.connect(mqtt_broker) #connect to broker

## MQTT Topic to be publish to
mqtt_topic = "city/soil"

## Message to be publis
mqtt_message = 23.3

# Publish MQTT message to the topic
client.publish(mqtt_topic,mqtt_message)
print("Message published")
