# MQTT in Python

### Install MQTT client library

To work with MQTT in Python we can use one of the following options based on the current `pip` version your system is using

```shell
pip install paho-mqtt
```

or

```bash
pip3 install paho-mqtt
```

### Connect to MQTT Broker

1. Import Library to perform MQTT operations

```python
import paho.mqtt.client as mqtt
```

2. As next step we can crate a client using following command, and give it a unique name of your choice

```python
client = mqtt.Client("T	est-MQTT") 
```

3. Connect the client to the MQTT Broker, MQTT broker is the name of the broker or the IP address of the MQTT broker device. This could running at your local Raspberry Pi or MQTT broker running on AWS

```python
client.connect(mqtt_broker)
```

4. Following step is optional if MQTT Broker is protected by user-id and password

```python
client.username_pw_set(user_name, password)
```

### Publish MQTT Message

To publish a MQTT message we need an MQTT topic and the message we want to publish. Following simple command can be used for the same. Here `mqtt_topic` is a string which is name of the topic and `mqtt_message` is another string which contains the message we want to publish to `mqtt_topic`.

```python
client.publish(mqtt_topic, mqtt_message)
```

As an example if a topic name is "home/temperature" and value of the temperature is 23.4, then we can publish this in following way and all MQTT clients subscribed to topic "home/temperature" will get this message

```python
client.publish("home/temperature", "23.4")
```

Here is the [link](https://github.com/LetsStartLooping/MQTT/blob/5d0260a2e90e2cf4d1214ee04fb3810cc225a430/mqtt-publish.py) to sample complete working code to publish a message to MQTT client

### Subscribe to MQTT Topic

To subscribe to a MQTT Topic following command can be used in python. Once this is done, then any message published by any client to this topic will be received by the client subscribed to a perticular MQTT topic

```python
# Subscribe to the MQTT topic
client.subscribe(mqtt_topic)
```

For example, if a client is subscribed to the topic "home/temperature". Then it will receive the above published message of "23.4"

```python
client.subscribe("home/temperature")
```

### Listen to MQTT Messages

Just subscribing to a topic in MQTT messages is not enough, we also need a way to receive and decode the incoming MQTT topics and messages.

**This Page is under construction**