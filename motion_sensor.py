# Motion Sensor
import network
from secret import ssid, password
from key import key
from time import sleep
from machine import Pin
import urequests
import gc

gc.collect()

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while not wlan.isconnected():
    print(".", end="")
    sleep(0.5)

motion_sensor = Pin(0, Pin.IN)

print("Connected to WiFi")
print("My IP address is:", wlan.ifconfig()[0])



def send_event():
    event_name = "motion_detected"
    url = f"https://maker.ifttt.com/trigger/{event_name}/json/with/key/{key}"

    urequests.post(url)
    print("Event sent")

detection_window = 5

while True:
    if motion_sensor.value() == 1:
        print("Motion detected")
        send_event()
    else:
        print("No motion")
        # send_event()
    sleep(detection_window)
