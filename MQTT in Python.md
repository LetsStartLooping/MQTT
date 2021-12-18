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

Import Library to perform MQTT operations

```python
import paho.mqtt.client as mqtt
```

As next step we can crate a client using following command, and give it a unique name of your choice

```python
client = mqtt.Client("Test-MQTT") 
```

