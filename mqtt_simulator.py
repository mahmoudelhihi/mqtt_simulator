import paho.mqtt.client as mqtt
import json
import time
import random
import threading
from global_box import GlobalBox
from box import Box
from materials import Materials

broker = 'localhost'  # EMQX broker IP or domain
port = 1883           # default MQTT port

# Number of simulated sensors
NUM_SENSORS = 3

def sensor_task(client_id, global_box : GlobalBox):
    """Task function for each sensor thread"""
    client = mqtt.Client(client_id=client_id, protocol=mqtt.MQTTv5)
    client.connect(broker, port)
    client.loop_start()  # Starts background thread for handling MQTT
    
    while True:
        topic = f'zone_1/{client_id}'
        client.publish(topic, json.dumps(global_box.to_dict()))
        for box in global_box.list_box:
            percent = box.fill_box()
            if percent > 85:
                box.collect_box()
        time.sleep(random.uniform(1, 2))  # Each sensor publishes at 1 Hz

# Create and start a thread for each sensor
def thread():
    threads = []
    for i in range(NUM_SENSORS):
        client_id = f"esp32_simulator_{i}"
        capacity = random.randint(1, NUM_SENSORS)
        boxes = [
            Box(random.uniform(10, 30), random.choice(list(Materials)))
            for i in range(capacity)
        ]
        global_box = GlobalBox(capacity, boxes)
        thread = threading.Thread(target=sensor_task, args=(client_id, global_box), daemon=True)
        thread.start()
        threads.append(thread)

# Keep the main program running
def main():
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping simulation...")

if __name__ == "__main__":
    thread()
    main()