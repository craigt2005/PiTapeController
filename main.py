from artnetListener import ArtnetListener
from machine import Pin
import neopixel
import time



def packet_handler(packet):
    if packet["universe"] == 2: # artnet universes are 0 based
        for i in range(0,14):
            np[i] = (packet["channels"][i*3+offset],packet["channels"][i*3+1+offset],packet["channels"][i*3+2+offset])
    

    np.write()
    #print(f"Packet recieved: {packet}")
    
def connection_state_changed_handler(state):
    print(f"New State: {state}")

np = neopixel.NeoPixel(Pin(0),14)

offset = 4

artnet = ArtnetListener()
artnet.on_packet(packet_handler)
artnet.listen()