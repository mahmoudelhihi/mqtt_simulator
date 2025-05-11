import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion as api
import json
import time
import random
import threading
from global_box import GlobalBox
from box import Box
from materials import Materials

BROKER = 'localhost'  # EMQX broker IP or domain
PORT = 1883           # default MQTT port

# Number of simulated sensors
NUM_SENSORS = 3

def sensor_task(client_id, global_box: GlobalBox):
    """Task function for each sensor thread"""
    client = mqtt.Client(client_id=client_id, protocol=mqtt.MQTTv5, callback_api_version=api.VERSION2)
    client.connect(BROKER, PORT)
    client.loop_start()  # Starts background thread for handling MQTT
    
    topic = f'zone_1/{client_id}'
    
    while True:
        for box in global_box.list_box:
            percent = box.fill_box()
            if percent > 85:
                box.collect_box()
        
        client.publish(topic, json.dumps(global_box.to_dict()))
        
        time.sleep(round(random.uniform(1, 2), 2))

def create_threads():
    threads = []
    for i in range(NUM_SENSORS):
        client_id = f"esp32_simulator_{i}"
        
        # Create a fixed number of boxes with stable IDs
        capacity = random.randint(2, 4)  # Each sensor has 2-4 boxes
        
        boxes = []
        for j in range(capacity):
            max_weight = random.randint(10, 30)
            material = random.choice(list(Materials))
            boxes.append(Box(max_weight, material))
        
        global_box = GlobalBox(capacity, boxes)
        
        thread = threading.Thread(target=sensor_task, args=(client_id, global_box), daemon=True)
        thread.start()
        threads.append(thread)
        
        print(f"Started sensor {client_id} with {capacity} boxes")
    
    return threads

# Keep the main program running
def main():
    try:
        threads = create_threads()
        print(f"Simulator is connected to the broker at {BROKER}:{PORT}")
        print(f"Running {NUM_SENSORS} sensors...")
        
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping simulation...")

if __name__ == "__main__":
    main()