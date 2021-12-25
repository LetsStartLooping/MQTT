# MQTT via Command Line (mosquitto_pub & mosquitto_sub)

This section introduces how to use `mosquitto_sub` and `mosquitto_pub` to Subscribe and Publish MQTT messages

Let's take the example where we will be using following MQTT details

`broker_address`: Name or IP address of the MQTT Broker. e.g. 192.168.1.24
`topic`: Name of the topic we want to subscribe and send message. e.g. `room/temperature`
`message`: This is our message which can be any string or json message. e.g. `23.45`

Optional Parameters: If MQTT broker is password protected then we also need to provide User ID and password details while subscribing to publishing messages

`user_id`: A valid UserID for MQTT Broker. e.g. `USER01`
`password`: Password for the above user id. e.g. `test1234`

## Subscribe to a topic in MQTT

We can use following command to subscribe to a topic. Here I will be using datails from the above example we have taken

```bash
mosquitto_sub -h 192.168.1.24 -t room/temperature 
```
So, with this simple command by just providing Broker address and topic name we can subscribe to a topic in MQTT. 

* `-h`: This option is to provide host name for MQTT Broker
* `-t`: This option is to provide name of the MQTT topic

If MQTT broker is password protected then 
```bash
mosquitto_sub -h 192.168.1.24 -t room/temperature  -u USER01 -P test1234
```

* `-u`: This option is to provide user name
* `-P`: This option is to provide a password

By default MQTT port is `1883`. But incase a different port is used, then that can also be specified by using option `-p` like following

```bash
mosquitto_sub -h 192.168.1.24 -p 1883 -t room/temperature  -u USER01 -P test1234
```

## Publish a message to a topic in MQTT

Publishing a message to a topic in MQTT is quite similar and that can be done by using `-m` option along with `mosquitto_pub` command. Rest of the syntax remains the same as `mosquitto_sub`

```bash
mosquitto_pub -h 192.168.1.24 -p 1883 -t room/temperature  -u USER01 -P test1234 -m "23.45"
```