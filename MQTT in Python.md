# MQTT in Python

### Install MQTT client for Python with one of the following options

```shell
pip install paho-mqtt
```

or

```bash
pip3 install paho-mqtt
```

#### Import Library

```python
import paho.mqtt.client as mqtt
```

As next step we can crate a client using following command, and give it a unique name of your choice

```python
client = mqtt.Client("Test-MQTT") 
```

