import random
import time

while True:
    voltage = round(random.uniform(210, 240), 2)
    current = round(random.uniform(5, 20), 2)
    frequency = round(random.uniform(49.5, 50.5), 2)

    print(f"Voltage: {voltage} V")
    print(f"Current: {current} A")
    print(f"Frequency: {frequency} Hz")
    print("----------------------")

    time.sleep(2)
