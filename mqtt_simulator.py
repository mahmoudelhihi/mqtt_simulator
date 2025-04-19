import paho.mqtt.client as mqtt
import json
import time
import random
import threading

broker = 'localhost'  # EMQX broker IP or domain
port = 1883           # default MQTT port

# Number of simulated sensors
NUM_SENSORS = 3

def sensor_task(client_id):
    """Task function for each sensor thread"""
    client = mqtt.Client(client_id=client_id, protocol=mqtt.MQTTv5)
    client.connect(broker, port)
    
    while True:
        payload = {
            'weight': round(random.uniform(100, 200), 2),
            'lat': round(random.uniform(30, 45), 6),
            'lng': round(random.uniform(-120, -70), 6),
            'timestamp': int(time.time())
        }
        topic = f'weight/{client_id}'
        client.publish(topic, json.dumps(payload))
        print(f'Published to {topic}: {payload}')
        time.sleep(random.uniform(1, 2))  # Each sensor publishes at 1 Hz

# Create and start a thread for each sensor
def thread():
    threads = []
    for i in range(NUM_SENSORS):
        client_id = f"esp32_simulator_{i}"
        thread = threading.Thread(target=sensor_task, args=(client_id,), daemon=True)
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