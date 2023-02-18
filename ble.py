import requests
import tkinter as tk
from tkinter import ttk
import rumps

# IP Address of device
device_ip = "192.168.1.100"

# Creating URL
posurl = f"http://{device_ip}/api/shutter/state"
print(posurl)
# Sending GET
response = requests.get(posurl)
# Getting response info 
def get_shade_status():
    if response.status_code == 200:
       return response.json()["shutter"]["currentPos"]["position"]
    else:
       return None
# Shutter position
def set_shade_position(position):
    url = f"http://{device_ip}/s/p/{position}"
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        return True
    else:
        return False
# slider definition
def on_slider_change(val):
    position = int(float(val))
    set_shade_position(position)
    response_json = get_shade_status()
    if response_json:
        print("The shutter position has been set to", position, "%")
        print("API Response:", response_json)
    else:
        print("Failed to adjust the position of the blind.")

response_poz = get_shade_status()

root = tk.Tk()
root.title("Setting the position of the blind")
root.geometry('100x400')
slider = tk.Scale(root, from_=0, to=100, orient="vertical", resolution=10, length=500, command=on_slider_change)
slider.pack()
slider.set(response_poz)
root.mainloop()
