import subprocess
import paho.mqtt.publish as publish

# Define the MQTT broker details
broker_address = "localhost"
broker_port = 1883
broker_username = "admin"
broker_password = "password"
mqtt_topic = "/log/ufw"


# Open the ufw.log file for tailing
tail_process = subprocess.Popen(["tail", "-F", "/var/log/ufw.log"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Continuously read lines from the tail process and publish them to MQTT
while True:
        #print("start")
        while True:
                line = tail_process.stdout.readline().decode().strip()
                if line:
                        #print(line)
                        publish.single(mqtt_topic, line, hostname=broker_address, port=broker_port)
