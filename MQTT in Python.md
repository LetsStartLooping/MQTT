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

4. To publish a MQTT message we need an MQTT topic and the message we want to publish. Following simple command can be used for the same. Here `mqtt_topic` is a string which is name of the topic and `mqtt_message` is another string which contains the message we want to publish to `mqtt_topic`.

```python
client.publish(mqtt_topic, mqtt_message)
```

As an example if a topic name is "home/temperature" and value of the temperature is 23.4, then we can publish this in following way and all MQTT clients subscribed to topic "home/temperature" will get this message

```python
client.publish("home/temperature", "23.4")
```

Here is the [link](https://github.com/LetsStartLooping/MQTT/blob/84c2592375d3e74dd7483945f89ffe5954b66dc8/mqtt-publish.py) to sample complete working code to publish a message to MQTT client